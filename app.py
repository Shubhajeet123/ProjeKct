import boto3
ec2_client = boto3.client('ec2',region_name= 'us-east-1')

#EC2 Lunch
response = ec2_client.run_instances(
    ImageId='ami-06b21ccaeff8cd686',
    InstanceType='t2.micro',
    KeyName='DevOps-AWS',
    MaxCount=1,
    MinCount=1
)
