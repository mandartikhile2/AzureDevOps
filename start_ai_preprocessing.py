"""
File : start_ai_preprocessing.py
Description : Start AI Pre Processing service
Created on :
Author :
E-mail :
"""

import cv2
import numpy as np
from flask import Flask, Response

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def start_ai_preproc():
    """
    Response message for AI Pre Processing service testing
    """
    response_message = "STARTING AI PRE PROCESSING"
    return Response(response = response_message, status = 200, mimetype = "application/json")


if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 80) # Port is not finalized. Used just for testing.


