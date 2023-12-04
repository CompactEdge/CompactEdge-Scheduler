from typing import Union

from utils.logger import Log as log

from .modules.remote_control_working import RemoteControlWorking
from .modules.remote_control_paramiko import RemoteControlParamiko

from .vo.remote_control_result_vo import RemoteControlResultVo
from .vo.remote_control_sessions_vo import RemoteControlSessionsVo
from .vo.remote_control_paramiko_vo import RemoteControlParamikoVo

from .meta import REMOTE_CONTROL_META
from .modules import REMOTE_CONTROL_SESSION_INFO


class RemoteControlUbuntu():

    def __init__(self):
        self.remote_control_working = RemoteControlWorking()
        self.remote_control_paramiko = RemoteControlParamiko()

        self.remote_control_apt_meta: dict = REMOTE_CONTROL_META['remote_control_apt_meta']
        self.remote_contorl_systemd_meta: dict = REMOTE_CONTROL_META['remote_contorl_systemd_meta']
        self.remote_control_swap_meta: dict = REMOTE_CONTROL_META['remote_control_swap_meta']
        self.remote_control_net_meta: dict = REMOTE_CONTROL_META['remote_control_net_meta']

        self.remote_control_session_info: RemoteControlSessionsVo = REMOTE_CONTROL_SESSION_INFO

    def __swap_file_name(self) -> Union[int, str]:
        __swap_file_name_code: str
        __swap_file_name_data: str

        try:
            __swap_file_name_meta = self.remote_control_swap_meta['__swap_file_name']
            __swap_file_name_service_command = __swap_file_name_meta['service_command']

            __swap_fstab_command = self.remote_control_paramiko.make_command(
                command=__swap_file_name_service_command,
                password=self.remote_control_session_info.password)

            __swap_fstab_paramiko_vo: RemoteControlParamikoVo = self.remote_control_paramiko.make_paramiko_vo(
                self.remote_control_session_info,
                command=__swap_fstab_command)

            __swap_fstab_code, __swap_fstab_data = self.remote_control_paramiko.execute_command(
                __swap_fstab_paramiko_vo)

            __swap_fstab_lines = __swap_fstab_data.split('\n')
            __swap_fstab_items = ''.join(
                '' if 'swap' not in __line else __line for __line in __swap_fstab_lines)

            __swap_file_name_code = 200
            __swap_file_name_data = __swap_fstab_items.split('\t')[0]

        except KeyError as ex:
            log.error('RemoteControlSwap :: __swap_file_name :: ' + str(ex))
            __swap_file_name_code = 500
            __swap_file_name_data = ''

        return __swap_file_name_code, __swap_file_name_data

    def apt_update(self, service_type: str) -> RemoteControlResultVo:
        apt_update_result_vo: RemoteControlResultVo

        try:
            apt_update_meta = self.remote_control_apt_meta['apt_update']
            apt_update_service_func = apt_update_meta['service_func']
            apt_update_service_command = apt_update_meta['service_command']
            apt_update_service_name = 'apt_update'

            apt_update_command = self.remote_control_paramiko.make_command(
                command=apt_update_service_command,
                password=self.remote_control_session_info.password)

            apt_update_paramiko_vo: RemoteControlParamikoVo = self.remote_control_paramiko.make_paramiko_vo(
                self.remote_control_session_info,
                command=apt_update_command)

            apt_update_code, apt_update_data = self.remote_control_paramiko.execute_invoke_shell(
                apt_update_paramiko_vo, service_type, apt_update_service_name)

            apt_update_result_vo = RemoteControlResultVo(
                service_code=apt_update_code,
                service_type=service_type,
                service_func=apt_update_service_func,
                service_name=apt_update_service_name,
                service_validate=(False if apt_update_code != 200 else True),
                service_result=apt_update_data)

            # self.remote_control_working.create(service_type, apt_update_service_name, apt_update_result_vo)

        except KeyError as ex:
            log.error('RemoteControlApt :: apt_update :: ' + str(ex))

        return apt_update_result_vo

    def apt_upgrade(self, service_type: str) -> RemoteControlResultVo:
        apt_upgrade_result_vo: RemoteControlResultVo

        try:
            apt_upgrade_meta = self.remote_control_apt_meta['apt_upgrade']
            apt_upgrade_service_func = apt_upgrade_meta['service_func']
            apt_upgrade_service_command = apt_upgrade_meta['service_command']
            apt_upgrade_service_name = 'apt_upgrade'

            apt_upgrade_command = self.remote_control_paramiko.make_command(
                command=apt_upgrade_service_command,
                password=self.remote_control_session_info.password)

            apt_upgrade_paramiko_vo: RemoteControlParamikoVo = self.remote_control_paramiko.make_paramiko_vo(
                self.remote_control_session_info,
                command=apt_upgrade_command)

            apt_upgrade_code, apt_upgrade_data = self.remote_control_paramiko.execute_invoke_shell(
                apt_upgrade_paramiko_vo, service_type, apt_upgrade_service_name)

            apt_upgrade_result_vo = RemoteControlResultVo(
                service_code=apt_upgrade_code,
                service_type=service_type,
                service_func=apt_upgrade_service_func,
                service_name=apt_upgrade_service_name,
                service_validate=(False if apt_upgrade_code != 200 else True),
                service_result=apt_upgrade_data)

            # self.remote_control_working.create(service_type, apt_upgrade_service_name, apt_upgrade_result_vo)

        except KeyError as ex:
            log.error('RemoteControlApt :: apt_upgrade :: ' + str(ex))

        return apt_upgrade_result_vo

    def apt_install(self, service_type: str) -> RemoteControlResultVo:
        apt_install_result_vo: RemoteControlResultVo

        try:
            apt_install_meta = self.remote_control_apt_meta['apt_install']
            apt_install_service_func = apt_install_meta['service_func']
            apt_install_service_command = apt_install_meta['service_command']
            apt_install_service_name = 'apt_install'
            apt_install_apps = ' '.join(
                ['net-tools', 'apt-transport-https', 'ca-certificates', 'curl', 'gnupg', 'lsb-release'])

            apt_install_command = self.remote_control_paramiko.make_command(
                command=apt_install_service_command,
                password=self.remote_control_session_info.password,
                apps=apt_install_apps)

            apt_install_paramiko_vo: RemoteControlParamikoVo = self.remote_control_paramiko.make_paramiko_vo(
                self.remote_control_session_info,
                command=apt_install_command)

            apt_install_code, apt_install_data = self.remote_control_paramiko.execute_invoke_shell(
                apt_install_paramiko_vo, service_type, apt_install_service_name)

            apt_install_result_vo = RemoteControlResultVo(
                service_code=apt_install_code,
                service_type=service_type,
                service_func=apt_install_service_func,
                service_name=apt_install_service_name,
                service_validate=(False if apt_install_code != 200 else True),
                service_result=apt_install_data)

            # self.remote_control_working.create(service_type, apt_install_service_name, apt_install_result_vo)

        except KeyError as ex:
            log.error('RemoteControlApt :: apt_install :: ' + str(ex))

        return apt_install_result_vo

    def ufw_stop(self):
        try:
            systemd_stop_meta = self.remote_contorl_systemd_meta['systemd_stop']
            systemd_stop_service_command = systemd_stop_meta['service_command']
            systemd_stop_service_app = 'ufw'

            ufw_stop_command = self.remote_control_paramiko.make_command(
                command=systemd_stop_service_command,
                password=self.remote_control_session_info.password,
                app=systemd_stop_service_app)

            ufw_stop_paramiko_vo: RemoteControlParamikoVo = self.remote_control_paramiko.make_paramiko_vo(
                self.remote_control_session_info,
                command=ufw_stop_command)

            self.remote_control_paramiko.execute_command(ufw_stop_paramiko_vo)

        except KeyError as ex:
            log.error('RemoteControlSystemd :: ufw_stop :: ' + str(ex))

    def ufw_disable(self):
        try:
            systemd_disable_meta = self.remote_contorl_systemd_meta['systemd_disable']
            systemd_disable_command = systemd_disable_meta['service_command']
            systemd_disable_app = 'ufw'

            ufw_disable_command = self.remote_control_paramiko.make_command(
                command=systemd_disable_command,
                password=self.remote_control_session_info.password,
                app=systemd_disable_app)

            ufw_disable_paramiko_vo: RemoteControlParamikoVo = self.remote_control_paramiko.make_paramiko_vo(
                self.remote_control_session_info,
                command=ufw_disable_command)

            self.remote_control_paramiko.execute_command(
                ufw_disable_paramiko_vo)

        except KeyError as ex:
            log.error('RemoteControlSystemd :: ufw_disable :: ' + str(ex))

    def ufw_status(self, service_type: str) -> RemoteControlResultVo:
        ufw_status_result_vo: RemoteControlResultVo

        try:
            systemd_status_meta = self.remote_contorl_systemd_meta['systemd_status']
            systemd_status_service_func = systemd_status_meta['service_func']
            systemd_status_service_command = systemd_status_meta['service_command']
            ufw_status_service_name = 'ufw_status'
            ufw_status_app = 'ufw'

            ufw_status_command = self.remote_control_paramiko.make_command(
                command=systemd_status_service_command,
                password=self.remote_control_session_info.password,
                app=ufw_status_app)

            ufw_status_paramiko_vo: RemoteControlParamikoVo = self.remote_control_paramiko.make_paramiko_vo(
                self.remote_control_session_info,
                command=ufw_status_command)

            ufw_status_code, ufw_status_data = self.remote_control_paramiko.execute_command(
                ufw_status_paramiko_vo)

            ufw_status_result_vo = RemoteControlResultVo(
                service_code=ufw_status_code,
                service_type=service_type,
                service_func=systemd_status_service_func,
                service_name=ufw_status_service_name,
                service_validate='Active: inactive' in ufw_status_data,
                service_result=ufw_status_data)

            self.remote_control_working.create(
                service_type, ufw_status_service_name, ufw_status_data)

        except KeyError as ex:
            log.error('RemoteControlUfw :: ufw_status :: ' + str(ex))

        return ufw_status_result_vo

    def swap_off(self):
        try:
            swap_off_meta = self.remote_control_swap_meta['swap_off']
            swap_off_service_command = swap_off_meta['service_command']

            swap_off_command = self.remote_control_paramiko.make_command(
                command=swap_off_service_command,
                password=self.remote_control_session_info.password)

            swap_off_paramiko_vo: RemoteControlParamikoVo = self.remote_control_paramiko.make_paramiko_vo(
                self.remote_control_session_info,
                command=swap_off_command)

            self.remote_control_paramiko.execute_command(swap_off_paramiko_vo)

        except KeyError as ex:
            log.error('RemoteControlSwap :: swap_off :: ' + str(ex))

    def swap_remove(self):
        try:
            swap_remove_meta = self.remote_control_swap_meta['swap_remove']
            swap_remove_service_command = swap_remove_meta['service_command']

            swap_file_name_code, swap_file_name_data = self.__swap_file_name()

            swap_remove_command = self.remote_control_paramiko.make_command(
                command=swap_remove_service_command,
                password=self.remote_control_session_info.password,
                swap_file_name=swap_file_name_data)

            swap_remove_paramiko_vo: RemoteControlParamikoVo = self.remote_control_paramiko.make_paramiko_vo(
                self.remote_control_session_info,
                command=swap_remove_command)

            self.remote_control_paramiko.execute_command(
                swap_remove_paramiko_vo)

        except KeyError as ex:
            log.error('RemoteControlSwap :: swap_remove :: ' + str(ex))

    def swap_disable(self):
        try:
            swap_disable_meta = self.remote_control_swap_meta['swap_disable']
            swap_disable_meta_service_command = swap_disable_meta['service_command']

            swap_file_name_code, swap_file_name_data = self.__swap_file_name()

            swap_disable_command = self.remote_control_paramiko.make_command(
                command=swap_disable_meta_service_command,
                password=self.remote_control_session_info.password,
                swap_file_name=swap_file_name_data)

            swap_disable_paramiko_vo: RemoteControlParamikoVo = self.remote_control_paramiko.make_paramiko_vo(
                self.remote_control_session_info,
                command=swap_disable_command)

            self.remote_control_paramiko.execute_command(
                swap_disable_paramiko_vo)

        except KeyError as ex:
            log.error('RemoteControlSwap :: swap_disable :: ' + str(ex))

    def swap_validate(self, service_type: str) -> RemoteControlResultVo:
        swap_validate_result_vo: RemoteControlResultVo

        swap_validate_meta = self.remote_control_swap_meta['swap_validate']
        swap_validate_service_func = swap_validate_meta['service_func']
        swap_validate_service_command = swap_validate_meta['service_command']

        swap_validate_service_name = 'swap_validate'

        swap_validate_command = self.remote_control_paramiko.make_command(
            command=swap_validate_service_command,
            password=self.remote_control_session_info.password)

        swap_validate_paramiko_vo: RemoteControlParamikoVo = self.remote_control_paramiko.make_paramiko_vo(
            self.remote_control_session_info,
            command=swap_validate_command)

        swap_validate_code, swap_validate_data = self.remote_control_paramiko.execute_command(
            swap_validate_paramiko_vo)

        swap_validate_result_vo = RemoteControlResultVo(
            service_code=swap_validate_code,
            service_type=service_type,
            service_func=swap_validate_service_func,
            service_name=swap_validate_service_name,
            service_validate=True if not swap_validate_data else False,
            service_result=''
        )

        self.remote_control_working.create(
            service_type, swap_validate_service_name, swap_validate_result_vo)

        return swap_validate_result_vo

    def ip_forward_alter(self):
        try:
            ip_forward_alter_meta = self.remote_control_net_meta['ip_forward_alter']
            ip_forward_alter_service_command = ip_forward_alter_meta['service_command']

            ip_forward_alter_command = self.remote_control_paramiko.make_command(
                command=ip_forward_alter_service_command,
                password=self.remote_control_session_info.password)

            ip_forward_alter_paramiko_vo: RemoteControlParamikoVo = self.remote_control_paramiko.make_paramiko_vo(
                self.remote_control_session_info,
                command=ip_forward_alter_command)

            self.remote_control_paramiko.execute_command(
                ip_forward_alter_paramiko_vo)

        except KeyError as ex:
            log.error('RemoteControlNet :: ip_forward_alter :: ' + str(ex))

    def iptables_modprobe_overlay(self):
        try:
            iptables_modprobe_overlay_meta = self.remote_control_net_meta[
                'iptables_modprobe_overlay']
            iptables_modprobe_overlay_service_command = iptables_modprobe_overlay_meta[
                'service_command']

            iptables_modprobe_overlay_command = self.remote_control_paramiko.make_command(
                command=iptables_modprobe_overlay_service_command,
                password=self.remote_control_session_info.password)

            iptables_modprobe_overlay_paramiko_vo: RemoteControlParamikoVo = self.remote_control_paramiko.make_paramiko_vo(
                self.remote_control_session_info,
                command=iptables_modprobe_overlay_command)

            self.remote_control_paramiko.execute_command(
                iptables_modprobe_overlay_paramiko_vo)

        except KeyError as ex:
            log.error(
                'RemoteControlNet :: iptables_modprobe_overlay :: ' + str(ex))

    def iptables_modprobe_br_netfilter(self):
        try:
            iptables_modprobe_br_netfilter_meta = self.remote_control_net_meta[
                'iptables_modprobe_br_netfilter']
            iptables_modprobe_br_netfilter_service_command = iptables_modprobe_br_netfilter_meta[
                'service_command']

            iptables_modprobe_br_netfilter_command = self.remote_control_paramiko.make_command(
                command=iptables_modprobe_br_netfilter_service_command,
                password=self.remote_control_session_info.password)

            iptables_modprobe_br_netfilter_paramiko_vo: RemoteControlParamikoVo = self.remote_control_paramiko.make_paramiko_vo(
                self.remote_control_session_info,
                command=iptables_modprobe_br_netfilter_command)

            self.remote_control_paramiko.execute_command(
                iptables_modprobe_br_netfilter_paramiko_vo)

        except KeyError as ex:
            log.error(
                'RemoteControlNet :: iptables_modprobe_br_netfilter :: ' + str(ex))

    def iptables_bridge_nf_call_iptables_create(self):
        try:
            iptables_bridge_nf_call_iptables_create_meta = self.remote_control_net_meta[
                'iptables_bridge_nf_call_iptables_create']
            iptables_bridge_nf_call_iptables_create_service_command = iptables_bridge_nf_call_iptables_create_meta[
                'service_command']

            iptables_bridge_nf_call_iptables_create_command = self.remote_control_paramiko.make_command(
                command=iptables_bridge_nf_call_iptables_create_service_command,
                password=self.remote_control_session_info.password)

            iptables_bridge_nf_call_iptables_create_paramiko_vo: RemoteControlParamikoVo = self.remote_control_paramiko.make_paramiko_vo(
                self.remote_control_session_info,
                command=iptables_bridge_nf_call_iptables_create_command)

            self.remote_control_paramiko.execute_command(
                iptables_bridge_nf_call_iptables_create_paramiko_vo)

        except KeyError as ex:
            log.error(
                'RemoteControlNet :: iptables_bridge_nf_call_iptables_create :: ' + str(ex))

    def iptables_k8s_conf_create(self):
        try:
            iptables_k8s_conf_create_meta = self.remote_control_net_meta['iptables_k8s_conf_create']
            iptables_k8s_conf_create_service_command = iptables_k8s_conf_create_meta[
                'service_command']

            iptables_k8s_conf_create_command = self.remote_control_paramiko.make_command(
                command=iptables_k8s_conf_create_service_command,
                password=self.remote_control_session_info.password)

            iptables_k8s_conf_create_paramiko_vo: RemoteControlParamikoVo = self.remote_control_paramiko.make_paramiko_vo(
                self.remote_control_session_info,
                command=iptables_k8s_conf_create_command)

            self.remote_control_paramiko.execute_command(
                iptables_k8s_conf_create_paramiko_vo)

        except KeyError as ex:
            log.error(
                'RemoteControlNet :: iptables_k8s_conf_create :: ' + str(ex))

    def ip_forward_validate(self, service_type: str) -> RemoteControlResultVo:
        try:
            ip_forward_validate_meta = self.remote_control_net_meta['ip_forward_validate']
            ip_forward_validate_service_func = ip_forward_validate_meta['service_func']
            ip_forward_validate_service_command = ip_forward_validate_meta['service_command']

            ip_forward_validate_service_name = 'ip_forward_validate'

            ip_forward_cat_command = self.remote_control_paramiko.make_command(
                command=ip_forward_validate_service_command,
                password=self.remote_control_session_info.password)

            ip_forward_cat_paramiko_vo: RemoteControlParamikoVo = self.remote_control_paramiko.make_paramiko_vo(
                self.remote_control_session_info,
                command=ip_forward_cat_command)

            ip_forward_cat_code, ip_forward_cat_data = self.remote_control_paramiko.execute_command(
                ip_forward_cat_paramiko_vo)

            ip_forward_validate_result_vo = RemoteControlResultVo(
                service_code=ip_forward_cat_code,
                service_type=service_type,
                service_func=ip_forward_validate_service_func,
                service_name=ip_forward_validate_service_name,
                service_validate='1' == ip_forward_cat_data.replace('\n', ''),
                service_result=''
            )

            self.remote_control_working.create(
                service_type, ip_forward_validate_service_name, ip_forward_validate_result_vo)

        except KeyError as ex:
            log.error('RemoteControlNet :: ip_forward_validate :: ' + str(ex))

        return ip_forward_validate_result_vo

    def iptables_bridge_nf_call_iptables_validate(self, service_type: str) -> RemoteControlResultVo:
        iptables_bridge_nf_call_iptables_validate_result_vo: RemoteControlResultVo

        iptables_bridge_nf_call_iptables_validate_code: int
        iptables_bridge_nf_call_iptables_validate_data: str

        try:
            iptables_bridge_nf_call_iptables_validate_meta = self.remote_control_net_meta[
                'iptables_bridge_nf_call_iptables_validate']
            iptables_bridge_nf_call_iptables_validate_service_func = iptables_bridge_nf_call_iptables_validate_meta[
                'service_func']
            iptables_bridge_nf_call_iptables_validate_meta_service_command = iptables_bridge_nf_call_iptables_validate_meta[
                'service_command']

            iptables_bridge_nf_call_iptables_validate_service_name = 'iptables_bridge_nf_call_iptables_validate'

            iptables_bridge_nf_call_iptables_validate_command = self.remote_control_paramiko.make_command(
                command=iptables_bridge_nf_call_iptables_validate_meta_service_command,
                password=self.remote_control_session_info.password)

            iptables_bridge_nf_call_iptables_validate_paramiko_vo: RemoteControlParamikoVo = self.remote_control_paramiko.make_paramiko_vo(
                self.remote_control_session_info,
                command=iptables_bridge_nf_call_iptables_validate_command)

            iptables_bridge_nf_call_iptables_validate_code, iptables_bridge_nf_call_iptables_validate_data = \
                self.remote_control_paramiko.execute_command(
                    iptables_bridge_nf_call_iptables_validate_paramiko_vo)

            iptables_bridge_nf_call_iptables_validate_result_vo = RemoteControlResultVo(
                service_code=iptables_bridge_nf_call_iptables_validate_code,
                service_type=service_type,
                service_func=iptables_bridge_nf_call_iptables_validate_service_func,
                service_name=iptables_bridge_nf_call_iptables_validate_service_name,
                service_validate=iptables_bridge_nf_call_iptables_validate_data.replace(
                    '\n', '') == '1',
                service_result=''
            )

            self.remote_control_working.create(
                service_type, iptables_bridge_nf_call_iptables_validate_service_name, iptables_bridge_nf_call_iptables_validate_result_vo)

        except KeyError as ex:
            log.error(
                'RemoteControlNet :: iptables_bridge_nf_call_iptables_validate :: ' + str(ex))

        return iptables_bridge_nf_call_iptables_validate_result_vo

    def iptables_k8s_conf_validate(self, service_type: str) -> RemoteControlResultVo:
        try:
            iptables_k8s_conf_validate_meta = self.remote_control_net_meta[
                'iptables_k8s_conf_validate']
            iptables_k8s_conf_validate_service_func = iptables_k8s_conf_validate_meta[
                'service_func']
            iptables_k8s_conf_validate_service_command = iptables_k8s_conf_validate_meta[
                'service_command']

            iptables_k8s_conf_validate_service_name = 'iptables_k8s_conf_validate'

            iptables_k8s_conf_validate_command = self.remote_control_paramiko.make_command(
                command=iptables_k8s_conf_validate_service_command,
                password=self.remote_control_session_info.password)

            iptables_k8s_conf_validate_paramiko_vo: RemoteControlParamikoVo = self.remote_control_paramiko.make_paramiko_vo(
                self.remote_control_session_info,
                command=iptables_k8s_conf_validate_command)

            iptables_k8s_conf_validate_code, iptables_k8s_conf_validate_data = \
                self.remote_control_paramiko.execute_command(
                    iptables_k8s_conf_validate_paramiko_vo)

            iptables_k8s_conf_validate_lines = iptables_k8s_conf_validate_data.split('\n')[
                :-1]

            iptables_k8s_conf_validate_result_vo = RemoteControlResultVo(
                service_code=iptables_k8s_conf_validate_code,
                service_type=service_type,
                service_func=iptables_k8s_conf_validate_service_func,
                service_name=iptables_k8s_conf_validate_service_name,
                service_validate=len(iptables_k8s_conf_validate_lines) == 3,
                service_result=''
            )

            self.remote_control_working.create(
                service_type, iptables_k8s_conf_validate_service_name, iptables_k8s_conf_validate_result_vo)

        except KeyError as ex:
            log.error(
                'RemoteControlNet :: iptables_k8s_conf_validate :: ' + str(ex))

        return iptables_k8s_conf_validate_result_vo
