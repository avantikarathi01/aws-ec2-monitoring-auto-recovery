import boto3

ec2 = boto3.client("ec2")

INSTANCE_ID = "YOUR_INSTANCE_ID"

def lambda_handler(event, context):
    ec2.reboot_instances(
        InstanceIds=[INSTANCE_ID]
    )

    return {
        "statusCode": 200,
        "message": f"Reboot initiated for {INSTANCE_ID}"
    }
