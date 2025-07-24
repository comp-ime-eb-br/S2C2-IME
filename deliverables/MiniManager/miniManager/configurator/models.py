from django.db import models

class TestPlan(models.Model):
    name = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(null = True)
    author = models.CharField(max_length=50, null = True)

    class Meta:
        db_table = "TestPlan"

class Network(models.Model):
    noise_th = models.IntegerField(default=-91)
    fading_cof = models.IntegerField(default=0)
    adhoc = models.BooleanField(default=False)
    
    class Meta:
        db_table="Network"

    def seialize(self):
        return {"adhoc": self.adhoc, "args": {"fading_cof": self.fading_cof, "noise_th": self.noise_th}}

#class NetworkController(models.Model): /vamos usar o Controller do mininet.node
    #protocol = models.CharField(max_length=30)

#PModelCatalog works as a catalog of propagation models
class PModelCatalog(models.Model): 
    name = models.CharField(max_length=30)
    displayname = models.CharField(max_length=30)

    class Meta:
        db_table = "PModelCatalog"

class MModelCatalog(models.Model): 
    name = models.CharField(max_length=30)
    displayname = models.CharField(max_length=30)

    class Meta:
        db_table = "MModelCatalog"

class PropagationModel(models.Model):
    model = models.ForeignKey(PModelCatalog, on_delete=models.CASCADE)

    class Meta:
        db_table = "PropagationModel"

class MobilityModel(models.Model):
    model = models.ForeignKey(MModelCatalog, on_delete=models.CASCADE)

    class Meta:
        db_table = "MobilityModel"
class Measure(models.Model):
    name = models.CharField(max_length=20)
    unit = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        db_table = "Measures"

class PerformanceMeasure(models.Model):
    name = models.CharField(max_length=30)
    unit = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        db_table = "PerformanceMeasure"

class PropagationParam(models.Model):
    name = models.CharField(max_length=30)
    value = models.FloatField()
    propagationmodel = models.ForeignKey(PropagationModel, on_delete=models.CASCADE)

    class Meta:
        db_table = "PropagationParam"

class MobilityParam(models.Model):
    name = models.CharField(max_length=30)
    value = models.FloatField()
    mobilitymodel = models.ForeignKey(MobilityModel, on_delete=models.CASCADE)

    class Meta:
        db_table = "MobilityParam"

class Node(models.Model):
    name = models.CharField(max_length=30)
    mac = models.CharField(max_length=30)
    type = models.CharField(max_length=30, blank=True, null=True)
    network = models.ForeignKey(Network, on_delete=models.CASCADE)

    class Meta:
        db_table = "Node"

    def getTypeWithAttributes(self):
        nodeTypeToSpecialization = {
            "station": Station,
            "accesspoint": AccessPoint,
            "host": Host,
            "switch": Switch
        }

        return nodeTypeToSpecialization[self.type].objects.get(node_id = self.id).serialize()

    def getInterface(self):
        return Interface.objects.get(node_id = self.id).serialize()

    def serialize(self):
        specializationArgs = self.getTypeWithAttributes()
        interface = self.getInterface()
        return {"name": self.name, "mac": self.mac, "type": self.type, "args": specializationArgs, "interface": interface}

class Station(models.Model):
    node = models.OneToOneField(Node, on_delete=models.CASCADE, unique=True)

    class Meta:
        db_table = "Station"
    
    def serialize(self):
        return {}

class Host(models.Model):
    node = models.OneToOneField(Node, on_delete=models.CASCADE, unique=True)

    class Meta:
        db_table = "Host"

    def serialize(self):
        return {}

class Switch(models.Model):
    node = models.OneToOneField(Node,on_delete=models.CASCADE, unique=True)
    
    class Meta:
        db_table="Switch"

    def serialize(self):
        return {}

class AccessPoint(models.Model):
    ssid = models.CharField(max_length=30)
    mode = models.CharField(max_length=30)
    channel = models.CharField(max_length=30)
    node = models.OneToOneField(Node,on_delete=models.CASCADE, unique=True)

    class Meta:
        db_table = "AccessPoint"

    def serialize(self):
        return {"ssid": self.ssid, "mode": self.mode, "channel": self.channel}

class Interface(models.Model):
    name = models.CharField(max_length=30)
    ip = models.CharField(max_length=30)
    node = models.ForeignKey(Node, on_delete=models.CASCADE) 

    class Meta:
        db_table = "Interface"

    def serialize(self):
        args = {"ip": self.ip}
        return {"id": self.id, "name": self.name, "args": args}

