FROM confluentinc/cp-kafka-connect-base:7.5.0

ENV CONNECT_PLUGIN_PATH="/usr/share/java,/usr/share/confluent-hub-components"

RUN confluent-hub install --no-prompt confluentinc/kafka-connect-jdbc:10.0.2
RUN confluent-hub install --no-prompt jcustenborder/kafka-connect-spooldir:2.0.60
#RUN confluent-hub install --no-prompt streamthoughts/kafka-connect-file-pulse:1.5.0
RUN confluent-hub install --no-prompt confluentinc/kafka-connect-elasticsearch:14.1.0
Run confluent-hub install --no-prompt debezium/debezium-connector-sqlserver:latest
RUN confluent-hub install --no-prompt debezium/debezium-connector-postgresql:1.1.0
