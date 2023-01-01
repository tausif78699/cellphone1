import pandas as pd
import numpy as np
import pickle
import json

import sklearn

class Cellphone_Price():

    def __init__(self,Sale, weight, resoloution, ppi, cpu_core, cpu_freq,
                internal_mem, ram, RearCam, Front_Cam, battery, thickness):
        print("INIT FUNCTION")
        self.Sale = Sale
        self.weight =  weight
        self.resoloution = resoloution
        self.ppi = ppi
        self.cpu_core = cpu_core
        self.cpu_freq = cpu_freq
        self.internal_mem =  internal_mem
        self.ram = ram
        self.RearCam = RearCam
        self.Front_Cam = Front_Cam
        self.battery = battery
        self.thickness =  thickness
        

    def load_saved_data(self):
        with open("lin_reg.pkl", 'rb') as f:
            self.model = pickle.load(f)

        with open("Cellphone_data.json", 'r') as f:
            self.cellphone_price_pred = json.load(f)

    def get_cellphone_pp(self):
        self.load_saved_data()

        # col_list = x.columns

        test = np.zeros(self.model.n_features_in_, int)
        test[0] = self.Sale
        test[1] = self.weight
        test[2] = self.resoloution
        test[3] = self.ppi
        test[4] = self.cpu_core
        test[5] = self.cpu_freq
        test[6] = self.internal_mem
        test[7] = self.ram
        test[8] = self.RearCam
        test[9] = self.Front_Cam
        test[10] = self.battery
        test[11] = self.thickness

        price1 = np.around(self.model.predict([test])[0] , 2)
        print(f"Predicted Cellphone price in dollar is : {price1} $")    
        return price1
    
if __name__ == "__main__":
    cell = Cellphone_Price()
    cell
