#!/bin/bash


aws ec2 describe-instances --filters "Name=instance-state-name,Values=running" > aws_ec2_running_instances.json
