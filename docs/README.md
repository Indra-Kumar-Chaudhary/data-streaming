<h1> ksqlDB </h1>
<b> Connect to ksqldb Server <b>
    <pre>docker exec -it ksqldb-cli ksql http://ksqldb-server:8088 </pre>

<b> Tell ksqlDB to start all queries from earliest point in each <b>
    <pre>SET 'auto.offset.reset' = 'earliest';</pre>


<b> Connector Creation </b>
<pre>
    CREATE SOURCE CONNECTOR customers_reader WITH (
        'connector.class' = 'io.debezium.connector.postgresql.PostgresConnector',
        'database.hostname' = 'postgres',
        'database.port' = '5432',
        'database.user' = 'postgres-user',
        'database.password' = 'postgres-pw',
        'database.dbname' = 'customers',
        'database.server.name' = 'customers',
        'table.whitelist' = 'public.customers',
        'transforms' = 'unwrap',
        'transforms.unwrap.type' = 'io.debezium.transforms.ExtractNewRecordState',
        'transforms.unwrap.drop.tombstones' = 'false',
        'transforms.unwrap.delete.handling.mode' = 'rewrite'
    );
<pre>

<h1> Creating the Postgres connector </h1>

<pre>
    {
        "name": "source-pg-customer-connect",
        config: {
                'connector.class' = 'io.debezium.connector.postgresql.PostgresConnector',
                'database.hostname' = 'postgres',
                'database.port' = '5432',
                'database.user' = 'postgres-user',
                'database.password' = 'postgres-pw',
                'database.dbname' = 'customers',
                'database.server.name' = 'customers',
                'table.whitelist' = 'public.customers',
                'transforms' = 'unwrap',
                'transforms.unwrap.type' = 'io.debezium.transforms.ExtractNewRecordState',
                'transforms.unwrap.drop.tombstones' = 'false',
                'transforms.unwrap.delete.handling.mode' = 'rewrite'
        }
    }
</pre>

<pre>
    curl -i -X POST -H "Accept:application/json" -H "Content-Type:application/json" \
    http://$CURRENT_HOST:8083/connectors/ -d @postgres-connect.json
</pre>


<h1> Create customer deail streams </h1>
    <pre>
        create stream customer_details WITH (kafka_topic = 'customer_details') AS SELECT * FROM customers emit changes;
    </pre>

<h1> Elasticsearch Sink Connector </h1>
    <pre>
    {
        "name": "sink_elastic_pg_customer_connector",
        "config": {
                "connector.class":"io.confluent.connect.elasticsearch.ElasticsearchSinkConnector",
                "connection.url":"http://elastic:9200",
                "type.name":"kafka-connect",
                "topics":"shipped_orders"
        }
    }
        
    </pre>

<p>
Check that the data arrived in the index by running the following command from your host:</p>

<pre>curl http://localhost:9200/shipped_orders/_search?pretty </pre>
