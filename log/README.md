# Deploying the ELK Stack 

This Docker image runs ELK (Elasticsearch, Logstash and Kibana) stack in Kubernetes using Helm Charts, to get application logs.

### How it works
1. Logstash should be installed in each of the nodes in the cluster to collect the logs in each node and forwards them to Elasticsearch. 
2. Elasticsearch gets the logs and insert them into its database.
3. Kibana will querry Elasticsearch database for logs and visualise them.


### Deploying ELK 

1. Build a Docker image
    
```sh
$ docker build -t elk-log ./log
```
2. Run the docker image
```sh
$ docker run elk-log
```
3. Get Running Services
```sh
$ kubectl get services
```
4. Copy Kibana external IP with port into the browser i.e 51.137.28.62:443, to open the dashboard

