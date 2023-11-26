import subprocess

def deploy_local_node():
    subprocess.run(['docker', 'pull', 'node_image'])

    subprocess.run(['docker', 'run', '-d', '--name', 'local_node', 'node_image'])

def deploy_monitoring_tools():
    subprocess.run(['docker', 'pull', 'prom/prometheus'])

    subprocess.run(['docker', 'run', '-d', '--name', 'prometheus', '-p', '9090:9090', 'prom/prometheus'])

    subprocess.run(['docker', 'pull', 'grafana/grafana'])

    subprocess.run(['docker', 'run', '-d', '--name', 'grafana', '-p', '3000:3000', 'grafana/grafana'])

if __name__ == "__main__":
    deploy_local_node()
    deploy_monitoring_tools()
