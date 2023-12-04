REMOTE_CONTROL_K8S_META = {
    'set_up_gpg_key': {
        'service_func': 'execute_command',
        'service_command': """echo '{password}' | sudo -S curl -fsSLo /usr/share/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg""",
    },
    'set_up_repo_key': {
        'service_func': 'execute_command',
        'service_command': """echo '{password}' | sudo -S sh -c "echo 'deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main' > /etc/apt/sources.list.d/kubernetes.list" """,
    },
    'get_join_command': {
        'service_func': 'execute_command',
        'service_command': """echo '{password}' | sudo -S kubeadm token create --print-join-command""",
    },
    'join_worker_node': {
        'service_func': 'execute_command',
        'service_command': """echo '{password}' | sudo -S {value}\n""",
    },
}
