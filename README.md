# apacheconfluentkafka
AppDynamics Extension to pull Apache Confluent Kafka (SaaS) metrics into AppDynamics.

## Use Case
Confluent Platform is a full-scale data streaming platform that enables you to easily access, store, and manage data as continuous, real-time streams. Built by the original creators of Apache Kafka®, Confluent expands the benefits of Kafka with enterprise-grade features while removing the burden of Kafka management or monitoring. 

The confluent platform exposes runtime monitoring metrics around Apache Kafka as explained here
https://docs.confluent.io/cloud/current/monitoring/metrics-api.html

This extension exports the monitoring metrics and pushes them into AppDynamics.


## Prerequisites

1. The extension requires python3.x to run and relies on the following dependencies (prometheus_client, requests, yaml)
2. Extension requires a service account setup on the Confluent side with MetricViewer role for the resources to be monitored. Links below provide steps for setting up the service account, cloud api key for querying the confluent metrics api and details on setting up the MetricsViewer Role.

https://docs.confluent.io/cloud/current/monitoring/metrics-api.html#metrics-quick-start
https://docs.confluent.io/cloud/current/monitoring/metrics-api.html#add-the-metricsviewer-role-to-a-new-service-account-in-the-ccloud-console

## Installation

1. Clone the "apacheconfluentkafka" repo using `git clone <repoUrl>` command.
2. Copy the extension folder to the monitors directory of the machine agent that is going to be used to run the extension.
3. Extension is configured to run on linux every minute, please update the frequency if needed in the monitor.xml



## Configuration
### Config.yml

Configure the extension by editing the config.yml file in `<MACHINE_AGENT_HOME>/monitors/ApacheConfluentKafka/`.

  1. Configure the "COMPONENT_ID" under which the metrics need to be reported. This can be done by changing the value of `<COMPONENT_ID>` in   **metricPrefix: Server|Component:<COMPONENT_ID>|Custom Metrics|ApacheConfluentKafka|**.
       For example,
       ```
       metricPrefix: "Server|Component:100|Custom Metrics|ApacheConfluentKafka|"
       ```
  More details around metric prefix can be found [here](https://community.appdynamics.com/t5/Knowledge-Base/How-do-I-troubleshoot-missing-custom-metrics-or-extensions/ta-p/28695).
  
  2. Configure the **confluentKafkaConnection** section in Config.yml to provide saas url for confluent kafka and authentication user and token for authentication. Apache Confluent documentation that provides steps to setup instructions to setup Cloud API key to authenticate to the Metrics API and configure the MetricViewer Role to the service account used to query the metrics api.

https://docs.confluent.io/cloud/current/monitoring/metrics-api.html#metrics-quick-start
https://docs.confluent.io/cloud/current/monitoring/metrics-api.html#add-the-metricsviewer-role-to-a-new-service-account-in-the-ccloud-console

3. Configure the resources to be monitored by specifying a name, type and resource id in the **resourceDetails** section of the config.yml
4. Configure the metrics to be captured per resource type in the **metricDetails** section of the config.yml. List of available metrics are found here;

https://api.telemetry.confluent.cloud/docs/descriptors/datasets/cloud

## Troubleshooting

1.  Please follow the steps listed in this [troubleshooting document](https://community.appdynamics.com/t5/Knowledge-Base/How-do-I-troubleshoot-missing-custom-metrics-or-extensions/ta-p/28695) in order to troubleshoot your issue. These are a set of common issues that customers might have faced during the installation of the extension.
2.  **Verify Machine Agent Data:** Please start the Machine Agent without the extension and make sure that it reports data. Verify that the machine agent status is UP and it is reporting Hardware Metrics
3.  **config.yml:** Validate the file [here](https://jsonformatter.org/yaml-validator)
4.  **Special chars in config** If you have special chars(like in passwords) in config.yml, make sure to wrap it in double quotes `""`
5.  **ApacheConfluent Metrics API:** Please update the `user:token` with correct values and set the kafka resource id. Invoke the URL from curl (or wget) and make sure that it is returning data. If it is not, then contact your Apache Confluent Admin with these details
    ```
        curl -v --user <user>:<token> https://api.telemetry.confluent.cloud/v2/metrics/cloud/export?resource.kafka.id=<resource-id>
    ```

6.  **Metric Limit:** Please start the machine agent with the argument `-Dappdynamics.agent.maxMetrics=5000` if there is a metric limit reached error in the logs. If you dont see the expected metrics, this could be the cause.
7.  **Check Logs:** There could be some obvious errors in the machine agent logs. Please take a look.



## Contributing
Always feel free to fork and contribute any changes directly here on [GitHub](https://github.com/lesterappd/apacheconfluentkafka).


**Note**: While extensions are maintained and supported by customers under the open-source licensing model, they interact with agents and Controllers that are subject to [AppDynamics’ maintenance and support policy](https://docs.appdynamics.com/latest/en/product-and-release-announcements/maintenance-support-for-software-versions). Some extensions have been tested with AppDynamics 4.5.13+ artifacts, but you are strongly recommended against using versions that are no longer supported.
