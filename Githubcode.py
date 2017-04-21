from flask import Flask, render_template, request
import requests
import json
app=Flask(__name__)



@app.route('/map/background')

def map_background():

  return 'Map_Background'



@app.route('/map/heatmap')

def map_heatmap():

  return 'Map_Heatmap'



@app.route('/pollution/realtime')

def pollution_realtime():

 return 'Pollution_realtime'



@app.route('/route/detail')

def route_detail():

 return 'Route_Detail'




@app.route('/route/alternatives')

def route_alternatives():

 return 'Route_Alternatives'





if __name__ == '__main__':

        app.run(debug=True)
