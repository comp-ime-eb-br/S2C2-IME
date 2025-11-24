from django.shortcuts import render
from django.core.files import File
from pathlib import Path
import re
import json
from datetime import datetime
import numpy as np
from time import process_time
import os


#------------------------------------------------------------------------
# 
#------------------------------------------------------------------------
def make_delivery_message(*args):

    background_message     = 'alert alert-danger'
    color_border_message   = 'border border-danger'
    weight_border_message  = 'border-2'
    highlight_text_message = 'success'
    
    return background_message,color_border_message,weight_border_message,highlight_text_message