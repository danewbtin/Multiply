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


if __name__ == "__main__":
    app.run(port=os.getenv("PORT", default=5000))
