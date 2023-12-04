REMOTE_CONTROL_SWAP_META = {
    'swap_off': {
        'service_func': 'execute_command',
        'service_command': """echo '{password}' | sudo -S swapoff -a""",
    },
    'swap_remove': {
        'service_func': 'execute_command',
        'service_command': """echo '{password}' | sudo -S rm -f {swap_file_name}""",
    },
    'swap_disable': {
        'service_func': 'execute_command',
        'service_command': """echo '{password}' | sudo -S sed -i '{swap_file_name}/s/^/#/' /etc/fstab""",
    },
    'swap_validate': {
        'service_func': 'execute_command',
        'service_command': """echo '{password}' | sudo -S swapon --show""",
    },
    '__swap_file_name': {
        'service_func': 'execute_command',
        'service_command': """echo '{password}' | sudo -S cat /etc/fstab""",
    },
}
