#!/bin/bash

# Nicolas Bonnand, 2018

# AWS security groups creation

tput setaf 6;echo 'Creating AWS security group dublin-demo-sg for region eu-west-1';tput setaf 7
aws ec2 --region eu-west-1 create-security-group --group-name dublin-demo-sg --description "Dublin demo sg"

tput setaf 6;echo 'Creating AWS security group paris-demo-sg for region eu-west-3';tput setaf 7
aws ec2 --region eu-west-3 create-security-group --group-name paris-demo-sg --description "Paris demo sg"


tput setaf 6;echo 'Adding ssh admin access in AWS dublin-demo-sg';tput setaf 7
aws ec2  --region eu-west-1 authorize-security-group-ingress --group-name dublin-demo-sg --ip-permissions '[{"ToPort": 22, "IpProtocol": "tcp", "FromPort":22, "IpRanges": [{"CidrIp":"0.0.0.0/0", "Description": "ssh admin"}]}]'

tput setaf 6;echo 'Adding ssh admin access in AWS paris-demo-sg';tput setaf 7
aws ec2  --region eu-west-3 authorize-security-group-ingress --group-name paris-demo-sg --ip-permissions '[{"ToPort": 22, "IpProtocol": "tcp", "FromPort":22, "IpRanges": [{"CidrIp":"0.0.0.0/0", "Description": "ssh admin"}]}]'



#AWS DUBLIN
tput setaf 6;echo 'Creating AWS instance dublinvm in region eu-west-1';tput setaf 7
aws ec2 --region eu-west-1 run-instances --image-id  ami-0773391ae604c49a4 --instance-type t2.micro --count 1 --key-name aws-dublin-keys --security-groups dublin-demo-sg --user-data file://install_ovs_docker_plotnetcfg.sh --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=dublinvm}]'

#AWS PARIS
tput setaf 6;echo 'Creating AWS instance parisvm in region eu-west-3';tput setaf 7
aws ec2 --region eu-west-3 run-instances --image-id  ami-075b44448d2276521 --instance-type t2.micro  --count 1 --key-name aws-paris-keys --security-groups paris-demo-sg --user-data file://install_ovs_docker_plotnetcfg.sh --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=parisvm}]'


# GCP Frankfurt
tput setaf 6;echo 'Creating GCP instance frankfurtvm in region europe-west3-b';tput setaf 7
gcloud compute instances create frankfurtvm --zone europe-west3-b --machine-type n1-standard-1 --description "FRANKFURT VM"  --image-project ubuntu-os-cloud --image-family ubuntu-minimal-1604-lts --tags=ovsdemo01 --metadata-from-file startup-script=install_ovs_docker_plotnetcfg.sh

# GCP London
tput setaf 6;echo 'Creating GCP instance londonvm in region europe-west3-b';tput setaf 7
gcloud compute instances create londonvm --zone europe-west2-b --machine-type n1-standard-1 --description "LONDON VM"  --image-project ubuntu-os-cloud --image-family ubuntu-minimal-1604-lts --tags=ovsdemo02 --metadata-from-file startup-script=install_ovs_docker_plotnetcfg.sh



tput setaf 6;echo "Querying dublinvm public ip";tput setaf 7
DUBLINVMIP=$(aws ec2 --region eu-west-1 describe-instances --query 'Reservations[].Instances[].PublicIpAddress' --filters "Name=tag:Name,Values=dublinvm" --output text)
tput setaf 6;echo "Querying dublinvm private ip";tput setaf 7
DUBLINVMPRIVIP=$(aws ec2 --region eu-west-1 describe-instances --query 'Reservations[].Instances[].PrivateIpAddress' --filters "Name=tag:Name,Values=dublinvm" --output text)


tput setaf 6;echo "Querying parisvm public ip";tput setaf 7
PARISVMIP=$(aws ec2 --region eu-west-3 describe-instances --query 'Reservations[].Instances[].PublicIpAddress' --filters "Name=tag:Name,Values=parisvm" --output text)
tput setaf 6;echo "Querying parisvm private ip";tput setaf 7
PARISVMPRIVIP=$(aws ec2 --region eu-west-3 describe-instances --query 'Reservations[].Instances[].PrivateIpAddress' --filters "Name=tag:Name,Values=parisvm" --output text)


