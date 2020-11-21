from aws_cdk import (
    core,
    aws_apigateway as apigateway,
    aws_lambda as lambda_,
    aws_sns as sns,
    aws_sqs as sqs,
    aws_sns_subscriptions as sns_subscriptions,
    aws_lambda_event_sources as event_sources,
    aws_iam as iam,
)


class EventsStack(core.Stack):
    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        person_topic = sns.Topic(self, "person topic", display_name="person-topic")
        person_queue = sqs.Queue(self, "person queue", queue_name="person-queue")

        person_topic.add_subscription(
            sns_subscriptions.SqsSubscription(person_queue, raw_message_delivery=True)
        )

        person_lambda = lambda_.Function(
            self,
            "person-lambda",
            code=lambda_.Code.asset("lambda"),
            runtime=lambda_.Runtime.PYTHON_3_8,
            handler="event.handler",
            function_name="person-lambda",
            memory_size=1024,
            timeout=core.Duration.seconds(10),
            tracing=lambda_.Tracing.ACTIVE,
            environment={"PERSON_SNS_TOPIC_ARN": person_topic.topic_arn},
        )

        person_lambda.add_to_role_policy(
            iam.PolicyStatement(
                actions=["sns:Publish"],
                effect=iam.Effect.ALLOW,
                resources=[person_topic.topic_arn],
            )
        )

        person_api = apigateway.LambdaRestApi(
            self,
            "person-api",
            handler=person_lambda,
            proxy=False,
            endpoint_configuration=apigateway.EndpointConfiguration(
                types=[apigateway.EndpointType.REGIONAL]
            ),
        )
        person_api_resource = person_api.root.add_resource("person")
        person_api_resource_method = person_api_resource.add_method(
            "POST",
            authorization_type=apigateway.AuthorizationType.NONE,
            api_key_required=True,
        )

        person_api_key = person_api.add_api_key("person-api-key")

        person_api_usage_plan = person_api.add_usage_plan(
            id="PER_API",
            name="PER_API",
            api_key=person_api_key,
            throttle=apigateway.ThrottleSettings(burst_limit=5, rate_limit=50),
        )

        person_api_stage = apigateway.Stage(
            self,
            id="qa",
            stage_name="qa",
            deployment=person_api.latest_deployment,
        )

        person_api_usage_plan.add_api_stage(
            stage=person_api_stage,
        )
