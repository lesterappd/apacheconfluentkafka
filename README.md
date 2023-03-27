# apacheconfluentkafka
AppDynamics Extension to pull Apache Confluent Kafka (SaaS) metrics into AppDynamics.

## Use Case
Confluent Platform is a full-scale data streaming platform that enables you to easily access, store, and manage data as continuous, real-time streams. Built by the original creators of Apache Kafka®, Confluent expands the benefits of Kafka with enterprise-grade features while removing the burden of Kafka management or monitoring. 

The confluent platform exposes runtime monitoring metrics around Apache Kafka as explained here
https://docs.confluent.io/cloud/current/monitoring/metrics-api.html

This extension exports the monitoring metrics and pushes them into AppDynamics.


## Prerequisites

## Installation

1. Clone the "apacheconfluentkafka" repo using `git clone <repoUrl>` command.
2. 


## Configuration
### Config.yml

Configure the extension by editing the config.yml file in `<MACHINE_AGENT_HOME>/monitors/ApacheConfluentKafka/`.

  1. Configure the "COMPONENT_ID" under which the metrics need to be reported. This can be done by changing the value of `<COMPONENT_ID>` in   **metricPrefix: Server|Component:<COMPONENT_ID>|Custom Metrics|ApacheConfluentKafka|**.
       For example,
       ```
       metricPrefix: "Server|Component:100|Custom Metrics|ApacheConfluentKafka|"
       ```
  More details around metric prefix can be found [here](https://community.appdynamics.com/t5/Knowledge-Base/How-do-I-troubleshoot-missing-custom-metrics-or-extensions/ta-p/28695).



## Contributing
Always feel free to fork and contribute any changes directly here on [GitHub](https://github.com/lesterappd/apacheconfluentkafka).


**Note**: While extensions are maintained and supported by customers under the open-source licensing model, they interact with agents and Controllers that are subject to [AppDynamics’ maintenance and support policy](https://docs.appdynamics.com/latest/en/product-and-release-announcements/maintenance-support-for-software-versions). Some extensions have been tested with AppDynamics 4.5.13+ artifacts, but you are strongly recommended against using versions that are no longer supported.
