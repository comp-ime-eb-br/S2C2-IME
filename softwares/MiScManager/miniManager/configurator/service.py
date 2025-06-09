class ConfiguratorService():

    def getVersionByID(self, versionID):
        from .models import Version
        version = Version.objects.get(id=versionID)
        return version
