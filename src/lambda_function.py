import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info("Where in the World Is Carmen Sandiego?")
    return {
        'statusCode': 200,
        'body': "Hello world!"
    }