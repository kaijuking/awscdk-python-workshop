import json
import pytest

from aws_cdk import core
from awscdk-python-workshop.awscdk_python_workshop_stack import AwscdkPythonWorkshopStack


def get_template():
    app = core.App()
    AwscdkPythonWorkshopStack(app, "awscdk-python-workshop")
    return json.dumps(app.synth().get_stack("awscdk-python-workshop").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
