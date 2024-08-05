<h2>Getting Started</h2>
<h4> Build container instances and start them</h4>
<pre>
    <p> Sample connecctor look in JSON </p>
    {
        "name": "DatagenSourceConnector_0",
        "config": {
            "connector.class": "DatagenSource",
            "name": "DatagenSourceConnector_0",
            "kafka.auth.mode": "KAFKA_API_KEY",
            "kafka.api.key": "****************",
            "kafka.api.secret": "****************************************************************",
            "kafka.topic": "orders",
            "output.data.format": "JSON",
            "quickstart": "ORDERS",
            "tasks.max": "1"
        }
    }
</pre>


# To check kafka connector installed 
curl -s localhost:8083/connector-plugins | jq '.[].class'