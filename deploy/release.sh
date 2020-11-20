aws_access_key=$1
aws_secret_key=$2
aws_region=$3

#Set env vars
export AWS_ACCESS_KEY_ID=aws_access_key
export AWS_SECRET_ACCESS_KEY=aws_secret_key
export AWS_DEFAULT_REGION=aws_region

# Install required dependencies
npm install aws-cdk
pip3 install setuptools
pip3 install -r requirements.txt

#Synthesize an AWS CloudFormation template
node_modules/aws-cdk/bin/cdk synth

#Deploy
node_modules/aws-cdk/bin/cdk deploy