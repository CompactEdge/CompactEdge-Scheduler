REMOTE_CONTROL_COMMON_META = {
    'validate_node': {
        'service_func': 'execute_command',
        'service_name': 'validate_node',
        'service_command': """echo '{password}' | sudo -S echo $HOSTNAME"""
    },
}
