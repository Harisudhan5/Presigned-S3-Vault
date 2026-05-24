import boto3

def get_s3_client(config):
    return boto3.client(
        "s3",
        aws_access_key_id=config["aws_access_key"],
        aws_secret_access_key=config["aws_secret_key"],
        region_name=config["region"]
    )