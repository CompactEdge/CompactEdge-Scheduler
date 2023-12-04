REMOTE_CONTROL_APT_META = {
    'apt_update': {
        'service_func': 'execute_invoke_shell',
        'service_command': """echo '{password}' | sudo -S apt update -y\n""",
    },
    'apt_upgrade': {
        'service_func': 'execute_invoke_shell',
        'service_command': """echo '{password}' | sudo -S apt upgrade -y\n""",
    },
    'apt_install': {
        'service_func': 'execute_invoke_shell',
        'service_command': """echo '{password}' | sudo -S apt install {apps} -y\n""",
    },
    'apt_mark': {
        'service_func': 'execute_invoke_shell',
        'service_command': """echo '{password}' | sudo -S apt-mark {option} {apps}\n""",
    },
}
