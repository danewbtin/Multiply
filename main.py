import re
import os
import requests
import json


from flask import Flask, jsonify, render_template
from threading import Thread


app = Flask("Multipy")



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
    app.run(port=os.getenv("PORT", default=5000))