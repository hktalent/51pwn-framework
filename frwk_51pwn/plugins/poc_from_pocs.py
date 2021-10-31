# load poc from pocs directories
import os

from frwk_51pwn.api import PLUGIN_TYPE
from frwk_51pwn.api import PluginBase
from frwk_51pwn.api import logger
from frwk_51pwn.api import paths
from frwk_51pwn.api import register_plugin


class PocFromPocs(PluginBase):
    category = PLUGIN_TYPE.POCS

    def init(self):
        _pocs = []
        for root, dirs, files in os.walk(paths.POCSUITE_POCS_PATH):
            files = filter(lambda x: not x.startswith("__") and x.endswith(".py"), files)
            _pocs.extend(map(lambda x: os.path.join(root, x), files))
        for f in _pocs:

            if self.add_poc_from_file(f):
                info_msg = "[PLUGIN] load PoC script '{0}' from pocs directories success".format(f)
            else:
                info_msg = "[PLUGIN] load PoC script '{0}' from pocs directories failed".format(f)
            logger.info(info_msg)


register_plugin(PocFromPocs)
