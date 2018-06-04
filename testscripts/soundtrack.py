#!flask/bin/python

import sys
from flask import Flask, render_template, request, redirect, Response
import random, json

app = Flask(__name__)

@app.route("/")
def output():
    return "Welcome to tracks!"

if __name__ == "__main__":
    app.run()


