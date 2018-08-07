# coding: utf-8
import boto3
session = boto3.Session(profile_name='pyAuto')
s3 = session.resource('s3')
for bucket in s3.buckets.all():
    print(bucket)
    
ec2  = session.resource('ec2')
for instance in ec2.instances.all():
    print (instance.instance_id,instance.instance_type,instance.launch_time)
    
