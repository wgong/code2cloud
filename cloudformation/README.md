# create stack via CloudFormation


## Sample 1 
https://apimeister.com/2017/08/24/integrate-api-gateway-with-kinesis-firehose-using-cloudformation.html

this was tested to be working


### S3 bucket: 
name: apigateway-firehose-databucket-h0qt5tcuqkh4

### Kinesis firehose
apigateway-firehose-EventFirehose-QPG6NOOCGWMB

#### test with demo data

API Gateway test body:
{
    "ticker_symbol": "SAC",
    "sector": "ENERGY",
    "change": 0.28,
    "price": 55.85
}

data found in S3 bucket:
{
    "apiKey": "test-invoke-api-key",
    "traceid": "",
    "body": {
        "ticker_symbol": "SAC",
        "sector": "ENERGY",
        "change": 0.28,
        "price": 55.85
    }
}

### api gateway:
name: apigateway-firehose-api		
ID: tqtg6eecwc
Invoke URL: https://tqtg6eecwc.execute-api.us-east-1.amazonaws.com/prod

### IAM roles:
apigateway-firehose-FirehoseRole-3088EWWBX5V8
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "s3:AbortMultipartUpload",
                "s3:GetBucketLocation",
                "s3:GetObject",
                "s3:ListBucket",
                "s3:ListBucketMultipartUploads",
                "s3:PutObject"
            ],
            "Resource": [
                "arn:aws:s3:::apigateway-firehose-databucket-h0qt5tcuqkh4",
                "arn:aws:s3:::apigateway-firehose-databucket-h0qt5tcuqkh4/*"
            ],
            "Effect": "Allow"
        }
    ]
}

apigateway-firehose-GatewayRole-NNYFE7CN4OPC
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "firehose:PutRecord"
            ],
            "Resource": "*",
            "Effect": "Allow"
        }
    ]
}


## Sample 2
completed SAM hello-world tutorial:
- https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started-hello-world.html

https://github.com/wg2g/serverless-data-pipeline-sam

## Ref: AWS Lambda Developer Guide
https://github.com/wg2g/aws-lambda-developer-guide
