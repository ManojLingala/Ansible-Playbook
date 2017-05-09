import boto
from boto.ec2.connection import EC2Connection
from boto.ec2.regioninfo import *

#Author : Manoj Kumar Reddy Lingala (886517)
#Access and Secret Key are specific to team cc27

region = RegionInfo(name="NeCTAR", endpoint="nova.rc.nectar.org.au")
connection = boto.connect_ec2(aws_access_key_id="616e0108b1bb4692aaded11e4675372b",
                    aws_secret_access_key="6a691b057ae34c2f8bfd9006f748587e",
                    is_secure=True,
                    region=region,
                    validate_certs=False,
                    port=8773,
                    path="/services/Cloud")

i = 0 # Initializing the instances creation
while i < 4: # Creating 4 nodes

    # Creating a  Small instance VM with access key of CCteam27 with
    # Image of (ami-fe917e46) specify NeCTAR Ubuntu 16.04 LTS (Xenial) amd64 (pre-installed murano-agent) and customized security group

    instance = connection.run_instances('ami-fe917e46', key_name='CCTeam27', instance_type='m1.small',
                                        security_groups=['default'])

    #Requesting a Volume of 60GB from NCI Availability Zone as default instances are created in Canberra
    #Snapshots are not required at this stage '' .

    vol_req = connection.create_volume(60,'NCI','','melbourne')

    #Attaching a Volume of 60GB to the created instance
    connection.attach_volume(vol_req.id,instance.id,'/dev/vdc')

    i = i + 1


