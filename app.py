#!/usr/bin/env python3

from aws_cdk import core

from awscdk_python_workshop.awscdk_python_workshop_stack import AwscdkPythonWorkshopStack


app = core.App()
AwscdkPythonWorkshopStack(app, "awscdk-python-workshop", env={'region': 'us-west-2'})

app.synth()
