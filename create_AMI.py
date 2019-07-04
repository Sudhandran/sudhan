import sys
import boto3
ec2=boto3.client('ec2')

#Another way of create AMI
#response = ec2.create_image(Description='NewImage',DryRun=False,InstanceId='i-03e1bbdc66e3cd9fd',Name='AMI_Name',NoReboot=True)


# Create AMI
import boto3
ec2=boto3.client('ec2')

def Create_Image():
    response = ec2.create_image(
    BlockDeviceMappings=[
        {
            'DeviceName': '/dev/sda1',
            'Ebs': {
                'DeleteOnTermination': True,
                'Encrypted': False
            },
        },
    ],
    Description='NewImage',
    DryRun=False,
    InstanceId='i-03e1bbdc66e3cd9fd',
    Name='AMI_Name',
    NoReboot=True
)


def Deregister_AMI(Image_ID):
    response = ec2.deregister_image(ImageId=Image_ID)
    print(response)


Create_Image()
Deregister_AMI(sys.argv[1])