tput setaf 6;echo "Querying frankfurtvm public ip";tput setaf 7
FRANKFURTVMIP=$(gcloud compute instances describe frankfurtvm --zone europe-west3-b --format='value(networkInterfaces[0].accessConfigs.natIP)')
tput setaf 6;echo "Querying frankfurtvm private ip";tput setaf 7
FRANKFURTVMPRIVIP=$(gcloud compute instances describe frankfurtvm --zone europe-west3-b --format='value(networkInterfaces[0].networkIP)')

tput setaf 6;echo "Querying londonvm public ip";tput setaf 7
LONDONVMIP=$(gcloud compute instances describe londonvm --zone europe-west2-b --format='value(networkInterfaces[0].accessConfigs.natIP)')
tput setaf 6;echo "Querying londonvm private ip";tput setaf 7
LONDONVMPRIVIP=$(gcloud compute instances describe londonvm --zone europe-west2-b --format='value(networkInterfaces[0].networkIP)')



tput setaf 6;echo 'Allowing ingress GRE in AWS dublin-demo-sg from parisvm';tput setaf 7
aws ec2  --region eu-west-1 authorize-security-group-ingress --group-name dublin-demo-sg --ip-permissions '[{"IpProtocol": "47", "IpRanges": [{"CidrIp":"'$PARISVMIP'/32", "Description": "GRE tunnel with LONDON"}]}]'

tput setaf 6;echo 'Allowing ingress GRE in AWS paris-demo-sg from dublinvm';tput setaf 7
aws ec2  --region eu-west-3 authorize-security-group-ingress --group-name paris-demo-sg --ip-permissions '[{"IpProtocol": "47", "IpRanges": [{"CidrIp":"'$DUBLINVMIP'/32", "Description": "GRE tunnel with DUBLIN"}]}]'


tput setaf 6;echo 'Allowing ingress Geneve in AWS paris-demo-sg from frankfurtvm';tput setaf 7
aws ec2  --region eu-west-3 authorize-security-group-ingress --group-name paris-demo-sg --ip-permissions '[{"ToPort": 6081, "IpProtocol": "udp", "FromPort":6081, "IpRanges": [{"CidrIp":"'$FRANKFURTVMIP'/32", "Description": "geneve tunnel with Frankfurt GCP"}]}]'

tput setaf 6;echo 'Allowing ingress Geneve in GCP firewall from parisvm';tput setaf 7
gcloud compute firewall-rules create genevetunneldemo --allow udp:6081 --direction=INGRESS --source-ranges=$PARISVMIP/32 --target-tags=ovsdemo01 --description='geneve tunnel with Paris'

tput setaf 6;echo 'Allowing ingress VXLAN in GCP firewall from londonvm';tput setaf 7
gcloud compute firewall-rules create vxlantunneldemo01 --allow udp:4789 --direction=INGRESS --source-ranges=$LONDONVMIP/32 --target-tags=ovsdemo01 --description='vxlan tunnel with London'

tput setaf 6;echo 'Allowing ingress VXLAN in GCP firewall from frankfurtvm';tput setaf 7
gcloud compute firewall-rules create vxlantunneldemo02 --allow udp:4789 --direction=INGRESS --source-ranges=$FRANKFURTVMIP/32 --target-tags=ovsdemo02 --description='vxlan tunnel with Frankfurt'


echo 
tput setaf 6;echo 'Cloud setup complete'
echo

echo 'VM       PRIV IP        PUB IP'
echo '------------------------------------------------'
echo "DUBLIN  $DUBLINVMPRIVIP    $DUBLINVMIP"
echo "PARIS  $PARISVMPRIVIP    $PARISVMIP"
echo "FRANKFURT  $FRANKFURTVMPRIVIP    $FRANKFURTVMIP"
echo "LONDON  $LONDONVMPRIVIP    $LONDONVMIP"
tput setaf 7





