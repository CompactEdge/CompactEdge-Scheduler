REMOTE_CONTROL_DOCKER_META = {
    'set_up_mkdir': {
        'service_func': 'execute_command',
        'service_command': """echo '{password}' | sudo -S docker info | grep -i Cgroup""",
    },
    'set_up_gpg_key': {
        'service_func': 'execute_command',
        'service_command': """echo '{password}' | sudo -S sh -c "curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --yes --dearmor -o /etc/apt/keyrings/docker.gpg" """,
    },
    'set_up_repo_key': {
        'service_func': 'execute_command',
        'service_command': """echo '{password}' | sudo -S sh -c "echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null" """
    },
    'edit_cgroup_docker': {
        'service_func': 'execute_command',
        'service_command': """echo '{password}' | sudo -S sh -c 'echo "{value}" > /etc/docker/daemon.json'""",
        'service_value': {
            "exec-opts": ["native.cgroupdriver=systemd"],
            "log-driver": "json-file",
            "log-opts": {
                "max-size": "100m"
            },
            "storage-driver": "overlay2"
        }
    },
    'status_cgroup_docker': {
        'service_func': 'execute_command',
        'service_command': """echo '{password}' | sudo -S docker info | grep -i Cgroup""",
    },
}
