from flask import Flask, jsonify
from kubernetes import client, config

app = Flask(__name__)

def get_deployment_versions():
    config.load_incluster_config()
    api_client = client.ApiClient()
    v1 = client.AppsV1Api(api_client)
    deployment_list = v1.list_deployment_for_all_namespaces().items
    
    versions = []
    for deployment in deployment_list:
        metadata = deployment.metadata
        labels=None
        if metadata is not None:
            labels=metadata.labels
        versions.append(labels)

    return versions

@app.route('/get-versions')
def get_versions():
    versions = get_deployment_versions()
    return jsonify({'versions':versions})

@app.route('/echo')
def echo():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
