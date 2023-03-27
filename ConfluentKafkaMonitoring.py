#Confluent Kafka Monitoring
# 
from prometheus_client.parser import text_string_to_metric_families
import requests
import sys
import yaml

def main():


    # Read Configuration 
    print("Parsing Config Yaml - Retrieving Connection Details")
    config = parseConfig('config.yml')
    url = config['confluentKafkaConnection']['url']
    user = config['confluentKafkaConnection']['authUser']
    token = config['confluentKafkaConnection']['authToken']
    metricPrefix = config['metricPrefix']
    metricList = config['metricDetails']

    print(metricList)

    if "confluent_kafka_received_bytes" in metricList:
        print("metric exists")

    # Validate All necessary config is available
    
    #For each resource id - Process Metrics
    for resource in config['resourceDetails']:
        resourceName = resource['name']
        resourceType = resource['type']
        resourceID = resource['id']
        
        # Connect to Confluent API Server
        print("Retrieving metrics for resource " + resourceName + " of type " + resourceType + " and id " + resourceID)
        confluenturl = url + '?resource.kafka.id=' + str(resourceID)
        response = request(confluenturl, user, token)
        print('Response Code Connecting to Apache Confluent ' + str(response.status_code))

        #if response code is 200 then proceed else print error
        # Parse Metrics
        for family in text_string_to_metric_families(response.text):
            for sample in family.samples:
                metricName = str(sample[0])
                metricValue = sample[2]
                
                if metricName in metricList: 
                    printMetrics(metricPrefix + resourceType + "|" + resourceName + "|" + metricName, round(metricValue))
  
def parseConfig(filename):
    with open(filename, 'r') as file:
        config = yaml.safe_load(file)
    return config

def request(url, username, token):
    
    try:
        r = requests.get(url, auth=(username, token), verify=True)
        r.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error")
        print(errh.args[0])
    except requests.exceptions.ReadTimeout as errrt:
        print("Time out")
    except requests.exceptions.ConnectionError as conerr:
        print("Connection error")
    except requests.exceptions.RequestException as errex:
        print("Exception request")
    
    return r

def printMetrics(metricPrefix, value):
    
    ans = "name=" + metricPrefix + ", value=" +  str(value)    
    #ans = "name=Server|Component:919|Custom Metrics|ApacheConfluentMonitor|Cluster|d-pdt-disx-pl-90072|confluent_kafka_server_cluster_load_percent, value=10"
    print(ans)
    sys.stdout.write(ans)  


main()




