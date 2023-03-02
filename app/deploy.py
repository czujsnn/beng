import subprocess
import logging

def create_deployment(yaml_file):
    # Run the kubectl apply command with the YAML file
    cmd = ['kubectl', 'apply', '-f', yaml_file]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode == 0:
        output = result.stdout.decode('utf-8')
        cmd = ['kubectl', 'get', 'pods', '-o', 'wide']
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # ip = parse_ip_from_output(result.stdout.decode('utf-8'))
        ip = "IP HERE. Succesfully callled /create and deployment was created" + str(result)
        return ip
    else:
        error = result.stderr.decode('utf-8')
        raise Exception(error)


def parse_ip_from_output(output):
    lines = output.split('\n')
    return str(lines[0])

def delete_deployment(deployment_name):
    cmd = ['kubectl', 'delete', 'deployment', deployment_name]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode == 0:
        status = result.stdout.decode('utf-8')
        return status
    else:
        error = result.stderr.decode('utf-8')
        raise Exception(error)
