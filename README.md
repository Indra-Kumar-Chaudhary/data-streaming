1. First Create all required volume folders
    mkdir volumes
    cd volumes
    mkdir kafka-data
    mkdir kafka-connect-data 

2. Create folder in docker-compose.yml directory 
    mkdir confluent-hub-components 

3. Create volume folders for Flink 
    mkdir flink-volumes
    cd flink-voumes 
    mkdir settings

5. Create directory for rawdata 
    mkdir filesystem


<h1> Debezium SQL Server Source Connector </h1>
    <b>1. Install the SQL Server Connector </b>
        <p> confluent-hub install --no-prompt debezium/debezium-connector-sqlserver:latest </p>

    <b>2. Configure Change Data Capture on SQL Server </b>
        <pre>
            <p>The SQL Server database must be configured to enable the Change Data Capture (CDC) feature.
            The connector requires this feature be enabled for the table(s) that should be 
            captured.</p>
        </pre>
        <pre>
            <b> To enable CDC on the monitored database, use following SQL command:
            <p>
                USE MyDB 
                GO 
                EXEC sys.sp_cdc_enable_db 
                GO
            </p>
            <b> Enable CDC for each table that you plan to monitor </b>
            <p>
               USE MyDB
               GO
                EXEC sys.sp_cdc_enable_table @source_schema = N’dbo’, @source_name = N’MyTable’, @role_name = N’MyRole’, @filegroup_name = N’MyDB_CT’, @supports_net_changes = 1
               GO
            </p>
        </pre>
        <pre>
            <b> Check if the SQL Server plugin has been installed correctly and picked up by plugin loader
            <p>
                curl -sS localhost:8083/connector-plugins | jq '.[].class' | grep SqlServer
                "io.debezium.connector.sqlserver.SqlServerConnector"
            </p>
        </pre>
<h2> Create Test Data and Enable Change Data Capture </h2>
    <p> To enable CDC on the monitored database, use the following SQL command: </p>
    <pre>
        USE MyDB
        GO
        EXEC sys.sp_cdc_enable_db
        GO
    </pre>
    <p> Enable CDC for each table that you plan to monitor</p>
    <pre>
        USE MyDB
        GO
        EXEC sys.sp_cdc_enable_table @source_schema = N'dbo', @source_name = N'MyTable', @role_name = N'MyRole', @filegroup_name = N'MyDB_CT', @supports_net_changes = 1
        GO
    </pre>

    <h2> In this example, the database testDB is pupulated with a set of customer records</p>
    <p> Create the test database </p>
    <pre>
        CREATE DATABASE testDB;
        GO
        USE testDB;
        EXEC sys.sp_cdc_enable_db;
    <pre>
    <p>Create some customers </p>
    <pre>
        CREATE TABLE customers (
            id INTEGER IDENTITY(1001,1) NOT NULL PRIMARY KEY,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE
            );
    </pre>
    <p> Insert some values into customers table </p>
    <pre>
        INSERT INTO customers(first_name,last_name,email)
            VALUES ('Sally','Thomas','sally.thomas@acme.com');
        INSERT INTO customers(first_name,last_name,email)
            VALUES ('George','Bailey','gbailey@foobar.com');
        INSERT INTO customers(first_name,last_name,email)
            VALUES ('Edward','Walker','ed@walker.com');
        INSERT INTO customers(first_name,last_name,email)
            VALUES ('Anne','Kretchmar','annek@noanswer.org');
        GO
    </pre>
    <p> Enable table level CDC </p>
    <pre>
        EXEC sys.sp_cdc_enable_table @source_schema = 'dbo', @source_name = 'customers', @role_name = NULL, @supports_net_changes = 0;
        GO
    </pre>

<h2> Start the Debezium SQL Server connector </h2>
<p> Create the file register-sqlserver.json to store the following connector configuration:</p>
<pre>
    {
    "name": "inventory-connector",
    "config": {
        "connector.class" : "io.debezium.connector.sqlserver.SqlServerConnector",
        "tasks.max" : "1",
        "database.server.name" : "server1",
        "database.hostname" : "localhost",
        "database.port" : "1433",
        "database.user" : "sa",
        "database.password" : "Password!",
        "database.dbname" : "testDB",
        "database.history.kafka.bootstrap.servers" : "localhost:9092",
        "database.history.kafka.topic": "schema-changes.inventory"
        }
    }
</pre>
<p> Start the connector </p>
<pre>
    curl -i -X POST -H "Accept:application/json" -H "Content-Type:application/json" http://localhost:8083/connectors/ -d @register-sqlserver.json
</pre>

<p> Insert New Records </p>
<pre>
    USE testDB;
    INSERT INTO customers(first_name,last_name,email) VALUES ('Pam','Thomas','pam@office.com');
    GO
</pre>

<h2>Clean up resources</h2>
<p> Delete the connector and stop Confluent services. </p>
<pre><tab><tab>
    curl -X DELETE localhost:8083/connectors/inventory-connector
</pre>