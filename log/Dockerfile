FROM ubuntu:20.04

# Install prerequisites
RUN apt-get update && apt-get install -y \
	wget 
	
CMD /bin/bash

ENV KUBE_LATEST_VERSION="v1.19.2"

RUN wget -q https://storage.googleapis.com/kubernetes-release/release/${KUBE_LATEST_VERSION}/bin/linux/amd64/kubectl -O /usr/local/bin/kubectl \
    && chmod +x /usr/local/bin/kubectl \
    && chmod g+rwx /root \
    && mkdir /config \
    && chmod g+rwx /config    

WORKDIR /config


RUN wget https://get.helm.sh/helm-v3.0.2-linux-amd64.tar.gz  

RUN tar xvf helm-v3.0.2-linux-amd64.tar.gz  					

RUN	mv linux-amd64/helm /usr/local/bin/ 
     					 
RUN	rm helm-v3.0.2-linux-amd64.tar.gz         					  
	
RUN rm -rf linux-amd64
	

RUN helm repo add elastic https://Helm.elastic.co

RUN helm install elasticsearch elastic/elasticsearch

RUN wget https://github.com/elastic/helm-charts/blob/master/logstash/values.yaml 

RUN kubectl create -f .\values.yaml 

RUN rm -rf values.yaml

RUN helm install kibana elastic/kibana -f ./log/kibana_values.yaml

#kubctl get services: pick ip with port

	
CMD bash