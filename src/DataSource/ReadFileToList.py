from src.DataSource.RockConstants import RockConstants
class ReadFileToList:

    filePath = RockConstants.filePrefix + "log/"

    def getFileRows(self,fileName):
        file = open(self.filePath + fileName, "r")
        fileRows = file.read().splitlines()
        file.close()
        return fileRows

    def getList(self,fileName):
        fileRows = self.getFileRows(fileName)
        fileList = []
        for fileRow in fileRows:
            if len(fileRow) > 0:
                fileList.append(fileRow)
        return fileList
