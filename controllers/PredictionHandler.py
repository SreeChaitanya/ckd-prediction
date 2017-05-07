import json
from controllers.RestClass import RestClass
from bo.Prediction import BO_Prediction


class PredictionHandler(RestClass):
    def __init(self):
        self.name = 'PredictionHandler'
        self.bPrediction = BO_Prediction()

    def get(self):
        self.__init()
        self.write("Code block reached to Prediction Handler")
        print("Code @ " + self.name + " GET")

    def post(self):
        self.__init()
        print("Code @ " + self.name + " POST")
        global_params = json.loads(self.request.body)
        prediction_result = self.bPrediction.disease_prediction(global_params)
        print prediction_result
        self.write(str(prediction_result))