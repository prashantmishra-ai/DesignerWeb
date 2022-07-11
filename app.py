from flask import Flask, render_template,request
import json
import urllib.request
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
    if (request.method) == "GET":
        return render_template("index.html")
    elif (request.method) == "POST":
        data =  {
  "Inputs": {
    "WebServiceInput0": [
      {
        "symboling": request.form.get("symboling"),
        "normalized-losses": request.form.get("normalized-losses"),
        "make": request.form.get("make"),
        "fuel-type": request.form.get("fuel-type"),
        "aspiration": request.form.get("aspiration"),
        "num-of-doors": request.form.get("num-of-doors"),
        "body-style": request.form.get("body-style"),
        "drive-wheels": request.form.get("drive-wheels"),
        "engine-location": request.form.get("engine-location"),
        "wheel-base":request.form.get("wheel-base") ,
        "length": request.form.get("length"),
        "width": request.form.get("width"),
        "height": request.form.get("height"),
        "curb-weight": request.form.get("curb-weight"),
        "engine-type": request.form.get("engine-type"),
        "num-of-cylinders": request.form.get("num-of-cylinders"),
        "engine-size": request.form.get("engine-size"),
        "fuel-system": request.form.get("fuel-system"),
        "bore": request.form.get("bore"),
        "stroke": request.form.get("stroke"),
        "compression-ratio": request.form.get("compression-ratio"),
        "horsepower": request.form.get("horsepower"),
        "peak-rpm":request.form.get("peak-rpm") ,
        "city-mpg": request.form.get("city-mpg"),
        "highway-mpg": request.form.get("highway-mpg"),
        "price": 1.0
      }
    ]
  },
  "GlobalParameters": {}
}

        body = str.encode(json.dumps(data))

        url = 'http://72c5ee29-1dcd-4122-a9d3-33fe4a42dd9d.eastus.azurecontainer.io/score'
        api_key = 'FvvTD7r5wYnhuPycCBZ7ypVlJztSTFyT' # Replace this with the API key for the web service

        # The azureml-model-deployment header will force the request to go to a specific deployment.
        # Remove this header to have the request observe the endpoint traffic rules
        headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

        req = urllib.request.Request(url, body, headers)
        response = urllib.request.urlopen(req)
        result = response.read()
        dict_str = json.loads(result.decode("UTF-8"))
        my_data = dict_str
        output = my_data.get("Results").get("WebServiceOutput0")[0].get('Scored Labels')
        return render_template("index.html", output=output)