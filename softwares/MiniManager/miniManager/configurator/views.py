import json
from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import *
from .xmlSchemaGenerator import XMLSchemaGenerator

class ConfigurationView():
    def getHelper(self):
        pmodels = PModelCatalog.objects.all()
        mmodels = MModelCatalog.objects.all()
        measures = Measure.objects.all()
        pmeasures = PerformanceMeasure.objects.all

        return {"pmodels": pmodels, "mmodels": mmodels, "measures": measures, "pmeasures": pmeasures}

    def __saveMeasurements(self, request, configuration):
        paramlist = request.POST.getlist('radiofrequency')
        for param in paramlist:
            measureName = str(param)
            measure = Measure.objects.get(name=measureName)

            period=request.POST.get(measureName)
            measurement = Measurement(period=period, measure=measure, config=configuration)
            measurement.save()

        hasPerformanceMeasurement = request.POST.get('performancemeasure')
        if hasPerformanceMeasurement:
            name = request.POST.get('performancemeasure_name')
            source = request.POST.get('performancemeasuresource')
            destination = request.POST.get('performancemeasuredestination')
            period = request.POST.get('performanceperiod')

            measure = PerformanceMeasure.objects.get(name=name)
            measurement = PerformanceMeasurement(period=period, source=source, destination=destination, measure=measure, config=configuration)
            measurement.save()
            

        xmlSchemaGenerator = XMLSchemaGenerator()
        return xmlSchemaGenerator.generate(paramlist)

    def __parseAttributes(self, attributesString):
        attributesString.strip()
        if (attributesString == ""):
            return []

        if "," in attributesString:
            return attributesString.split(",")

        return [attributesString]
    
    def __saveNode(self, request, network, nodeID):
        type = request.POST.get(nodeID + "-" + "type")

        nodeTypeToSaverMap = {
            "station": Station,
            "accesspoint": AccessPoint,
            "host": Host,
            "switch": Switch
        }

        nodeClass = nodeTypeToSaverMap[type]

        specificAttributeString = request.POST.get(type+"_specific_attribute")
        specificAttributes = self.__parseAttributes(specificAttributeString)
            
        nodeAttributeString = request.POST.get(type+"_node_attribute")
        nodeAttributes = self.__parseAttributes(nodeAttributeString)

        interfaceAttributeString = request.POST.get(type+"_interface_attribute")
        interfaceAttributes = self.__parseAttributes(interfaceAttributeString)

        nodeParams = {}
        for attr in nodeAttributes:
            nodeParams[attr] = request.POST.get(nodeID + "-" + attr)
        node = Node(network = network, type = type, **nodeParams)
        node.save()

        specParams = {}
        for attr in specificAttributes:
            specParams[attr] = request.POST.get(nodeID + "-" + attr)
        spec = nodeClass(node = node, **specParams)
        spec.save()

        interfaceParams = {}
        for attr in interfaceAttributes:
            interfaceParams[attr] = request.POST.get(nodeID + "-" + attr)
        interface = Interface(name=node.name + "int", node=node, **interfaceParams)
        interface.save()

        return node.name, interface.id

    def __saveNodes(self, request, network):
        nodesString = request.POST.get('nodes')
        nodes = nodesString.split(",")

        nodeToInterfaceMap = {}

        for nodeID in nodes:
            nodeName, interfaceID = self.__saveNode(request, network, nodeID)
            nodeToInterfaceMap[nodeName] = interfaceID

        return nodeToInterfaceMap
            
    def __saveLink(self, request, linkID, nodeToInterfaceMap):
        node1 = request.POST.get(linkID + "-" + "node1")
        node2 = request.POST.get(linkID + "-" + "node2")

        linkAttributes = ["bw", "delay", "loss", "max_queue_size", "jitter"]
        linkObj = {}
        for attr in linkAttributes:
            linkObj[attr] = request.POST.get(linkID + "-" + attr)

        int1 = nodeToInterfaceMap[node1]
        int2 = nodeToInterfaceMap[node2]

        link = Link(int1_id = int1, int2_id = int2, **linkObj)
        link.save()
    
    def __saveLinks(self, request, nodeToInterfaceMap):
        linksString = request.POST.get('links')
        links = linksString.split(",")

        for linkID in links:
            self.__saveLink(request, linkID, nodeToInterfaceMap)

    def __saveNetwork(self, request):
        adhoc = request.POST.get('adhoc') == 'on'
        fading_cof = request.POST.get('fading_cof')
        noise_th = request.POST.get('noise_th')

        network = Network(adhoc=adhoc, fading_cof=fading_cof, noise_th=noise_th)
        network.save()
        return network
    
    def __savePropagationModel(self, request):
        pmodelSelected = request.POST.get('propagationmodel')
        pmodel = PModelCatalog.objects.get(name=pmodelSelected)
        propagationmodel = PropagationModel(model=pmodel)
        propagationmodel.save()

        propagationParamsString = request.POST.get("{}attribute".format(pmodelSelected))
        propagationParams = []
        if propagationParamsString:
            propagationParams = propagationParamsString.split(",")
        for param in propagationParams:
            value = request.POST.get(param)
            propagationparam = PropagationParam(name=param, value=value, propagationmodel=propagationmodel)
            propagationparam.save()

        return propagationmodel

    def __saveMobilityModel(self, request):
        mmodelSelected = request.POST.get('mobilitymodel')
        mmodel=MModelCatalog.objects.get(name=mmodelSelected)
        mobilitymodel=MobilityModel(model=mmodel)
        mobilitymodel.save()

        mobilityParamsString = request.POST.get("{}attribute".format(mmodelSelected))
        mobilityParams = []
        if mobilityParamsString:
            mobilityParams = mobilityParamsString.split(",")
        for param in mobilityParams:
            value=request.POST.get(param)
            mobilityparam = MobilityParam(name=param, value=value, mobilitymodel=mobilitymodel)
            mobilityparam.save()

        return mobilitymodel

    def postHelper(self, request):
        propagationmodel = self.__savePropagationModel(request)
        mobilitymodel = self.__saveMobilityModel(request)
        network = self.__saveNetwork(request)
        nodeToInterfaceMap = self.__saveNodes(request, network)
        self.__saveLinks(request, nodeToInterfaceMap)

        configuration = Configuration(medicao_schema='xml_schema', propagationmodel=propagationmodel, mobilitymodel=mobilitymodel, network=network)
        configuration.save()

        configuration.medicao_schema = self.__saveMeasurements(request, configuration)
        configuration.save()

        return configuration

