from bo.Base import BO_Base


class BO_Prediction(BO_Base):

    def __init__(self):
        pass

    def disease_prediction(self, global_params):

        # ----> Machine Learning Code goes here
        print(global_params)
        print "Code block @ disease prediction fn."
        return True
