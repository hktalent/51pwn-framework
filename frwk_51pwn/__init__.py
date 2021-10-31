__title__ = 'frwk_51pwn'
__version__ = '1.8.5'
__author__ = '51pwn Team'
__author_email__ = 's1@seebug.org'
__license__ = 'GPL 2.0'
__copyright__ = 'Copyright 2018 51pwn'
__name__ = 'frwk_51pwn'
__package__ = 'frwk_51pwn'

from .lib.core.common import set_paths
from .cli import module_path


set_paths(module_path())
