#import libraries
import json
import subprocess
import time


#AWS CLI script to launch EC2 instances
launch_script='aws ec2 run-instances --image-id ami-03f4878755434977f --count 1 --instance-type t2.micro --key-name aws-login.pem --security-group-ids sg-02d75e48b0bfa150d --subnet-id subnet-06c867bcca503534a'
status_script='aws ec2 describe-instances --filters "Name=instance-state-name,Values=running" > aws_ec2_running_instances.json'

#Execute script to launch ec2 instance
def execute_aws_instances_launch_script():
    global launch_script
    print("GET LAUNCH SCRIPT:  ", script)
    result = subprocess.run(['bash'], input=script, capture_output=True, text=True)
    print("Script executed....",)
    # Print the result
    print("Exit Code:", result.returncode)
    print("Script Output:", result.stdout)
    print("Script Error (if any):", result.stderr)




def get_the_instance_status():
    global status_script
    print("GET STATUS SCRIPT:  ",status_script)
    result = subprocess.run(['bash'], input=script, capture_output=True, text=True)
    print("Script executed....")
    # Print the result
    print("Exit Code:", result.returncode)
    print("Script Output:", result.stdout)
    print("Script Error (if any):", result.stderr)

    instance_status=data["Reservations"][0]["Instances"][index]["State"]["Name"] 
    t_end = time.time() + 60 * 15
    while time.time() < t_end:
        if "running" == instance_status:
            print("Instance Lanuched with status: ", instance_status)
        else:
            print("Instance is being launched...",instance_status)



execute_aws_instances_launch_script()

get_the_instance_status()