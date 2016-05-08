"""Scripts for CropKeeper Website Application."""
import os
from run import app, APP_ROOT


def getfeilds():
    path = '/'.join([APP_ROOT, 'static', 'feilds'])
    rawfeilds = os.listdir(path)
    feilds = [map(lambda x: x.replace("-", " "), feild.split("_")) for feild in rawfeilds]
    return feilds
