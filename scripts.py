"""Scripts for CropKeeper Website Application."""
import os
from run import app, APP_ROOT


def getfields():
    path = '/'.join([APP_ROOT, 'static', 'feilds'])
    rawfeilds = os.listdir(path)
    feilds = [map(lambda x: x.replace("-", " "), feild.split("_")) for feild in feilds]
    return feilds
