# aatools

Recipes for [Ansible](https://www.ansible.com/) on [Amazon Web Services (AWS)](https://aws.amazon.com/). This repo provides some examples of Ansible playbooks configured on AWS environment.


1. Initiate AWS instance(s) and copying data from S3 to instance(s)
2. Set up the inventory for playbook subjects. 
3. A script to configure a playbook and inventory file for run.


## Aims

- ~10k jobs with decent i/o size and single core can be done in t2 series and light AMI from AWS (only 8Gb per instance).

## References:

http://docs.ansible.com/ansible/guide_aws.html

