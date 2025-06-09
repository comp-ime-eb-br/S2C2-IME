from django.views import View
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.template.defaultfilters import register

from mininetWifiAdapter import MininetWifiExp, ResultNotifier
from provenanceCatcher import ProvenanceService
from configurator import ConfiguratorService

from .listener import ExperimentListener
from .experimentsQueue import ExperimentsQueue
from .models import Round
from .constants import ExperimenterConstants

class RoundsView(View):
    def get(self, request, version_id):
        args = {}
        args['version'] = ConfiguratorService().getVersionByID(version_id)
        args['rounds'] = Round.objects.filter(version_id=version_id).order_by('-start')
        return render(request, 'rounds.html', args)

class RoundView(View):
    def get(self, request, round_id):
        args = {}
        round = Round.objects.get(id=round_id)
        args['round'] = round

        
        configuration = round.version.configuration
        radioFrequencyMeasurements = configuration.getMeasurements()
        
        args["radioFrequencyTitles"] = ["time", "name"]+[measurement["measure"]["name"] for measurement in radioFrequencyMeasurements]
        args["performanceTitles"] = ExperimenterConstants.PERFORMANCE_TITLES

        if round.status == Round.DONE:
            args['radioFrequency'], args['performance'] = ProvenanceService().getResultRowsFromRound(round.id, configuration.medicao_schema, args["radioFrequencyTitles"])

        return render(request, 'round.html', args)

    def post(self, request):
        versionID = request.POST.get('version')
        version = ConfiguratorService().getVersionByID(versionID)

        total = Round.objects.filter(version_id=versionID).count()
        name = "{} - rodada {}".format(version.name, total + 1)        
        round = Round(name=name, version_id = versionID)
        round.save()

        self.__enqueueExperiment(version.configuration, round.id)

        url = reverse('round', kwargs={ 'round_id': round.id })
        return HttpResponseRedirect(url)

    def __enqueueExperiment(self, configuration, roundID):
        experimentListener = ExperimentListener(roundID)
        notifier = ResultNotifier()
        notifier.attach(experimentListener)
        
        configurationObj = configuration.getConfigurationObj()
        
        mininetWifiExp = MininetWifiExp(notifier, configurationObj)
        queue = ExperimentsQueue.instance()
        queue.add(mininetWifiExp, roundID, configuration.medicao_schema)

class FinishRoundView(View):
    def post(self, request):
        roundID = request.POST.get('round')
        queue = ExperimentsQueue.instance()
        queue.finishExperiment(roundID)
        
        round = Round.objects.get(id=roundID)
        url = reverse('rounds', kwargs={ 'version_id': round.version_id })
        return HttpResponseRedirect(url)

class ExportRoundView(View):
    def get(self, request, round_id):
        round = Round.objects.get(id=round_id)
        xml = ProvenanceService().getXML(round.id)

        response = HttpResponse(xml, content_type="application/xml")
        response['Content-Disposition'] = 'attachment; filename={}.xml'.format(round.name)
        return response

class CompareRoundsView(View):
    def get(self, request):
        roundID1 = request.GET.get('round1')
        roundID2 = request.GET.get('round2')
        round1 = Round.objects.get(id=roundID1)
        round2 = Round.objects.get(id=roundID2)
        args = {"round1": round1.name, "round2": round2.name, "hasError": False}

        isRoundsDone = round1.isDone() and round2.isDone()
        if not isRoundsDone:
            args["hasError"] = True
            args["errorMessage"] = ExperimenterConstants.ROUND_NOT_DONE_ERROR
            return render(request, 'compare-rounds.html', args)
            
        configuration1 = round1.version.configuration
        radioFrequencyMeasures1 = [measurement["measure"]["name"] for measurement in configuration1.getMeasurements()]
        configuration2 = round1.version.configuration
        radioFrequencyMeasures2 = [measurement["measure"]["name"] for measurement in configuration2.getMeasurements()]

        args["radioFrequencyTitles"] = ["time", "name"]+[value for value in radioFrequencyMeasures1 if value in radioFrequencyMeasures2]
        args["performanceTitles"] = ExperimenterConstants.PERFORMANCE_TITLES

        try:
            service = ProvenanceService()
            diffResults = service.diffResults(roundID1, roundID2, configuration1.medicao_schema, configuration2.medicao_schema, args["radioFrequencyTitles"])
            args["radioFrequency"], args["performance"] = diffResults
        except:
            args["hasError"] = True
            args["errorMessage"] = ExperimenterConstants.COMPARE_ROUNDS_ERROR
        finally:
            return render(request, 'compare-rounds.html', args)

    def post(self, request):
        roundName1 = request.POST.get('round1')
        roundName2 = request.POST.get('round2')
        try:
            round1 = Round.objects.filter(name=roundName1).first()
            round2 = Round.objects.filter(name=roundName2).first()
            round1ID = round1.id
            round2ID = round2.id
            return HttpResponseRedirect('/compare-rounds?round1='+str(round1ID)+'&round2='+str(round2ID))
        except:
            testPlanID = request.POST.get('test-plan')
            return HttpResponseRedirect('/versions/'+str(testPlanID))


@register.filter(name='dict_key')
def dict_key(d, k):
    return d[k]

@register.filter(name='round_message')
def round_message(status):
    STATUS_TO_MESSAGE = {
      "WAITING": "Em espera",
      "STARTING": "Inicializando",
      "IN_PROGRESS": "Executando",
      "DONE": "Finalizado"
    }

    return STATUS_TO_MESSAGE[status]

@register.filter(name='type_signal')
def round_message(status):
    if not status:
        return ""

    TYPE_TO_SIGNAL = {
      "KEEP": "",
      "ADD": "+",
      "REMOVE": "-"
    }

    return TYPE_TO_SIGNAL[status]

@register.filter(name='type_style')
def round_message(status):
    if not status:
        return ""


    TYPE_TO_STYLE = {
      "KEEP": "",
      "ADD": "add-row",
      "REMOVE": "removed-row"
    }

    return TYPE_TO_STYLE[status]
