from flask import Flask, render_template, request, jsonify
from utils import Cellphone_Price
import numpy as np
import sklearn


app = Flask(__name__,template_folder="template")
@app.route('/')
def hello_flask():
    print("Welcome to Cellphone price Prediction")
    return render_template("home.html")

@app.route('/predict_price', methods = ['POST','GET'])
def predict_price():
    if request.method == "GET":
        # user_data = request.form
        print("We are using get method")
        Sale = eval(request.args.get("Sale"))
        weight = eval(request.args.get("weight"))
        resoloution = eval(request.args.get("resoloution"))
        ppi = eval(request.args.get("ppi"))
        cpu_core = eval(request.args.get("cpu_core"))
        cpu_freq = eval(request.args.get("cpu_freq"))
        internal_mem = eval(request.args.get("internal_mem"))
        ram = eval(request.args.get("ram"))
        RearCam = eval(request.args.get("RearCam"))
        Front_Cam = eval(request.args.get("Front_Cam"))
        battery = eval(request.args.get("battery"))
        thickness = eval(request.args.get("thickness"))

        print('Sale', 'weight', 'resoloution', 'ppi', 'cpu_core', 'cpu_freq',
                'internal_mem', 'ram', 'RearCam', 'Front_Cam', 'battery', 'thickness',
                Sale, weight,resoloution, ppi, cpu_core, cpu_freq,internal_mem, ram,
                RearCam, Front_Cam, battery, thickness)
        pc = Cellphone_Price(Sale, weight,resoloution, ppi, cpu_core, cpu_freq,internal_mem, ram,
                RearCam, Front_Cam, battery, thickness)
        price = pc.get_cellphone_pp()
        
        # return jsonify({"Message": f"Predicted House price is {price} $"})
        return render_template("home.html", price = price)

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5050)