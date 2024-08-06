<h1> ksqlDB </h1>
<b> Connect to ksqldb Server <b>
    <pre>docker exec -it ksqldb-cli ksql http://ksqldb-server:8088 </pre>

<b> Tell ksqlDB to start all queries from earliest point in each <b>
    <pre>SET 'auto.offset.reset' = 'earliest';</pre>
