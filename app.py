import requests, json
from flask import Flask, render_template, request, redirect
import config


app = Flask(__name__)

@app.route("/")
def index():
    response0 = requests.get(config.url0)
    data0 = json.loads(response0.text)
    return render_template("index.html", data0=data0)

@app.route("/country", methods = ["GET", "POST"])
def country():
    if request.method == "GET":
        return render_template("country.html")
    else:
        cname = request.form.get("cname")
        if not cname:
            return redirect("/country")
        response1 = requests.get(config.url1+cname)
        data1 = json.loads(response1.text)
        if 'message' in data1:
            data1 = None
        if data1 == None:
            return redirect("/country")
        return render_template("country.html", data1=data1)

@app.route("/instates", methods = ["GET", "POST"])
def instates():
    if request.method == "GET":
        return render_template("instates.html")
    else:
        sname = request.form.get("sname")
        if not sname:
            return redirect("/instates")
        response3 = requests.get(config.url3)
        dt = json.loads(response3.text)
        dt1 = dt['data']['regional']
        f = 0
        for st in dt1:
            if st['loc'] == sname:
                data3 = st
                f = 1
        if not f:
            data3 = None
        if data3 == None:
            return redirect("/instates")
        return render_template("instates.html", data3=data3)

@app.route("/usstates", methods = ["GET", "POST"])
def usstates():
    if request.method == "GET":
        return render_template("usstates.html")
    else:
        sname = request.form.get("sname")
        if not sname:
            return redirect("/usstates")
        response2 = requests.get(config.url2+sname)
        data2 = json.loads(response2.text)
        if 'message' in data2:
            data2 = None
        if data2 == None:
            return redirect("/usstates")
        return render_template("usstates.html", data2=data2)