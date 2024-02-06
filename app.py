Print(This is my second version)
'''
Full commands used in this video
To create a Docker Volume use the command
-----------------------------------------
docker volume create testvol1

docker volume ls

docker volume inspect testvol1

---------------------------------------
Mounting a Volume using -v or --mount
---------------------------------------
docker run -it --name=srv01 --mount source=testvol1,destination=/data centos

docker run -it --name srv04 -v testvol1:/data centos

docker run -it --volumes-from srv01 --name srv02 centos /bin/bash

---------------------------------------
Mounting a Host Directory as a Data volume 
---------------------------------------
mkdir files
cd files

touch file.txt

docker run -it –-name srv05 -v "$(pwd)":/data1 centos


docker volume rm [volume_name]
'''