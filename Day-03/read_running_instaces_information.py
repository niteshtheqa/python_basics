import json
import subprocess


script_path = '/Users/niteshwayafalkar/Desktop/Coding/python/python_basics/Day-03/get_ec2_status_running.sh'

all_id = ' '
script = ' '
result = subprocess.run(['bash', script_path], capture_output=True, text=True)

# Print the result
print("Exit Code:", result.returncode)
print("Script Output:", result.stdout)
print("Script Error (if any):", result.stderr)


with open('/Users/niteshwayafalkar/Desktop/Coding/python/python_basics/Day-03/aws_ec2_running_instances.json', 'r') as file:
    # Load json data
    data = json.load(file)


print(len(data["Reservations"][0]["Instances"]))


def print_all_instances_data():
    for index in range(len(data["Reservations"][0]["Instances"])):
        print(index, "  INFORMATION")
        print("Key Name: ", data["Reservations"]
              [0]["Instances"][index]["KeyName"])
        print("Public Address: ", data["Reservations"]
              [0]["Instances"][index]["PublicIpAddress"])
        print("Private Dns Name: ", data["Reservations"]
              [0]["Instances"][index]["PrivateDnsName"])
        print("Instance Status: ", data["Reservations"]
              [0]["Instances"][index]["State"]["Name"])
        print("---------------------------------------------------------------------------------\n\n\n\n\n\n\n")


def read_instance_ids():
    global all_id
    for index in range(len(data["Reservations"][0]["Instances"])):
        all_id += " "+data["Reservations"][0]["Instances"][index]["InstanceId"]
    print("All ID's: ", all_id)


def generate_terminate_script():
    global script
    script = "aws ec2 terminate-instances --instance-ids"+all_id


def execute_aws_instances_terminate_script():
    print("Script:  ", script)
    terminate_script = subprocess.run(['bash'], input=script, capture_output=True, text=True)
    print("Script executed....",)
    # Print the result
    print("Exit Code:", terminate_script.returncode)
    print("Script Output:", terminate_script.stdout)
    print("Script Error (if any):", terminate_script.stderr)
# print("Instance Id: ",data["Reservations"][0]["Instances"][0]["InstanceId"])
# print("Key Name: ",data["Reservations"][0]["Instances"][0]["KeyName"])

# print("Public Address: ",data["Reservations"][0]["Instances"][0]["PublicIpAddress"])

# print("Private Dns Name: ",data["Reservations"][0]["Instances"][0]["PrivateDnsName"])


# print("Instance Status: ",data["Reservations"][0]["Instances"][0]["State"]["Name"])


print_all_instances_data()

read_instance_ids()
generate_terminate_script()
execute_aws_instances_terminate_script()
