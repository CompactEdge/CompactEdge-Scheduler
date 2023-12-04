REMOTE_CONTROL_SYSTEMD_META = {
    'systemd_daemon_reload': {
        'service_type': '',
        'service_func': 'execute_command',
        'service_name': '',
        'service_command': """echo '{password}' | sudo -S systemctl daemon-reload""",
    },
    'systemd_disable': {
        'service_type': '',
        'service_func': 'execute_command',
        'service_name': '',
        'service_command': """echo '{password}' | sudo -S systemctl disable {app}"""
    },
    'systemd_enable': {
        'service_type': '',
        'service_func': 'execute_command',
        'service_name': '',
        'service_command': """echo '{password}' | sudo -S systemctl enable {app}"""
    },
    'systemd_restart': {
        'service_type': '',
        'service_func': 'execute_command',
        'service_name': '',
        'service_command': """echo '{password}' | sudo -S systemctl restart {app}"""
    },
    'systemd_status': {
        'service_type': '',
        'service_func': 'execute_command',
        'service_name': '',
        'service_command': """echo '{password}' | sudo -S systemctl status {app}"""
    },
    'systemd_stop': {
        'service_type': '',
        'service_func': 'execute_command',
        'service_name': '',
        'service_command': """echo '{password}' | sudo -S systemctl stop {app}"""
    },
}
