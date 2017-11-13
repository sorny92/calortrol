import time
from flask import Flask, render_template, request
from servo import *
#Initialize Flask webapp
heaterControl = HeaterController()
switch_on_times = []
heating_ON = False
app = Flask(__name__)
@app.route("/")
def index():
    print (heating_ON)
    print (switch_on_times)
    return render_template('index.html', heating_ON=heating_ON, times=switch_on_times)

@app.route("/switchOn")
def switchOn():
    heating_ON=True
    print (heating_ON)
    print (switch_on_times)
    return render_template('index.html', heating_ON=heating_ON, times=switch_on_times)

@app.route("/switchOff")
def switchOff():
    heating_ON=False
    print (heating_ON)
    print (switch_on_times)
    return render_template('index.html', heating_ON=heating_ON, times=switch_on_times)

@app.route("/save_time")
def save_time():
    projectpath = request.form
    print (projectpath)
    switch_on_times.append("date")
    print (heating_ON)
    print (switch_on_times)
    return render_template('index.html', heating_ON=heating_ON, times=switch_on_times)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1992)