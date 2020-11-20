# Install required dependencies
npm install aws-cdk
pip3 install setuptools
pip3 install -r requirements.txt

node_modules/aws-cdk/bin/cdk bootstrap

#Synthesize an AWS CloudFormation template
node_modules/aws-cdk/bin/cdk synth

#Deploy
node_modules/aws-cdk/bin/cdk deploy  --require-approval never