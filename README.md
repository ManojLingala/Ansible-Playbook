
BOTO & ANSIBLE PLAYBOOK 

Overview

Step 1 : 

Boto libraries are adopted  for spinning up the 4 virtual machines over the AURIN and dynamically creating  the additional external storage of 60GB  , and attaching over to the created nodes '/dev/vdc'

RUN : Nectar.Py

Step 2 : 

Install Ansible Client and execute the below 

command-line parameter, :

ansible-playbook -i nodes.inventory -e “configure_cluster=True” Team27.yaml -u ubuntu --key-file cloud.key

As per the above we are defining the host inventory file which contains list of all the VM which were earlier created via Boto , and via the playbook we are installing { JVM,Python,CouchDB} and configuring the Cluster configurations of CouchDB as well as connecting to the bit bucket and releasing the binaries over the servers .

Step 3 :

Cluster setup : 

configure-cluster.Yaml is called from the main script to get configured all the nodes 

