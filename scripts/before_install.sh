# update os & install python3
sudo yum -y update
sudo amazon-linux-extras install -y python3
sudo yum -y install python3-devel python3-pip
pip3 install --user --upgrade virtualenv

# delete app
sudo rm -rf /home/ec2-user/CCD-Proj





