curl -i -X PUT -H "Accept:application/json" \
    -H "Content-Type:application/json" http://localhost:8083/connectors/CsvSchemaSpoolDir/config" \

    -d '{
        "connector.class":"com.github.jcustenborder.kafka.connect.spooldir.SpoolDirCsvSourceConnector",
        "tasks.max":"1",
        "input.path":"/data/unprocessed",
        "input.file.pattern":"csv-spooldir-source.csv"
        "error.path":"/path/to/error",
        "finished.path":"/data/finished",
        "halt.on.error":"false",
        "topic":"spooldir-testing-topic",
        "csv.first.row.as.header":"true",
        "key.schema":"{\n  \"name\" : \"com.example.users.UserKey\",\n  \"type\" : \"STRUCT\",\n  \"isOptional\" : false,\n  \"fieldSchemas\" : {\n    \"id\" : {\n      \"type\" : \"INT64\",\n      \"isOptional\" : false\n    }\n  }\n}",
        "value.schema":"{\n  \"name\" : \"com.example.users.User\",\n  \"type\" : \"STRUCT\",\n  \"isOptional\" : false,\n  \"fieldSchemas\" : {\n    \"id\" : {\n      \"type\" : \"INT64\",\n      \"isOptional\" : false\n    },\n    \"first_name\" : {\n      \"type\" : \"STRING\",\n      \"isOptional\" : true\n    },\n    \"last_name\" : {\n      \"type\" : \"STRING\",\n      \"isOptional\" : true\n    },\n    \"email\" : {\n      \"type\" : \"STRING\",\n      \"isOptional\" : true\n    },\n    \"gender\" : {\n      \"type\" : \"STRING\",\n      \"isOptional\" : true\n    },\n    \"ip_address\" : {\n      \"type\" : \"STRING\",\n      \"isOptional\" : true\n    },\n    \"last_login\" : {\n      \"type\" : \"STRING\",\n      \"isOptional\" : true\n    },\n    \"account_balance\" : {\n      \"name\" : \"org.apache.kafka.connect.data.Decimal\",\n      \"type\" : \"BYTES\",\n      \"version\" : 1,\n      \"parameters\" : {\n        \"scale\" : \"2\"\n      },\n      \"isOptional\" : true\n    },\n    \"country\" : {\n      \"type\" : \"STRING\",\n      \"isOptional\" : true\n    },\n    \"favorite_color\" : {\n      \"type\" : \"STRING\",\n      \"isOptional\" : true\n    }\n  }\n}"
    }'
   
curl -i -X PUT -H "Accept:application/json" \
    -H "Content-Type:application/json" http://localhost:8083/connectors/CsvSchemaSpoolDir/config \
    -d '{
        "connector.class":"com.github.jcustenborder.kafka.connect.spooldir.SpoolDirCsvSourceConnector",
        "tasks.max":"1",
        "input.path":"/data/unprocessed",
        "input.file.pattern":"csv-spooldir-source.csv",
        "error.path":"/data/error",
        "finished.path":"/data/processed",
        "halt.on.error":"false",
        "topic":"spooldir-testing-topic",
        "csv.first.row.as.header":"true",
        "schema.generation.enabled":"true"

    }'


2. TSV Input File Example 

'''
    The following example loads a TSV file and produces each record to kafka.

    1. Generate a TSV dataset using the command below:

        curl "https://api.mockaroo.com/api/b10f7e90?count=1000&key=25fd9c80" > "tsv-spooldir-source.tsv"

    2. Create a spooldir.properties file with the following contents:

        name=TsvSpoolDir
        tasks.max=1
        connector.class=com.github.jcustenborder.kafka.connect.spooldir.SpoolDirCsvSourceConnector
        input.path=/path/to/data
        input.file.pattern=tsv-spooldir-source.tsv
        error.path=/path/to/error
        finished.path=/path/to/finished
        halt.on.error=false
        topic=spooldir-tsv-topic
        schema.generation.enabled=true
        csv.first.row.as.header=true
        csv.separator.char=9
'''
# Curl to create connector 
    curl -i -X PUT -H "Accept:application/json" \
        -H "Content-Type:application/json" http://localhost:8083/connectors/TsvSpoolDir/config \
        -d '{
            "connector.class":"com.github.jcustenborder.kafka.connect.spooldir.SpoolDirCsvSourceConnector",
            "topic":"spooldir-tsv-topic",
            "input.path":"/data/unprocessed",
            "finished.path":"/data/processed",
            "error.path":"/data/error",
            "input.file.pattern":"tsv-spooldir-source.tsv",
            "schema.generation.enabled":"true",
            "csv.first.row.as.header":"true",
            "csv.separator.char":"9"

        }'


3. JSON Source Connector

    This connector is used to stream JSON files from a directory while also converting the data 
    based on the schema supplied in the configuration. 

    # JSON Source Connector Example 
    1. Generate a JSON dataset using the command below:
        curl "https://api.mockaroo.com/api/17c84440?count=500&key=25fd9c80" > "json-spooldir-source.json"

    2. Create a spooldir.properties file with following contents:

        name=JsonSpoolDir
        tasks.max=1 
        connector.class=com.github.jcustenborder.kafka.connect.spooldir.SpoolDirJsonSourceConnector
        input.path=/path/to/data
        input.file.pattern=json-spooldir-source.json 
        error.path=/path/to/error
        finished.path=/path/to/finished 
        halt.on.error=false 
        topic=spooldir-json-topic 
    
    # Curl to create connector 
    curl -i -X PUT -H "Accept:application/json" \
        -H "Content-Type:application/json" http://localhost:8083/connectors/JsonSpoolDir/config \
        -d '{
            "connector.class":"com.github.jcustenborder.kafka.connect.spooldir.SpoolDirJsonSourceConnector",
            "topic":"spooldir-json-topic",
            "tasks.max":"1",
            "input.path":"/data/unprocessed",
            "input.file.pattern":"json-spooldir-source.json",
            "error.path":"/data/error",
            "finished.path":"/data/processed",
            "halt.on.error":"false",
            "schema.generation.enabled":"true"
        }'

    # JSON Schemaless Source Connector Example:

        1. Generate a JSON dataset using the command below:
            curl "https://api.mockaroo.com/api/17c84440?count=500&key=25fd9c80" > "json-spooldir-source.json"
        
        2. Create a spooldir.properties file with the following contents:

            name=SchemaLessJsonSpoolDir 
            tasks.max=1
            connector.class=com.github.jcustenborder.kafka.connect.spooldir.SpoolDirSchemaLessJsonSourceConnector
            input.path=/path/to/data 
            input.file.pattern=json-spooldir-source.json 
            error.path=/path/to/error 
            finished.path=/path/to/finished 
            halt.on.error=false
            topic=spooldir-schemaless-json-topic 
            value.converter=org.apache.kafka.connect.storage.StringConverter 
    
        ## Curl 
            curl -i -X PUT -H "Accept:application/json" \
                -H "Content-Type:application/json" http://localhost:8083/connectors/SchemaLessJsonSpoolDir/config \
                -d '{
                    "connector.class":"com.github.jcustenborder.kafka.connect.spooldir.SpoolDirSchemaLessJsonSourceConnector",
                    "topic":"spooldir-schemaless-json-topic",
                    "tasks.max":"1",
                    "input.path":"/data/unprocessed",
                    "input.file.pattern":"json-spooldir-source.json",
                    "error.path":"/data/error",
                    "finished.path":"/data/processed",
                    "halt.on.error":"false",
                    "value.converter":"org.apache.kafka.connect.storage.StringConverter"
                }'
        
