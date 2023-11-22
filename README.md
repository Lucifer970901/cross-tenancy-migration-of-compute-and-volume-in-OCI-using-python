Simplify the Migration of Oracle Cloud Infrastructure compute and volume across tenancies using Python.

Migration of the compute resources and volume across tenancies can be quite a complicated task. But with the help of properly tested processes, you will be able to migrate your data safely with little downtime across tenancies. What if the data to be migrated is huge? Spanning across multiple VMs and in hundreds of block volumes, the whole process would get more challenging and even more complicated.

This document explains how the different tasks in the migration process can be simplified using Python while providing a brief on the process involved. Along with helping the customer who wants to move their data across tenancies and show how to:

•	Migrate the VMs and data to newer tenancies for operational and business reasons like different service providers.
•	Protecting the data from ransomware attacks
•	 Migrate the VMs across multiple customer tenancies.

In this case, the VMs are moved across 2 different tenancies as shown in the Architecture.
![Alt text](https://github.com/Lucifer970901/cross-tenancy-migration-of-compute-and-volume-in-OCI-using-python/blob/main/cross_tenancy_migration.png)
 

Prerequisites:
you need to have predefined policies to restore the backups across tenancies. These policies are controlled by OCI identity policies. The admit policy must be defined in the old tenancy and the endorse policy must be defined in the new tenancy.

Admit policy includes:
Define tenancy NewTenancy as <new_tenancy_ocid>
Define group NewTenancyIdentityGroup as <new_tenancy_group_ocid>
Admit group NewTenancyIdentityGroup of tenancy NewTenancy to read boot-volume-backups in tenancy
Admit group NewTenancyIdentityGroup of tenancy NewTenancy to read volume-backups in tenancy 

Endorse Policy includes:
Define tenancy OldTenancy as <old_tenancy_ocid>
Endorse group NewTenancyIdentityGroup to read boot-volume-backups in tenancy OldTenancy
Endorse group NewTenancyIdentityGroup to read volume-backups in tenancy OldTenancy
Endorse group NewTenancyIdentityGroup to inspect volumes in tenancy OldTenancy

Make sure to grant the permissions that are required for cross-migration activities and  delete the policies once the activity is completed.
for more information on policies used here: please review this document 

Recommended Hardware:
For the deployment of the Python code, you might have to create the instances in both tenancies. In this case, we are using Oracle Linux 8 operating system and with VM standard E4.Flex shape with 1 OCPU and 6GB memory. The script may require you to install pip3, pandas, and OCI-CLI for the code to work.
if you want to execute the script from the local machine, make sure all the Python packages and OCI-CLI are configured for 2 different tenancies.

Process:
Once the instance is running, you can SSH into the instance and install the required Python packages like pandas. You can import the script from the above repository. Make sure you have OCI-CLI configured prior you testing the script in the instance. The Python script covers the creation of the custom images and backups in the old tenancy as well as moving the custom images and volumes to the newer tenancy. These  two scripts need to be executed for two different tenancies. You can find the script on this GitHub page.


Here it shows the detailed workflow followed by each of the scripts.
 The script 1 (create_image_push_to_bucket.py)
•	For each instance present in the compartment, create a custom image, and save the generated custom image OCID for later use.
•	Check if the object storage bucket exists, if not create a bucket and a Pre Authenticated Request for the bucket to export the custom image created.
•	Export the custom image to the bucket and create PAR for the objects created. And store it in the file.
•	Create the backup for each of the block volumes present in the compartment.

The script 2 (create_object_PAR.py) 
creates the PAR URL for each of the objects created from the previous step.

The script 3 (import_image_backup.py).
•	In the new tenancy you will be running this script, first it will read the file and the PAR created for each object, and import the image from the PAR access URI. And create a custom image.
•	Create the block volumes in the new tenancy from the backup created  in the old tenancy.

Summary
I used this set of scripts to migrate a large volume of data and compute across multiple tenancies. It’s a great way to ease the complexities involved in migration with Python.

Hope this helps! Happy Learning!
Explore More
To learn more about migrating OCI compute and volume across tenancies, review these additional resources:
•	Best practices framework for Oracle Cloud Infrastructure
•	General Variables for All Requests
•	Configuring the CLI


![Uploading image.png…]()
