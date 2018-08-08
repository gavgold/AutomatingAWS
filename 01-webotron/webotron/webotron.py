
import boto3
import click

session = boto3.Session(profile_name='pyAuto')
s3 = session.resource('s3')
ec2  = session.resource('ec2')

@click.group()
def awsGroup():
    "Webotron is performs an number of AWS functions"
    pass

@awsGroup.command('list-buckets')
def list_buckets():
    "List all s3 buckets"
    for bucket in s3.buckets.all():
        print(bucket)

@awsGroup.command('list-bucket-objects')
@click.argument('bucket')
def list_bucket_objects(bucket):
    "List all objects in a s3 bucket"
    for object in s3.Bucket(bucket).objects.all():
        print(object)

@awsGroup.command('list-instances')
def list_instanctes():
    "List ec2 instances in the region"
    for instance in ec2.instances.all():
        print (instance.instance_id,instance.instance_type,instance.launch_time)

if __name__ == '__main__':
    awsGroup()
    