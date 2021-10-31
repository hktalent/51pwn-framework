from frwk_51pwn.lib.controller.controller import start
from frwk_51pwn.lib.core.common import (encoder_bash_payload,
                                       encoder_powershell_payload,
                                       get_host_ipv6, single_time_warn_message)
from frwk_51pwn.lib.core.data import conf, kb, logger, paths
from frwk_51pwn.lib.core.datatype import AttribDict
from frwk_51pwn.lib.core.enums import PLUGIN_TYPE, POC_CATEGORY, VUL_TYPE
from frwk_51pwn.lib.core.interpreter_option import (OptBool, OptDict, OptFloat,
                                                   OptInteger, OptIP, OptItems,
                                                   OptPort, OptString)
from frwk_51pwn.lib.core.option import init, init_options
from frwk_51pwn.lib.core.plugin import PluginBase, register_plugin
from frwk_51pwn.lib.core.poc import Output, POCBase
from frwk_51pwn.lib.core.register import (load_file_to_module,
                                         load_string_to_module, register_poc)
from frwk_51pwn.lib.core.settings import DEFAULT_LISTENER_PORT
from frwk_51pwn.lib.request import requests
from frwk_51pwn.lib.utils import (generate_shellcode_list, get_middle_text,
                                 random_str)
from frwk_51pwn.modules.censys import Censys
from frwk_51pwn.modules.ceye import CEye
from frwk_51pwn.modules.fofa import Fofa
from frwk_51pwn.modules.httpserver import PHTTPServer
from frwk_51pwn.modules.listener import (REVERSE_PAYLOAD, bind_shell,
                                        bind_tcp_shell, bind_telnet_shell)
from frwk_51pwn.modules.quake import Quake
from frwk_51pwn.modules.seebug import Seebug
from frwk_51pwn.modules.shodan import Shodan
from frwk_51pwn.modules.spider import crawl
from frwk_51pwn.modules.zoomeye import ZoomEye
from frwk_51pwn.shellcodes import OSShellcodes, WebShell

__all__ = ('requests', 'PluginBase', 'register_plugin', 'PLUGIN_TYPE',
           'POCBase', 'Output', 'AttribDict', 'POC_CATEGORY', 'VUL_TYPE',
           'register_poc', 'conf', 'kb', 'logger', 'paths',
           'DEFAULT_LISTENER_PORT', 'load_file_to_module',
           'load_string_to_module', 'single_time_warn_message', 'CEye',
           'Seebug', 'ZoomEye', 'Shodan', 'Fofa', 'Quake', 'Censys',
           'PHTTPServer', 'REVERSE_PAYLOAD', 'get_listener_ip',
           'get_listener_port', 'get_results', 'init_frwk_51pwn',
           'start_frwk_51pwn', 'get_poc_options', 'crawl', 'OSShellcodes',
           'WebShell', 'OptDict', 'OptIP', 'OptPort', 'OptBool', 'OptInteger',
           'OptFloat', 'OptString', 'OptItems', 'get_middle_text',
           'generate_shellcode_list', 'random_str', 'encoder_bash_payload',
           'encoder_powershell_payload', 'get_host_ipv6', 'bind_shell',
           'bind_tcp_shell', 'bind_telnet_shell')


def get_listener_ip():
    return conf.connect_back_host


def get_listener_port():
    return conf.connect_back_port


def get_current_poc_obj():
    pass


def get_poc_options(poc_obj=None):
    poc_obj = poc_obj or kb.current_poc
    return poc_obj.get_options()


def get_results():
    return kb.results


def init_frwk_51pwn(options={}):
    init_options(options)
    init()


def start_frwk_51pwn():
    start()
