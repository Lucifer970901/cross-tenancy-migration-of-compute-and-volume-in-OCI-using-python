This has a set of scripts which does the following.

The scripts for old tenancy do the following.

this includes create_image_push_to_bucket.py and create_object_PAR.py 

•	 List all the block volumes present in a compartment and create the block volume backup for each of the block volumes. Save the backup IDs to a file.

•	For each instance present in the compartment, create a custom image, and save the generated custom image OCID for later use.

•	Check if the object storage bucket exists, if not create a bucket and a Pre Authenticated Request for the bucket to export the custom image created.

•	Export the custom image to the bucket and create PAR for the objects created. And store it in a file.




The scripts for new tenancy do the following.

this includes import_image and backup.py

•	In the new tenancy you will be running this script, first it will read the file and the PAR created for each object, and import the image from the PAR access URI. And create the custom image.

•	Create the block volumes in the new tenancy from the backup created  in the old tenancy.
