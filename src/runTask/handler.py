import boto3
import os

client = boto3.client('ecs')

def handler(event, context):
    print(event)

    params = {
        'launchType': 'FARGATE',
        'count': 1,
        'taskDefinition': os.environ['DOCKER_TASK_ARN'],
        'networkConfiguration': {
            'awsvpcConfiguration': {
                'subnets': os.environ['DOCKER_TASK_SUBNETS'].split(','),
                'assignPublicIp': 'ENABLED'          
            }
        }
    }

    response = client.run_task(**params)
    return str(response)