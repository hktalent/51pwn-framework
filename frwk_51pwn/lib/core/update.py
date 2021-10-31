import sys
import time
import os
import re
import subprocess
from frwk_51pwn.lib.core.common import data_to_stdout
from frwk_51pwn.lib.core.common import get_latest_revision
from frwk_51pwn.lib.core.common import poll_process
from frwk_51pwn.lib.core.data import conf
from frwk_51pwn.lib.core.data import logger
from frwk_51pwn.lib.core.data import paths
from frwk_51pwn.lib.core.revision import get_revision_number
from frwk_51pwn.lib.core.settings import GIT_REPOSITORY
from frwk_51pwn.lib.core.settings import IS_WIN
from frwk_51pwn.lib.core.settings import UNICODE_ENCODING
from frwk_51pwn.lib.core.settings import VERSION


def update():
    if not conf.update_all:
        return
    success = False
    if not os.path.exists(os.path.join(paths.POCSUITE_ROOT_PATH, "../", ".git")):
        warn_msg = "not a git repository. It is recommended to clone the 'hktalent/51pwn-framework' repository "
        warn_msg += "from GitHub (e.g. 'git clone --depth 1 {} frwk_51pwn')".format(GIT_REPOSITORY)
        logger.warn(warn_msg)
        if VERSION == get_latest_revision():
            logger.info("already at the latest revision '{}'".format(get_revision_number()))
            return
    else:
        info_msg = "updating frwk_51pwn to the latest development revision from the "
        info_msg += "GitHub repository"
        logger.info(info_msg)
        debug_msg = "frwk_51pwn will try to update itself using 'git' command"
        logger.debug(debug_msg)
        data_to_stdout("\r[{0}] [INFO] update in progress ".format(time.strftime("%X")))
        cwd_path = os.path.join(paths.POCSUITE_ROOT_PATH, "../")
        try:
            process = subprocess.Popen("git checkout . && git pull %s HEAD" % GIT_REPOSITORY,
                                       shell=True,
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       cwd=cwd_path.encode(
                                           sys.getfilesystemencoding() or UNICODE_ENCODING))
            poll_process(process, True)
            stdout, stderr = process.communicate()
            success = not process.returncode
        except (IOError, OSError) as ex:
            success = False
            stderr = str(ex)
        if success:
            logger.info("{0} the latest revision '{1}'".format("already at" if b"Already" in stdout else "updated to",
                                                               get_revision_number()))
        else:
            if "Not a git repository" in stderr:
                err_msg = "not a valid git repository. Please checkout the 'hktalent/51pwn-framework' repository "
                err_msg += "from GitHub (e.g. 'git clone --depth 1 %s frwk_51pwn')" % GIT_REPOSITORY
                logger.error(err_msg)
            else:
                logger.error("update could not be completed ('%s')" % re.sub(r"\W+", " ", stderr).strip())
    if not success:
        if IS_WIN:
            info_msg = "for Windows platform it's recommended "
            info_msg += "to use a GitHub for Windows client for updating "
            info_msg += "purposes (http://windows.github.com/) or just "
            info_msg += "download the latest snapshot from "
            info_msg += "https://github.com/51pwn-framework/frwk_51pwn/downloads"
        else:
            info_msg = "for Linux platform it's recommended "
            info_msg += "to install a standard 'git' package (e.g.: 'sudo apt-get install git')"
        logger.info(info_msg)
    sys.exit()
