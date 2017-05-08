# --- API Controllers ---
from bo.Base import BO_Base
import scipy
# --- Logger ---
from logger import logger_error, logger_info, logger_warning
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import pickle

class BO_Prediction(BO_Base):

    def __init__(self):
        pass

    def disease_prediction(self, prediction_params):

        # ----> Machine Learning Code goes here
        dataset = pd.Series(prediction_params)
        logger_info("Code block at Disease Prediction fn.")
        logger_info("Parameters received : " + str(prediction_params))
        rf = pickle.load(open('ckd_prediction_model.sav', 'rb'))
        Y_pred = rf.predict(dataset)

        return Y_pred[0]
