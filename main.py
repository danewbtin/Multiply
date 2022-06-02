from cgitb import small
import re
import os
import requests
import json
from pandas import *


from flask import Flask, jsonify, render_template,request
from threading import Thread


app = Flask("Multipy")

def xl2dict(file:str)->dict:
    xls = ExcelFile(f"data/{file}.xlsx")
    df = xls.parse(xls.sheet_names[0])
    # with open("xt.txt","w") as f:
    #     f.write(json.dumps(df.to_dict(),indent=4))
    return df.to_dict()

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/getstarted")
def getstarted():
    if request.args.get("amount"):
            
        amount = int(request.args.get("amount"))
        if amount<25000:
            cap="small-cap"
        elif amount<100000:
            cap="mid-cap"
        else:
            cap="large-cap"
        data=xl2dict(cap)
        cap = cap.title().replace("-"," ")
        return render_template("results.html",len=len(data["Company Name"]),data=data,cap=cap)
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
