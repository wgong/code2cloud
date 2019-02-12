
# coding: utf-8

# http://www.postgresqltutorial.com/postgresql-python/create-tables/

# ### Create table in AWS RDS/Postgres

# In[1]:


import psycopg2
import os


# In[13]:


db_host = os.environ.get('AWS_PG_DB_HOST')
db_name = os.environ.get('AWS_PG_DB_NAME')
db_user = os.environ.get('AWS_PG_DB_USER')
password = os.environ.get('AWS_PG_DB_PASS')

db_connection_string = f"dbname='{db_name}' user='{db_user}' host='{db_host}' password='{password}'"

connection = psycopg2.connect(db_connection_string)


# ### create table = 'xml_schemas'
# 
# this table stores XML schema

# In[10]:


#
# The table for storing known schemas
#

xml_table_name = 'xml_schemas'
file_pattern_field, file_pattern_props = 'file_pattern', 'text'
schema_time_field, schema_time_props = 'schema_datetime_utc', 'timestamp without time zone'
schema_desc_field, schema_desc_props = 'schema_description', 'text'
proc_schema_field, proc_schema_props = 'processing_schema', 'json NOT NULL'
xml_schemas_pk = f'{file_pattern_field}, {schema_time_field}'


def create_schemas_meta_table(connection):
    """
    Creates a meta info table for storing known schemas.

    :param connection: a connection to the database
    """
    cur = connection.cursor()
    cur.execute(f"CREATE TABLE IF NOT EXISTS {xml_table_name} ("
                f"{file_pattern_field} {file_pattern_props},"
                f"{schema_time_field} {schema_time_props},"
                f"{schema_desc_field} {schema_desc_props},"
                f"{proc_schema_field} {proc_schema_props},"
                f"PRIMARY KEY ({xml_schemas_pk}));")

    connection.commit()

create_schemas_meta_table(connection)

# verify
cur = connection.cursor()
cur.execute(f"select count(*) from {xml_table_name};")
rows = cur.fetchall()
print("Found # rows", rows[0][0])
cur.close()


# ### create table = 'xml_log'
# 
# this table stores detailed log 

# In[11]:


xml_table_name = 'xml_log'
time_field, time_props = 'date_time_utc', 'timestamp without time zone'
file_field, file_props = 'file', 'text'
status_field, status_props = 'status', 'smallint'  # possible values: succeeded, failed, processing, other = -1
msgs_field, msgs_props = 'messages', 'text[] NOT NULL'
xml_log_pk = f'{time_field}'


def create_xml_log_table(connection):
    cur = connection.cursor()
    cur.execute(
        f"CREATE TABLE IF NOT EXISTS {xml_table_name} ("
        f"{time_field} {time_props},"
        f"{file_field} {file_props},"
        f"{status_field} {status_props},"
        f"{msgs_field} {msgs_props},"
        f"PRIMARY KEY ({xml_log_pk}));")

    connection.commit()

create_xml_log_table(connection)

# verify
cur = connection.cursor()
cur.execute(f"select count(*) from {xml_table_name};")
rows = cur.fetchall()
print("Found # rows", rows[0][0])
cur.close()


# ### create table = 'xml_txns'
# 
# this table stores data processing per file

# In[14]:


xml_table_name = "xml_txns"

def create_xml_txns_table(connection, table_name):
    cur = connection.cursor()
    
    cur.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
          id              SERIAL PRIMARY KEY,
          filename        varchar(100) NOT NULL,
          begin_datetime  timestamp,
          end_datetime    timestamp,
          num_locations   int default 0,
          status          SMALLINT  default 2,  /* 0 - success, 1 - failed, 2 - processing */
          msg             VARCHAR(1000)
        );
    """)

    connection.commit()

create_xml_txns_table(connection, xml_table_name)


# In[20]:


# create unique index
xml_table_name = "xml_txns"
xml_table_index_name = "xml_txns_n1"
xml_table_idx_col_name = "filename"

def create_xml_txns_index(connection, table_name, index_name, idx_col_name):
    cur = connection.cursor()
    
    cur.execute(f"""
        CREATE UNIQUE INDEX IF NOT EXISTS {index_name} ON {table_name}({idx_col_name});
    """)

    connection.commit()

create_xml_txns_index(connection, xml_table_name,xml_table_index_name,xml_table_idx_col_name)


# In[22]:


# verify
cur = connection.cursor()
cur.execute(f"select count(*) from {xml_table_name};")
rows = cur.fetchall()
print("Found # rows", rows[0][0])
cur.close()


# In[17]:


# close connection
connection.close()

