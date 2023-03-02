from flask import Flask, render_template, jsonify, request
from deploy import create_deployment, delete_deployment

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('main.html')

@app.route('/create', methods=['POST'])
def create():
    try:
        # Call the run_terraform()/kuberentes() function to deploy the Kubernetes POD
        yaml_file = 'C:\\repos\\beng\\app\\deployment.yaml'
        ip = create_deployment(yaml_file)

        # Return the POD IP as a JSON response
        response = {'ip': ip}
        return jsonify(response)
    except:
        return "Error while calling /create"
    
@app.route('/delete', methods=['POST'])
def delete():
    try:
        deployment_name = 'nginx-deployment' #hardcoded for now
        status = delete_deployment(deployment_name)

        response = {'delete_pod': status}
        return jsonify(response)
    except:
        return "Error while calling /delete"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
