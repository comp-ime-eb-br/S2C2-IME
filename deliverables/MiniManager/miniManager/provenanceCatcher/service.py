import xmlschema

class ProvenanceService():
    def __getResultContentFromRound(self, roundID, schema):
        from .models import Result
        try:
            result = Result.objects.get(round__pk=roundID)
            resultDict = xmlschema.XMLSchema(schema).decode(result.xml_content, attr_prefix='')

            radioFrequency = []
            performance = []
            if resultDict["radioFrequency"] and "instant" in resultDict["radioFrequency"]:
                radioFrequency = resultDict["radioFrequency"]["instant"]
            if resultDict["performance"] and "instance" in resultDict["performance"]:
                performance = resultDict["performance"]["instance"]

            return radioFrequency, performance

        except:
            return [], []

    def getResultRowsFromRound(self, roundID, schema, radioFrequencyMeasures):
        PERFORMANCE_KEYS = ["time", "source", "destination", "name", "value"]
        radioFrequencyObj, performanceObj = self.__getResultContentFromRound(roundID, schema)

        radioFrequency = []
        for resultInstance in radioFrequencyObj:
            for result in resultInstance["station"]:
                row = []
                for measure in radioFrequencyMeasures:
                    value = ""
                    if measure == "time":
                        value = resultInstance["time"]
                    elif measure in result:
                        value = result[measure]

                    row.append(value)
                
                radioFrequency.append({"value": row})
        radioFrequency.sort(key=lambda row:(int(row["value"][0]), row["value"][1]))
        
        performance = []
        for resultInstance in performanceObj:
            row = []
            for key in PERFORMANCE_KEYS:
                row.append(resultInstance[key])

            performance.append({"value": row})
        performance.sort(key=lambda row:(int(row["value"][0]), row["value"][1]))

        return radioFrequency, performance

    def getXML(self, roundID, encoding = True):
        from .models import Result
        result = Result.objects.get(round__pk=roundID)

        enc = ''
        if encoding:
            enc = '<?xml version="1.0" encoding="utf-8"?>'

        return enc + result.xml_content

    def __isGreaterThan(self, row1, row2):
        if int(row1[0]) == int(row2[0]):
            return row1[0] > row2[0]

        return int(row1[0]) > int(row2[0])

    def __isEqual(self, row1, row2):
        if int(row1[0]) == int(row2[0]):
            return row1[1] == row2[1]

        return False

    def __getDiff(self, rows1, rows2):
        len1 = len(rows1)
        len2 = len(rows2)

        index1 = 0
        index2 = 0

        diff = []
        while index1 < len1 and index2 < len2:
            if rows1[index1]["value"] == rows2[index2]["value"]:
                diff.append({"type": "KEEP", "value": rows1[index1]["value"]})
                index1 = index1 + 1
                index2 = index2 + 1
                continue

            if self.__isEqual(rows1[index1]["value"], rows2[index2]["value"]):
                diff.append({"type": "REMOVE", "value": rows1[index1]["value"]})
                diff.append({"type": "ADD", "value": rows2[index2]["value"]})
                index1 = index1 + 1
                index2 = index2 + 1
                continue

            if self.__isGreaterThan(rows1[index1]["value"], rows2[index2]["value"]):
                diff.append({"type": "ADD", "value": rows2[index2]["value"]})
                index2 = index2 + 1
                continue

            if self.__isGreaterThan(rows2[index2]["value"], rows1[index1]["value"]):
                diff.append({"type": "REMOVE", "value": rows1[index1]["value"]})
                index1 = index1 + 1
                continue

        while index1 < len1:
            diff.append({"type": "REMOVE", "value": rows1[index1]["value"]})
            index1 = index1 + 1

        while index2 < len2:
            diff.append({"type": "ADD", "value": rows2[index2]["value"]})
            index2 = index2 + 1

        return diff

    def diffResults(self, roundID1, roundID2, schema1, schema2, measurements):
        radioFrequency1, performance1 = self.getResultRowsFromRound(roundID1, schema1, measurements)
        radioFrequency2, performance2 = self.getResultRowsFromRound(roundID2, schema2, measurements)

        radioFrequencyDiff = self.__getDiff(radioFrequency1, radioFrequency2)
        performanceDiff = self.__getDiff(performance1, performance2)

        return radioFrequencyDiff, performanceDiff