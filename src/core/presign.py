from src.core.s3_client import get_s3_client

def generate_presigned_url(config, operation, bucket, key):
    s3 = get_s3_client(config)

    return s3.generate_presigned_url(
        operation,
        Params={"Bucket": bucket, "Key": key},
        ExpiresIn=config["expiry"]
    )
    
def generate_upload_url(config, bucket, key):
    return generate_presigned_url(config, "put_object", bucket, key)

def generate_download_url(config, bucket, key):
    return generate_presigned_url(config, "get_object", bucket, key)

def generate_delete_url(config, bucket, key):
    return generate_presigned_url(config, "delete_object", bucket, key)