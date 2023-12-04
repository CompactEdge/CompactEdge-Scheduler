from .remote_control_apt_meta import REMOTE_CONTROL_APT_META
from .remote_control_common_meta import REMOTE_CONTROL_COMMON_META
from .remote_control_docker_meta import REMOTE_CONTROL_DOCKER_META
from .remote_control_k8s_meta import REMOTE_CONTROL_K8S_META
from .remote_control_net_meta import REMOTE_CONTROL_NET_META
from .remote_control_swap_meta import REMOTE_CONTROL_SWAP_META
from .remote_control_systemd_meta import REMOTE_CONTROL_SYSTEMD_META

REMOTE_CONTROL_META = {
    'remote_control_apt_meta': REMOTE_CONTROL_APT_META,
    'remote_control_common_meta': REMOTE_CONTROL_COMMON_META,
    'remote_control_docker_meta': REMOTE_CONTROL_DOCKER_META,
    'remote_control_k8s_meta': REMOTE_CONTROL_K8S_META,
    'remote_control_net_meta': REMOTE_CONTROL_NET_META,
    'remote_control_swap_meta': REMOTE_CONTROL_SWAP_META,
    'remote_contorl_systemd_meta': REMOTE_CONTROL_SYSTEMD_META,
}