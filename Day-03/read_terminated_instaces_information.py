import json
import subprocess


script_path ='/Users/niteshwayafalkar/Desktop/Coding/python/python_basics/Day-03/get_status_ec2_instance.sh'

result = subprocess.run(['bash', script_path], capture_output=True, text=True)

# Print the result
print("Exit Code:", result.returncode)
print("Script Output:", result.stdout)
print("Script Error (if any):", result.stderr)


with open('/Users/niteshwayafalkar/Desktop/Coding/python/python_basics/Day-03/aws_ec2_result.json', 'r') as file:
    #Load json data
    data = json.load(file)
    


print("Instance Id: ",data["Reservations"][0]["Instances"][0]["InstanceId"]) 
print("Key Name: ",data["Reservations"][0]["Instances"][0]["KeyName"]) 
print("Instance Status: ",data["Reservations"][0]["Instances"][0]["State"]["Name"]) 
   


    

