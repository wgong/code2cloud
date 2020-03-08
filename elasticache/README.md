
https://github.com/aws-samples/amazon-elasticache-samples

https://realpython.com/python-redis/

Lambda and Elasticache has to be in the same VPC

[Tutorial: Configuring a Lambda Function to Access Amazon ElastiCache in an Amazon VPC](https://docs.aws.amazon.com/lambda/latest/dg/services-elasticache-tutorial.html)

create a redis cache
name = maas-redis
version=5.0.6
port=6379
node-type=cache.t2.micro 0.5GB
No. replica=0

vpc ID = vpc-f13d148b
subnet group = maas-redis-sg

add policy = AWSLambdaVPCAccessExecutionRole
to role = MaasSQSLambdaRole

Write down the configuration endpoint for the cache cluster that you launched
Endpoint = maas-redis.1qremv.0001.use1.cache.amazonaws.com