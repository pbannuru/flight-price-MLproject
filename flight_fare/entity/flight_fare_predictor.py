import os
import sys

from flight_fare.exception import flight_fareException
from flight_fare.util.util import load_object

import pandas as pd


class flight_fareData:

    def __init__(self,
                 longitude: float,
                 latitude: float,
                 flight_fare_median_age: float,
                 total_rooms: float,
                 total_bedrooms: float,
                 population: float,
                 households: float,
                 median_income: float,
                 ocean_proximity: str,
                 median_house_value: float = None
                 ):
        try:
            self.longitude = longitude
            self.latitude = latitude
            self.flight_fare_median_age = flight_fare_median_age
            self.total_rooms = total_rooms
            self.total_bedrooms = total_bedrooms
            self.population = population
            self.households = households
            self.median_income = median_income
            self.ocean_proximity = ocean_proximity
            self.median_house_value = median_house_value
        except Exception as e:
            raise flight_fareException(e, sys) from e

    def get_flight_fare_input_data_frame(self):

        try:
            flight_fare_input_dict = self.get_flight_fare_data_as_dict()
            return pd.DataFrame(flight_fare_input_dict)
        except Exception as e:
            raise flight_fareException(e, sys) from e

    def get_flight_fare_data_as_dict(self):
        try:
            input_data = {
                "longitude": [self.longitude],
                "latitude": [self.latitude],
                "flight_fare_median_age": [self.flight_fare_median_age],
                "total_rooms": [self.total_rooms],
                "total_bedrooms": [self.total_bedrooms],
                "population": [self.population],
                "households": [self.households],
                "median_income": [self.median_income],
                "ocean_proximity": [self.ocean_proximity]}
            return input_data
        except Exception as e:
            raise flight_fareException(e, sys)


class flight_farePredictor:

    def __init__(self, model_dir: str):
        try:
            self.model_dir = model_dir
        except Exception as e:
            raise flight_fareException(e, sys) from e

    def get_latest_model_path(self):
        try:
            folder_name = list(map(int, os.listdir(self.model_dir)))
            latest_model_dir = os.path.join(self.model_dir, f"{max(folder_name)}")
            file_name = os.listdir(latest_model_dir)[0]
            latest_model_path = os.path.join(latest_model_dir, file_name)
            return latest_model_path
        except Exception as e:
            raise flight_fareException(e, sys) from e

    def predict(self, X):
        try:
            model_path = self.get_latest_model_path()
            model = load_object(file_path=model_path)
            median_house_value = model.predict(X)
            return median_house_value
        except Exception as e:
            raise flight_fareException(e, sys) from e