import os


class Config(object):
    basedir = os.path.abspath(os.path.dirname(__file__))


class LocalConfig(Config):
    MASTER_IP = '10.7.23.111'

    DEBUG = True
    CONFIG_FILE = Config.basedir + "/kube_config.yaml"

    REPOS_IP = MASTER_IP
    REPOS_PORT = 5000

    MONITORING_IP = MASTER_IP
    MONITORING_PORT = 9090

    # elasticsearch
    ELASTICSEARCH_SERVER = MASTER_IP
    ELASTICSEARCH_PORT = 9200
    ELASTICSEARCH_USERNAME = 'edgeuser'
    ELASTICSEARCH_PASSWORD = 'qwe123'

    # remote_control
    DOCKER_VERSIONS = """docker.io=20.10.12-0ubuntu2~20.04.1"""
    K8S_VERSIONS = """kubelet=1.23.3-00 kubeadm=1.23.3-00 kubectl=1.23.3-00"""
    K8S_MASTER_NODE_INFO = {
        'server': MASTER_IP,
        'port': '22',
        'username': 'ubuntu',
        'password': 'qwe123'
    }

    LOGGER_NAME = "log"
    LOG_LEVEL = "debug"
    LOG_FILE = ""


class DevelopmentConfig(Config):
    MASTER_IP = '10.7.23.111'

    DEBUG = True
    CONFIG_FILE = os.path.expanduser('~')+"/.kube/config"

    REPOS_IP = '10.4.18.215'
    REPOS_PORT = 5000

    MONITORING_IP = "10.4.18.212"
    MONITORING_PORT = 9090

    # elasticsearch
    ELASTICSEARCH_SERVER = '10.4.18.213'
    ELASTICSEARCH_PORT = 9200
    ELASTICSEARCH_USERNAME = 'edgeuser'
    ELASTICSEARCH_PASSWORD = 'qwe123'

    # remote_control
    DOCKER_VERSIONS = """docker.io=20.10.12-0ubuntu2~20.04.1"""
    K8S_VERSIONS = """kubelet=1.23.3-00 kubeadm=1.23.3-00 kubectl=1.23.3-00"""
    K8S_MASTER_NODE_INFO = {
        'server': MASTER_IP,
        'port': '22',
        'username': 'ubuntu',
        'password': 'qwe123'
    }

    LOGGER_NAME = "log"
    LOG_LEVEL = "debug"
    LOG_FILE = "/applog/edgeManager/edgeManager.log"


class ProductionConfig(Config):
    MASTER_IP = '192.168.54.41'

    DEBUG = False
    CONFIG_FILE = os.path.expanduser('~')+"/.kube/config"

    REPOS_IP = '192.168.54.42'
    REPOS_PORT = 5000

    MONITORING_IP = "192.168.54.41"
    MONITORING_PORT = 9090

    # elasticsearch
    ELASTICSEARCH_SERVER = '192.168.54.43'
    ELASTICSEARCH_PORT = 9200
    ELASTICSEARCH_USERNAME = 'edgeuser'
    ELASTICSEARCH_PASSWORD = 'qwe123'

    # remote_control
    DOCKER_VERSIONS = """docker.io=20.10.12-0ubuntu2~20.04.1"""
    K8S_VERSIONS = """kubelet=1.23.3-00 kubeadm=1.23.3-00 kubectl=1.23.3-00"""
    K8S_MASTER_NODE_INFO = {
        'server': MASTER_IP,
        'port': '22',
        'username': 'ubuntu',
        'password': 'qwe123'
    }

    LOGGER_NAME = "log"
    LOG_LEVEL = "info"
    LOG_FILE = "/applog/edgeManager/edgeManager.log"


# Load all possible configurations
config_dict = {
    'Local': LocalConfig,
    'Dev': DevelopmentConfig,
    'Prod': ProductionConfig,
}
