import xml.etree.ElementTree as ET
import xmlschema

class ProvenanceManager:

    __instance = None

    def __init__(self):
        self.__roundID = 0
        self.__schema = None
        #self.__resultsBuffer = []

        self.__radioFrequency = ET.Element("radioFrequency")
        self.__performance = ET.Element("performance")

    @classmethod
    def instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def reset(self, roundID, schema):
        self.__roundID = roundID
        self.__schema = schema

        #self.__resultsBuffer = []

        self.__radioFrequency = ET.Element("radioFrequency")
        self.__performance = ET.Element("performance")


    def addResult(self, content):
        #self.__resultsBuffer.append(content)
        if "radioFrequency" in content:
            self.__addRadioFrequencyElement(content["time"], content["radioFrequency"])

        if "performance" in content:
            self.__addPerformanceElement(content["time"], content["performance"])

    def __addRadioFrequencyElement(self, time, radioFrequency):
        instant = ET.Element("instant")
        instant.set('time', str(time))
        self.__radioFrequency.append(instant)

        for row in radioFrequency:
            station = ET.Element("station")
            station.set('name', row["name"])
            instant.append(station)

            for key in row:
                if key == "time" or key == "name":
                    continue

                element = ET.SubElement(station, key)
                element.text = str(row[key])

    def __addPerformanceElement(self, time, performance):
        instance = ET.Element("instance")
        instance.set('time', str(time))
        instance.set('source', str(performance["source"]))
        instance.set('destination', str(performance["destination"]))
        instance.set('name', str(performance["name"]))
        self.__performance.append(instance)

        value = ""
        for partialValue in performance["value"]:
            value = value + " " + partialValue

        element = ET.SubElement(instance, "value")
        element.text = str(value)


    def saveResults(self):
        from .models import Result #TODO: fix it

        root = ET.Element("result")
        root.set('roundID', str(self.__roundID))
        root.append(self.__radioFrequency)
        root.append(self.__performance)

        tree = ET.ElementTree(root)
        schema = xmlschema.XMLSchema(self.__schema)
        if not schema.is_valid(tree):
            return

        xml = ET.tostring(tree.getroot()).decode('utf-8')

        result = Result(round_id = self.__roundID, xml_content=xml)
        result.save()