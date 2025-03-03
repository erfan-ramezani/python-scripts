# Python Scripts for Various Tasks

This repository contains a collection of Python scripts that I have developed to automate and solve various tasks, including data analysis and more.

# Suggestions for Improving the Scripts

If you have any suggestions for improving the scripts or have any questions, feel free to message me on LinkedIn:

[Link to my LinkedIn profile](https://www.linkedin.com/in/erfanramezani)


## How to Use search_Host_zabbix.py
Extracting hostnames, IP, etc. based on tags in Zabbix
You must give it the Zabbix URL and token at the entrance




### KubeVirt Configuration Explained
This configuration file creates a simple Virtual Machine (VM) using KubeVirt, a powerful tool that allows you to manage VMs directly within Kubernetes.
Configuration Explanation:
apiVersion and kind: Specifies that we are using the KubeVirt API, and the type of object we are creating is a VirtualMachine.
metadata: Defines the name of our VM (my-first-vm).
spec: Indicates that the VM should start running immediately after creation.
template: Sets the labels and specifications for the VM.
domain: Configures the disks and resources (such as RAM) for the VM.
volumes: Specifies the operating system image and initial configuration (like setting a password) for the VM.
With this configuration, you’ve created a VM with the Fedora operating system that’s ready to use! 🖥️
