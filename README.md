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

python
	requirements.txt

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
	add following export to .bashrc
		export AWS_S3_BUCKET=<your-S3-bucket-name>
		export AWS_PG_DB_HOST=<your-RDS-postgres-DB-hostname>
		export AWS_PG_DB_PORT=<your-RDS-postgres-DB-port>
		export AWS_PG_DB_NAME=traffic_db
		export AWS_PG_DB_USER=<db-user-name>
		export AWS_PG_DB_PASS=<db-user-password>

create tables
	setup/create_tables_dynamoDB.py  
	setup/create_tables_postgreSQL.py
	
install python 3.6 on Jenkins instance
```

### Development
```
wrote scripts to create tables:
	setup/create_tables_dynamoDB.py
	setup/create_tables_postgreSQL.py
	
added new function extract_traffic_data so it is more robust to schema changes
	src/lambda_xml/lambda_function_xml.py

added 3 functions: log_msg, log_txn to simplify logging
	src/lambda_xml/logs.py

created pyTest case for end-to-end integration test
	src/lambda_xml/test_lambda_function_xml.py

Jenkins pipeline
	Jenkinsfile
	
Build script
	build-docker-deploy.sh
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
https://www.linkedin.com/in/wen-gong-a890681/
