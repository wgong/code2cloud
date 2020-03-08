API name = MaasDataCapture
endpoint type = Edge optimized
resource name = maas-sqs


[API proxy for SQS](https://medium.com/@pranaysankpal/aws-api-gateway-proxy-for-sqs-simple-queue-service-5b08fe18ce50)

Name:	MaasSQSLambda	
URL:	https://sqs.us-east-1.amazonaws.com/578247465916/MaasSQSLambda	
ARN:	arn:aws:sqs:us-east-1:578247465916:MaasSQSLambda
Default Visibility Timeout:	30 seconds
Message Retention Period:	4 days

IAM Role
use Policy SQSLambda

APIGatewaySqsRole
Role ARN = arn:aws:iam::578247465916:role/APIGatewaySqsRole

Test successful

