from aws_cdk import (
    core,
    aws_lambda as _lambda,
    aws_apigateway as apigw
)

from hitcounter import HitCounter


class AwscdkPythonWorkshopStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Define an AWS Lambda resource
        my_lambda = _lambda.Function(
            self, 'HelloHandler',
            runtime = _lambda.Runtime.PYTHON_3_8,
            code = _lambda.Code.asset('lambda'),
            handler = 'hello.handler'
        )

        hello_with_counter = HitCounter(
            self, 'HelloHitCounter',
            downstream = my_lambda
        )

        # API Gateway
        apigw.LambdaRestApi(
            self, 'Endpoint',
            handler=hello_with_counter.handler
        )
