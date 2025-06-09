from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Configuration)

admin.site.register(Measure)

admin.site.register(PerformanceMeasure)

admin.site.register(PerformanceMeasurement)

admin.site.register(Measurement)

admin.site.register(PropagationModel)

admin.site.register(PModelCatalog)

admin.site.register(PropagationParam)

admin.site.register(MobilityModel)

admin.site.register(MModelCatalog)

admin.site.register(MobilityParam)

admin.site.register(Network)

admin.site.register(Version)

admin.site.register(Node)

admin.site.register(Mobility)

#admin.site.register(Position)

admin.site.register(Station)

admin.site.register(Host)

admin.site.register(Switch)

admin.site.register(AccessPoint)

admin.site.register(Interface)

admin.site.register(Link)

admin.site.register(MayTalkTo)

#admin.site.register(MilitaryOrganization)

#admin.site.register(MilitaryOrganizationPowerType)

#admin.site.register(CommDeviceCarrier)

#admin.site.register(MilitaryPlatform)

#admin.site.register(MilitaryPerson)

#admin.site.register(MilitaryScenario)

admin.site.register(TestPlan)