import json
import os

class FileFactory:
    def writeData(self,path,dataObject):
        jsonString = json.dumps(dataObject,default=lambda o: o.__dict__, indent=4)
        jsonFile = open(path, "w")
        jsonFile.write(jsonString)
        jsonFile.close()

    def readData(self,path,ClassName):
        if os.path.isfile(path) == False:
            return []
        file = open(path, "r", encoding="utf-8")
        jsonstring=file.read()
        ds = ClassName(**json.loads(jsonstring))
        file.close()
        return ds