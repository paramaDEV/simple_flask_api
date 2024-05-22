from models.Studio import *

studioModel = StudioModel()
class StudioController :
    def displayStudio(id):
       return studioModel.displayStudio(id)
    
    def insertStudio(param):
        studioModel.insertStudio(param)

    def updateStudio(param):
        studioModel.updateStudio(param)