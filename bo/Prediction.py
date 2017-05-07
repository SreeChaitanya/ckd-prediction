# --- API Controllers ---
from bo.Base import BO_Base

# --- Logger ---
from logger import logger_error, logger_info, logger_warning


class BO_Prediction(BO_Base):

    def __init__(self):
        pass

    def disease_prediction(self, prediction_params):

        # ----> Machine Learning Code goes here
        logger_info("Code block at Disease Prediction fn.")
        logger_info("Parameters received : " + str(prediction_params))
        return True
