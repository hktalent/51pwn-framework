#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/25 morning 10:49
# @Author  : chenghs
# @File    : console.py
import os
import sys

try:
    import frwk_51pwn
except ImportError:
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from frwk_51pwn.cli import check_environment, module_path
from frwk_51pwn import set_paths
from frwk_51pwn.lib.core.interpreter import frwk_51pwnInterpreter
from frwk_51pwn.lib.core.option import init_options


def main():
    check_environment()
    set_paths(module_path())
    init_options()
    poc = frwk_51pwnInterpreter()
    poc.start()


if __name__ == '__main__':
    main()
