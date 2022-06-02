import re
import os
import requests
import json
from pandas import *


from flask import Flask, jsonify, render_template
from threading import Thread


app = Flask("Multipy")

def xl2dict()->dict:
    xls = ExcelFile("data/small-cap.xlsx")
    df = xls.parse(xls.sheet_names[0])
    # with open("xt.txt","w") as f:
    #     f.write(json.dumps(df.to_dict(),indent=4))
    return df.to_dict()

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/getstarted")
def getstarted():
    return render_template("getstarted.html")


@app.route("/disclaimer")
def disclaimer():

    return render_template("disclaimer.html")


@app.route("/toc")
def toc():
    return render_template("toc.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(port=os.getenv("PORT", default=5000),debug=True)
