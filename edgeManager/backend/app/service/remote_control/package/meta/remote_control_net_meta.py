REMOTE_CONTROL_NET_META = {
    'ip_forward_alter': {
        'service_func': 'execute_command',
        'service_command': """echo '{password}' | sudo -S sh -c 'echo 1 > /proc/sys/net/ipv4/ip_forward'""",
    },
    'iptables_modprobe_overlay': {
        'service_func': 'execute_command',
        'service_command': """echo '{password}' | sudo -S modprobe overlay""",
    },
    'iptables_modprobe_br_netfilter': {
        'service_func': 'execute_command',
        'service_command': """echo '{password}' | sudo -S modprobe br_netfilter""",
    },
    'iptables_bridge_nf_call_iptables_create': {
        'service_func': 'execute_command',
        'service_command': """echo '{password}' | sudo -S sh -c 'echo 1 > /proc/sys/net/bridge/bridge-nf-call-iptables'""",
    },
    'iptables_k8s_conf_create': {
        'service_func': 'execute_command',
        'service_command': """echo '{password}' | sudo -S sh -c 'echo "net.bridge.bridge-nf-call-ip6tables = 1\nnet.bridge.bridge-nf-call-iptables = 1\nnet.ipv4.ip_forward = 1" > /etc/sysctl.d/k8s.conf'""",
    },
    'ip_forward_validate': {
        'service_func': 'execute_command',
        'service_command': """echo '{password}' | sudo -S cat /proc/sys/net/ipv4/ip_forward""",
    },
    'iptables_bridge_nf_call_iptables_validate': {
        'service_func': 'execute_command',
        'service_command': """echo '{password}' | sudo -S cat /proc/sys/net/bridge/bridge-nf-call-iptables""",
    },
    'iptables_k8s_conf_validate': {
        'service_func': 'execute_command',
        'service_command': """echo '{password}' | sudo -S sudo cat /etc/sysctl.d/k8s.conf""",
    },
}
