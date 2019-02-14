# Code-to-Cloud
> ***Speed up software innovation from code to cloud***

This project was completed during the Insight DevOps program (New York, Jan 2019)

## Business Problem
How to streamline software development process by leveraging DevOps best practice and tools such as Jenkins, CI/CD? 

Our goal is to help IT automate test > build > deliver > deploy processes so that developer can focus on coding features. 

Business benefits include faster time-to-market speed, productivity gain and cost savings.

DevOps CI/CD Pipeline
----------------------
![alt text](https://github.com/wgong/code2cloud/blob/master/images/Wen_Gong-DevOps-CI-CD.jpg "Code2Cloud Pipeline")

## Project 

### Overview

I built upon an existing Insight project by a Data Engineering fellow:
* created integration test
* built Jenkins pipeline 
	- trigger on Git push
	- run test
	- alert by email when test fails
	- build docker image
	- publish to container registry
	- deploy app to cloud.

The Data Engineering project is an AWS Lambda app which processes IoT [traffic](https://github.com/arsegorov/insight-project) sensor data.

### Environment setup 
```
install Jenkins on AWS

install python 3.6 on Jenkins instance
        pip install virtualenv
        virtualenv -p /usr/local/bin/python3 py36 
        source py36/bin/activate
        pip3 install -r requirements.txt

AWS configuration
	CLI
	S3
		create bucket
		
	RDS - PostgreSQL
		create database

	Lambda
		in AWS console, create Lambda function
		
		run ./upload-lambda-xml.sh
		
		Lambda settings:
			Timeout=15 mins (max)
			Memory = 3GB
	
set env vars
	# after filling in S3 bucket name and database secrets in setu/aws_env_vars.sh
        source scripts/aws_env_vars.sh

create tables
	python3 scripts/create_tables_dynamoDB.py  
	python3 scripts/create_tables_postgreSQL.py
	
```

### Development
```
wrote scripts to create tables:
	scripts/create_tables_dynamoDB.py
	scripts/create_tables_postgreSQL.py
	
added new function extract_traffic_data so it is more robust to schema changes
	src/lambda_xml/lambda_function_xml.py

added 3 functions: log_msg, log_txn, new_txn to simplify logging
	src/lambda_xml/logs.py

created pyTest case for end-to-end integration test
	src/lambda_xml/test_lambda_function_xml.py

Jenkins pipeline
	Jenkinsfile

Docker build and publish
        Dockerfile
	
```

### How to run 

#### Continuous Integration (CI) pipeline

video walkthrough from git push to docker push (https://youtu.be/rKY6u4Z6AzM)

```
login to devopsgong@osboxes:
$ cd ~/GitHub/insight-project

$ vi README.md   # change anything

$ git status
$ git add .; git commit -m "demo CI"; git push

view Jenkins job log at http://jenkins.s8s.cloud/blue/organizations/jenkins/insight-project/activity

```

#### Continuous Delivery (CD) pipeline

video walkthrough from git push to service deployed in AWS (https://youtu.be/dxnUyEwXZhw)

```

login to devopsgong@osboxes:
$ cd ~/GitHub/hello-aws-docker

$ vi www/index.php   # change company name

$ git status
$ git add .; git commit -m "demo CD"; git push

view Jenkins job log at http://jenkins.s8s.cloud/blue/organizations/jenkins/hello-aws-docker-git/activity

view docker cloud homepage at http://hello.s8s.cloud/

```

#### Data Engineering (traffic-data) pipeline

video walkthrough (https://youtu.be/qpPLTKGVnkc)

```
$ git clone https://github.com/wgong/insight-project.git
$ cd insight-project
$ pip3 install -r requirements.txt

# retrieve traffic data
$ ./src/retrieve-realtime-data.sh &

# run dash
$ python3 src/data/app.py
```

### Operation

#### Jenkins
* use [Jenkins admin console](http://jenkins.s8s.cloud) to create/configure build pipeline

* monitor build jobs after git push


#### AWS Lambda
config lambda functions 			
* https://console.aws.amazon.com/lambda/home?region=us-east-1#/functions/preprocess_xml?tab=graph
	
#### AWS CloudWatch
view Lambda logs	
* https://console.aws.amazon.com/cloudwatch/home?region=us-east-1#logStream:group=/aws/lambda/preprocess_xml;streamFilter=typeLogStreamPrefix

#### AWS S3
monitor file uploads
* https://us-east-1.console.aws.amazon.com/s3/buckets/wengong
	
#### AWS DynamoDB
monitor processed traffic data
* https://console.aws.amazon.com/dynamodb/home?region=us-east-1#tables:selected=TrafficSpeed;tab=items
	
#### AWS IAM
manage resource permissions

#### SQL Workbench
monitor data processing and view logs

#### Dash
use [dashboard](dash.s8s.cloud) to monitor traffic data processing

#### AWS ECR
* https://console.aws.amazon.com/ecr/repositories/code2cloud/?region=us-east-1


#### AWS Load Balancer
* https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#LoadBalancers:sort=loadBalancerName

ELB Type: network

Target group: 
	ecs-cluster-target-group
	
Targets: 
* http://ec2-18-234-37-93.compute-1.amazonaws.com   (inst1)
* http://ec2-35-172-234-244.compute-1.amazonaws.com (inst2)

#### NameCheap.com
DNS Admin: REDIRECT DOMAIN
* hello.s8s.cloud => http://ecs-cluster-ad4b30d1387b520b.elb.us-east-1.amazonaws.com/
* jenkins.s8s.cloud => http://ec2-52-3-227-246.compute-1.amazonaws.com:8080/


#### Hello Docker
see deployed app 
* http://hello.s8s.cloud 


### Test

Below are 3 test scenarios. One can run them manually to verify project setup and/or further development.

#### Unit test

upload a single file

```
$ cd test
$ aws s3 cp sample_Trafficspeed.xml.gz s3://wengong/Traffic/test/Trafficspeed.xml.gz
```

#### Batch test

run a batch test

```
$ cd src
$ ./retrieve-realtime-data.sh
```
#### Integration/Regression test


```
$ cd src/lambda_xml
$ source ~/py36/bin/activate
$ pytest -q test_lambda_function_xml.py

```




### References

* [Use Jenkins](https://jenkins.io/doc/)
* [Get started with AWS CD](https://docs.aws.amazon.com/AWSGettingStartedContinuousDeliveryPipeline/latest/GettingStarted/ECS_CD_Pipeline.html)


### About Me
https://www.linkedin.com/in/wen-g-gong/
