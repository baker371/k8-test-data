# Deploying the ELK Stack 

This Docker image runs ELK (Elasticsearch, Logstash and Kibana) stack in Kubernetes using Helm Charts, to get application logs.

### How it works
1. Logstash should be installed in each of the nodes in the cluster to collect the logs in each node and forwards them to Elasticsearch. 
2. Elasticsearch gets the logs and insert them into its database.
3. Kibana will querry Elasticsearch database for logs and visualise them.

### Deploying ELK 

#### 1. Manual Installation

1. Install Helm charts
```sh
$ wget https://get.helm.sh/helm-v3.0.2-linux-amd64.tar.gz 
```
```sh
$ tar xvf helm-v3.0.2-linux-amd64.tar.gz 
```
```sh
$ mv linux-amd64/helm /usr/local/bin/
```
```sh
$ rm helm-v3.0.2-linux-amd64.tar.gz 
```
```sh
$ rm -rf linux-amd64 
```

```sh
$ helm repo add elastic https://Helm.elastic.co
```

2. Install Elasticsearch
    
```sh
$ helm install elasticsearch elastic/elasticsearch
```
3. Install Logistash
```sh
$ wget https://github.com/elastic/helm-charts/blob/master/logstash/values.yaml
```
```sh
$ kubectl create -f .\values.yaml 
```
```sh
$ rm -rf values.yaml
```
4. Installing Kibana
```sh
$ helm install kibana elastic/kibana -f ./log/kibana_values.yaml
```
5. Get Kibana external IP with port into the browser i.e 51.137.28.62:443, to open the dashboard
```sh
$ kubectl get services
```
6. Video Instuctions on setup


