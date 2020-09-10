# VirusShare POC

### Usage

## Run app

`python main.py`

## Run test cases
`python -m unittest`

### Endpoints [ All POST ]

| Endpoint | Description             | Payload     |
| -------- | ------------------------| ----------- |
| `/scrape-vs-file`  | Download a file from VS   | `{"api_key": "","hash"   : ""}` |
| `/check-malicious` | Check if a file is malicious   | `{"file": "<binary file>"}` |
| `/fetch-vs-files` | Get all VS malicious files from hash   |  |
| `/files` | Get malicious files   | `{"file_type": "txt", "num_files":2}` |	

## Docker Image

### Build

To build the Docker image and name it `k8-test-data` run:

`docker build -t k8-test-data .`

To push
`docker push <username>/k8-test-data`

### Run

To run the aforementioned built image run:

`docker run -e STATIC_PATH=<static_path> -e vs_zip_pwd=<pwd> -e PYTHONUNBUFFERED=0 -e virustotal_key=<key> -e vs_api_key=<key> -p 5000:5000 -it --rm k8-test-data`

To run the aforementioned built image along with minio, run:

`docker-compose up --build`

## Kubernetes

To run through kubernetes

```
kubectl apply -f minio_service.yaml
kubectl apply -f deploy.yaml
```
