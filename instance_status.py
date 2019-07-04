import boto3
import sys


Instance_ID=sys.argv[1]

'''      0 : pending
         16 : running
         32 : shutting-down
         48 : terminated
         64 : stopping
         80 : stopped'''

ec2=boto3.client('ec2')

desc_ins=ec2.describe_instances()
describe_out=desc_ins['Reservations'][0]['Instances'][0]['State']['Name']
print(describe_out)

def Start_Instance(Instance_ID):
    if describe_out=='stopped':
        ec2.start_instances(InstanceIds=[str(Instance_ID)])
        print("Instance ID: %s is Started"%Instance_ID)

def Stop_Instance(Instance_ID):
    if describe_out== 'running':
        ec2.stop_instances(InstanceIds=[str(Instance_ID)])
        print("Instance ID: %s has Stopped"%Instance_ID)
    else:
        print("Instance Status is %s" % describe_out)

def Reboot_Instance(Instance_ID):
    if describe_out == 'running':
        ec2.reboot_instances(InstanceIds=[str(Instance_ID)])
        print('Instance ID: %s is Rebooted' % Instance_ID)
    else:
        print("Instance Status is %s" % describe_out)

    def Terminate_Instance(Instance_ID):
        if describe_out == 'running' or describe_out == 'stopped':
            ec2.terminate_instances(InstanceIds=[str(Instance_ID)])
            print("Instance ID: %s is Terminated" % Instance_ID)
        else:
            print("Instance Status is %s" % describe_out)

        # def Stop_Instance():

    def Describe_instance(Instance_ID):
        desc_ins = ec2.describe_instances()
        desc_output = desc_ins['Reservations'][0]['Instances'][0]['State']['Code']
        print(desc_output)

        if desc_output == 80:
            print("Instance in Stopped status")
        elif desc_output == 64:
            print("Instance in Stopping status")
        elif desc_output == 48:
            print('Instance in Terminatted status')
        elif desc_output == 32:
            print("Instance is going to Shutting Down")
        elif desc_output == 16:
            print("Instance is in Running status")
        elif desc_output == 0:
            print("Instance in Pending Status")
        else:
            print("Unknown Status")



#Start_Instance(Instance_ID)
#Stop_Instance(Instance_ID)
#Reboot_Instance(Instance_ID)
#Terminate_Instance(Instance_ID)
#Describe_instance(Instance_ID)



'''    response = ec2.describe_instance_status()
    output=response['InstanceStatuses'][0]['InstanceState']['Code']
    print(output)'''
