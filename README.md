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
        