class VersionView(ConfigurationView, View):
    def get(self, request, test_plan_id):
        testPlan = TestPlan.objects.get(id=test_plan_id)
        args = {"error": False, "errorMessage": "", "testPlan": testPlan}
        args.update(self.getHelper())

        return render(request, 'version.html', args)

    def post(self, request):
        versionName = request.POST.get('version_name')
        testPlanID = request.POST.get('test-plan')

        if Version.objects.filter(name=versionName, test_plan_id=testPlanID).exists():
            testPlan = TestPlan.objects.get(id=testPlanID)
            args = {"error": True, "errorMessage": "Já existe uma versão com esse nome", "testPlan": testPlan}
            args.update(self.getHelper())
            return render(request, 'version.html', args)

        try:
            configuration = self.postHelper(request)
            version = Version(name=versionName, test_plan_id = testPlanID, configuration=configuration)
            version.save()
        except:
            testPlan = TestPlan.objects.get(id=testPlanID)
            args = {"error": True, "errorMessage": "Ocorreu um erro ao salvar a versão, verifique os dados inseridos", "testPlan": testPlan}
            args.update(self.getHelper())
            return render(request, 'version.html', args)

        url = reverse('versions', kwargs={ 'test_plan_id': testPlanID })
        return HttpResponseRedirect(url)

class VersionsView(View):
    def get(self, request, test_plan_id):
        testPlan = TestPlan.objects.get(id=test_plan_id)
        versions = Version.objects.filter(test_plan_id=testPlan.id).all().order_by('-created_at')
        args = {"versions": versions, "testPlan": testPlan}
        return render(request, 'versions.html', args)

class HomeView(View):
    def get(self, request):
        args = {"error": False, "errorMessage": ""}
        return render(request, 'home.html', args)



class TestPlanView(View):
    def get(self, request):
        args = {"error": False, "errorMessage": ""}
        return render(request, 'test-plan.html', args)

    def post(self, request):
        testPlanName = request.POST.get('test-plan_name')

        if TestPlan.objects.filter(name=testPlanName).exists():
            args = {"error": True, "errorMessage": "Já existe um plano de teste com esse nome"}
            return render(request, 'test-plan.html', args)

        testPlanDescription = request.POST.get('test-plan_description')
        testplanAuthor = request.POST.get('test-plan_author')

        try:
            testPlan = TestPlan(name=testPlanName, author = testplanAuthor, description = testPlanDescription)
            testPlan.save()
        except:
            args = {"error": True, "errorMessage": "Ocorreu um erro ao salvar o plano de teste, verifique os dados inseridos"}
            return render(request, 'test-plan.html', args)

        url = reverse('test-plans')
        return HttpResponseRedirect(url)

class TestPlansView(View):
    def get(self, request):
        testPlans = TestPlan.objects.all().order_by('-created_at')
        args = {"testPlans": testPlans}
        return render(request, 'test-plans.html', args)

class ExportVersionView(View):
    def get(self, request, version_id):
        version = Version.objects.get(id=version_id)
        configurationObj = version.configuration.getConfigurationObj()

        jsonString = json.dumps(configurationObj, default=lambda o: o.__dict__, indent=4)
        response = HttpResponse(jsonString, content_type="application/json")
        response['Content-Disposition'] = 'attachment; filename={}.json'.format(version.name)
        return response