class Link(models.Model):
    int1 = models.ForeignKey(Interface, related_name='int1', on_delete=models.CASCADE, null=True)
    int2 = models.ForeignKey(Interface, related_name='int2', on_delete=models.CASCADE, null=True)
    bw = models.IntegerField(blank=True, null=True)
    delay = models.IntegerField(blank=True, null=True)
    loss = models.IntegerField(blank=True, null=True)
    max_queue_size = models.IntegerField(blank=True, null=True)
    jitter = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table="Link"

    def serialize(self):
        args = {"bw": self.bw, "delay": self.delay, "loss": self.loss, "max_queue_size": self.max_queue_size, "jitter": self.jitter}
        return {"node1": self.int1.node.name, "node2": self.int2.node.name, "args": args}

class Mobility(models.Model):
    tempo = models.FloatField()
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    node = models.ForeignKey(Node, on_delete=models.CASCADE)
    class Meta:
        db_table = "Mobility"

class Position(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    node = models.ForeignKey(Node, on_delete=models.CASCADE)
   
    class Meta:
        db_table = "Position"

class Configuration(models.Model):
    medicao_schema = models.TextField()
    propagationmodel = models.ForeignKey(PropagationModel, on_delete=models.CASCADE, null= True)
    mobilitymodel = models.ForeignKey(MobilityModel, on_delete = models.CASCADE, null=True)
    stop_time = models.IntegerField(null=True)
    network = models.ForeignKey(Network, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "Configuration"

    def getNodes(self):
        result = []
        nodes = Node.objects.filter(network_id = self.network.id)

        for node in nodes:
            nodeObj = node.serialize()
            result.append(nodeObj)

        return result

    def getLinks(self, nodes):
        links = []
        for node in nodes:
            foundedLinks = Link.objects.filter(int1_id = node["interface"]["id"]).all()
            for link in foundedLinks:
                links.append(link.serialize())

        return links

    def getMeasurements(self):
        result = []
        measurements = Measurement.objects.filter(config_id = self.id)
        for measurement in measurements:
            result.append({"period": measurement.period, "measure": {"name": measurement.measure.name}})

        return result

    def getPerformanceMeasurements(self):
        result = []
        measurements = PerformanceMeasurement.objects.filter(config_id = self.id)
        for measurement in measurements:
            result.append({"period": measurement.period, "source": measurement.source, "destination": measurement.destination, "measure": {"name": measurement.measure.name}})

        return result

    def getPropagationModel(self):
        propagationmodel = self.propagationmodel
        args = {}
        params = PropagationParam.objects.filter(propagationmodel_id = propagationmodel.id)
        for param in params:
            args[param.name] = param.value

        return {"model": propagationmodel.model.name, "args": args}

    def getMobilityModel(self):
        mobilitymodel = self.mobilitymodel
        args = {}
        params = MobilityParam.objects.filter(mobilitymodel_id = mobilitymodel.id)
        for param in params:
            args[param.name] = param.value

        return {"model": mobilitymodel.model.name, "args": args}

    def getConfigurationObj(self):
        nodes = self.getNodes()
        return {
            "network": self.network.seialize(),
            "radioFrequencyMeasurements": self.getMeasurements(),
            "performanceMeasurements": self.getPerformanceMeasurements(),
            "propagationModel": self.getPropagationModel(),
            "mobilityModel": self.getMobilityModel(),
            "nodes": nodes,
            "links": self.getLinks(nodes)
        }

class PerformanceMeasurement(models.Model):
    period = models.IntegerField()
    measure = models.ForeignKey(PerformanceMeasure, on_delete=models.CASCADE)
    config = models.ForeignKey(Configuration, on_delete=models.CASCADE)
    source = models.CharField(max_length=20)
    destination = models.CharField(max_length=20)

    class Meta:
        db_table = "PerformanceMeasurement"

class Measurement(models.Model):
    period = models.IntegerField()
    measure = models.ForeignKey(Measure, on_delete=models.CASCADE)
    config = models.ForeignKey(Configuration, on_delete=models.CASCADE)

    class Meta:
        db_table = "Measurement"

class Version(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    test_plan = models.ForeignKey(TestPlan, models.CASCADE, blank=True, null=True, unique=False)
    configuration = models.OneToOneField(Configuration, models.CASCADE, unique=True, blank=True, null=True)

    class Meta:
        db_table = "Version"