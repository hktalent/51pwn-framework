from frwk_51pwn.api import PluginBase
from frwk_51pwn.api import PLUGIN_TYPE
from frwk_51pwn.api import logger
from frwk_51pwn.api import conf
from frwk_51pwn.api import Quake
from frwk_51pwn.api import register_plugin
from frwk_51pwn.api import kb
from frwk_51pwn.lib.core.exception import frwk_51pwnPluginDorkException


class TargetFromQuake(PluginBase):
    category = PLUGIN_TYPE.TARGETS

    def init_quake_api(self):
        self.quake = Quake(token=conf.quake_token)

    def init(self):
        self.init_quake_api()
        dork = None
        if conf.dork_quake:
            dork = conf.dork_quake
        else:
            dork = conf.dork
        if not dork:
            msg = "Need to set up dork (please --dork or --dork-quake)"
            raise frwk_51pwnPluginDorkException(msg)
        if conf.dork_b64:
            import base64
            dork = str(base64.b64decode(dork), encoding="utf-8")

        if kb.comparison:
            kb.comparison.add_dork("Quake", dork)
        info_msg = "[PLUGIN] try fetch targets from Quake with dork: {0}".format(
            dork)
        logger.info(info_msg)
        targets = self.quake.search(dork, conf.max_page)
        count = 0
        if targets:
            for target in targets:
                if kb.comparison:
                    kb.comparison.add_ip(target, "Quake")
                if self.add_target(target):
                    count += 1

        info_msg = "[PLUGIN] get {0} target(s) from Quake".format(count)
        logger.info(info_msg)


register_plugin(TargetFromQuake)
