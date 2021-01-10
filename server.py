from flask import Flask, request, jsonify # Imported flask for web.
import requests
import joblib
import numpy as np
#from tensorflow import keras



# Creating web app.
app = Flask(__name__, static_url_path="",static_folder="static")


# Added root route 

@app.route("/")
def index():
    print("hello world!")
    
    return app.send_static_file("index.html")

@app.route('/api/normal') 
def normal(): 
  return {"value": np.random.normal()}    




if __name__ == '__main__':
   app.run(debug = True)

