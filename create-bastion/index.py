from __future__ import print_function

import json
import urllib
import boto3
from botocore.exceptions import ClientError
import datetime
import os
import time
import re

def lambda_handler(event, context):
    response = {}
    response['statusCode'] = 200
    response['body'] = 'Hello Serverless Bastion!'
    return response
