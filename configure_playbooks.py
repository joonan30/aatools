#!/usr/bin/env python

# set up the run
pem_key_location = ''
filename_inventory = '' # inventory file for playbook(s)
filename_worker = '' # playbook for worker

# create the list of ip addresses
fh = open('list_ec2_ips.txt').read().splitlines() # list of ip addresses for ec2 instances
match = []
for line in fh:
    ip = line.split('ec2-')[1].split('.compute')[0].replace('-','.')
    match.append(ip)

# create the inventory and playbook
file_inventory = open(,'w')
file_worker = open(filename_worker,'w')
file_worker.write('---'+'\n')

for ip, i in zip(match,range(len(match))):
    worker = 'worker' + str(i)
    # inventory
    line = '[' + worker + ']' + '\n'
    file_inventory.write(line)
    uid = 'uid=' + str(i)
    line = ' '.join([ip,'ansible_ssh_private_key_file=',pem_key_location,uid]) + '\n'
    file_inventory.write(line)
    # worker
    line = '- hosts: ' + worker + '\n'
    file_worker.write(line)
    line = '  ' + 'remote_user: ec2-user' + '\n'
    file_worker.write(line)
    file_worker.write('\n')
    line = '' # add your task line or code block
    file_worker.write(line)

file_inventory.close()
file_worker.close()
