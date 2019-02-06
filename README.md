# Code2Cloud
> ***Speed up innovation from code to cloud***

This is a project I completed during the Insight DevOps program (New York, Jan 2019)

## Business Problem
How to streamline software development process by leveraging DevOps tool such as Jenkins? The goal is to help developer automate test > build > release process so that developer can focus on coding features. The benefits to business are faster time-to-market speed, productivity gain and cost savings.

DevOps CI/CD Pipeline
----------------------
![alt text](https://github.com/wgong/code2cloud/blob/master/images/Wen_Gong-DevOps-CI-CD.jpg "Code2Cloud Pipeline")

## Project 

### Overview

I took an existing project by Insight Data Engineering fellow:
* created integration test
* built Jenkins pipeline 
	1. trigger on Git push
	2. run test
	3. alert by email when test fails
	4. build docker image
	5. publish to container registry
	6. deploy app to cloud.

The Data Engineering project is an AWS Lambda app which processes IoT [traffic](https://github.com/arsegorov/insight-project) sensor data, its details can be found here (https://github.com/arsegorov/insight-project)

### Environment setup 
```
	Jenkins on AWS

	python
		requirements.txt

	AWS
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
		
	env vars
		add following export to .bashrc
			export AWS_S3_BUCKET=<your-S3-bucket-name>
			export AWS_PG_DB_HOST=<your-RDS-postgres-DB-hostname>
			export AWS_PG_DB_PORT=<your-RDS-postgres-DB-port>
			export AWS_PG_DB_NAME=traffic_db
			export AWS_PG_DB_USER=<db-user-name>
			export AWS_PG_DB_PASS=<db-user-password>
	
	tables
		setup/create_tables_dynamoDB.py  
		setup/create_tables_postgreSQL.py
		
	python 3.6 on Jenkins instance
```

### Development
```
	wrote scripts to create tables:
		setup/create_tables_dynamoDB.py
		setup/create_tables_postgreSQL.py
		
	added new function extract_traffic_data() so it is more robust to schema changes
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

* monitor build job when git push


#### AWS Lambda: config lambda function 			https://console.aws.amazon.com/lambda/home?region=us-east-1#/functions/preprocess_xml?tab=graph
	
#### AWS CloudWatch: view Lambda log	https://console.aws.amazon.com/cloudwatch/home?region=us-east-1#logStream:group=/aws/lambda/preprocess_xml;streamFilter=typeLogStreamPrefix

#### AWS S3: monitor file upload
	https://us-east-1.console.aws.amazon.com/s3/buckets/wengong
	
#### AWS DynamoDB : monitor processed traffic data
https://console.aws.amazon.com/dynamodb/home?region=us-east-1#tables:selected=TrafficSpeed;tab=items
	
#### AWS IAM: grant resource permission

#### SQL Workbench: monitor log

#### Dash
use [dashboard](dash.s8s.cloud) to monitor traffic data processing

#### Hello Docker
see deployed app at http://hello.s8s.cloud or http://hello2.s8s.cloud 
(ToDo : run load balanced or reverse proxy)

### Test

#### Unit test

upload a single file

```
$ aws s3 cp sample_Trafficspeed.xml s3://wengong/Traffic/test/Trafficspeed.xml
```

#### Batch test

run a batch test

```
	$ cd src
	$ ./retrieve-realtime-data.sh
```

### References


### About Me
https://www.linkedin.com/in/wen-gong-a890681/
