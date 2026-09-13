import boto3

def upload_to_cloud(config):
    s3_cfg = config["aws_s3"]
    s3 = boto3.client(
        "s3",
        region_name=s3_cfg["region"]
    )
    
    s3.upload_file(
        config["local_output_path"],
        s3_cfg["bucket_name"],
        "saved_credentials.txt"
    )
