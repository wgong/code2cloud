
# coding: utf-8

# [Python and DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.html)

# ### Create a table in AWS DynamoDB

# In[5]:


import boto3
# Get the service resource.
dynamodb = boto3.resource('dynamodb')


# In[6]:


dyn_table_name="TrafficSpeed"
dyn_field_name_site="measurementSiteReference"
dyn_field_name_time="measurementTimeDefault"


# In[7]:


try:
    # Create the DynamoDB table.
    table = dynamodb.create_table(
        TableName="{}".format(dyn_table_name),
        KeySchema=[
            {
                'AttributeName': "{}".format(dyn_field_name_site),
                'KeyType': 'HASH'
            },
            {
                'AttributeName': "{}".format(dyn_field_name_time),
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': "{}".format(dyn_field_name_site),
                'AttributeType': 'S'
            },
            {
                'AttributeName': "{}".format(dyn_field_name_time),
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    
    # Wait until the table exists.
    table.meta.client.get_waiter('table_exists').wait(TableName="{}".format(dyn_table_name))

    # Print out some data about the table.
    print(table.item_count)
    print("Table created at:", table.creation_date_time)
    print("Table status:", table.table_status)

except Exception as e:
    if "Table already exists" in str(e):
        print("Table already exists")
    else:
        raise e

