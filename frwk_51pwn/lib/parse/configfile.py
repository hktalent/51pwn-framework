import os
from configparser import ConfigParser

from frwk_51pwn.lib.core.data import logger, cmd_line_options, conf
from frwk_51pwn.lib.core.enums import OPTION_TYPE
from frwk_51pwn.lib.core.exception import frwk_51pwnFilePathException, frwk_51pwnMissingMandatoryOptionException, \
    frwk_51pwnValueException
from frwk_51pwn.lib.core.optiondict import optDict


def config_file_parser(configFile):
    """
    Parse configuration file and save settings into the configuration
    advanced dictionary.
    """

    # global config

    debugMsg = "parsing configuration file"
    logger.debug(debugMsg)

    if not os.path.isfile(configFile):
        raise frwk_51pwnFilePathException("file '{}' don't exist".format(configFile))

    config = ConfigParser()
    config.read(configFile, encoding='utf-8')

    if not config.has_section("Target"):
        errMsg = "missing a mandatory section 'Target' in the configuration file"
        raise frwk_51pwnMissingMandatoryOptionException(errMsg)

    sections = config.sections()
    for section in sections:
        options = config.options(section)
        if options:
            for option in options:
                datatype = "string"
                try:
                    datatype = optDict[section][option]
                except KeyError:
                    pass

                try:
                    if datatype == OPTION_TYPE.BOOLEAN:
                        value = config.getboolean(section, option) if config.get(section, option) else False
                    elif datatype == OPTION_TYPE.INTEGER:
                        value = config.getint(section, option) if config.get(section, option) else 0
                    elif datatype == OPTION_TYPE.FLOAT:
                        value = config.getfloat(section, option) if config.get(section, option) else 0.0
                    else:
                        value = config.get(section, option)
                except ValueError as ex:
                    errMsg = "error occurred while processing the option "
                    errMsg += "'%s' in provided configuration file ('%s')" % (option, ex)
                    raise frwk_51pwnValueException(errMsg)

                if value:
                    conf[option] = value
