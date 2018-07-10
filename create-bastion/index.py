from __future__ import print_function

import json
import urllib
import boto3
from botocore.exceptions import ClientError
import datetime
import os
import time
import re

bastion_cluster = os.environ['BASTION_CLUSTER']
subnet_string = os.environ['BASTION_SUBNETS']
subnet_array = subnet_string.split(',')
vpc = os.environ['BASTION_VPC']

def lambda_handler(event, context):
    user = event['queryStringParameters']['user']
    ip = event['requestContext']['identity']['sourceIp'] + "/32"
    ec2 = boto3.client('ec2')
    ecs = boto3.client('ecs')

    bastion_name = 'bastion-' + user

    # Create the security group
    sg_response = ec2.create_security_group(
        Description='Bastion access for ' + user,
        GroupName=bastion_name,
        VpcId=vpc
    )

    sg = sg_response['GroupId']

    # Add the ingress rule to it
    ec2.authorize_security_group_ingress(
        CidrIp=ip,
        FromPort=22,
        GroupId=sg,
        IpProtocol='tcp',
        ToPort=22
    )

    # Start the bastion container
    response = ecs.run_task(
        cluster=bastion_cluster,
        taskDefinition=bastion_name,
        count=1,
        startedBy='bastion-builder',
        launchType='FARGATE',
        networkConfiguration={
            'awsvpcConfiguration': {
                'subnets': subnet_array,
                'securityGroups': [sg],
                'assignPublicIp': 'ENABLED'
            }
        }
    )

    response = {}
    response['statusCode'] = 200
    response['body'] = 'Hello ' + user + " from " + ip
    return response
