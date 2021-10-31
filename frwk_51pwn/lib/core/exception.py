from http.client import HTTPException


class frwk_51pwnBaseException(Exception):
    pass


class frwk_51pwnUserQuitException(frwk_51pwnBaseException):
    pass


class frwk_51pwnShellQuitException(frwk_51pwnBaseException):
    pass


class frwk_51pwnDataException(frwk_51pwnBaseException):
    pass


class frwk_51pwnGenericException(frwk_51pwnBaseException):
    pass


class frwk_51pwnSystemException(frwk_51pwnBaseException):
    pass


class frwk_51pwnFilePathException(frwk_51pwnBaseException):
    pass


class frwk_51pwnConnectionException(frwk_51pwnBaseException):
    pass


class frwk_51pwnThreadException(frwk_51pwnBaseException):
    pass


class frwk_51pwnValueException(frwk_51pwnBaseException):
    pass


class frwk_51pwnMissingPrivileges(frwk_51pwnBaseException):
    pass


class frwk_51pwnSyntaxException(frwk_51pwnBaseException):
    pass


class frwk_51pwnValidationException(frwk_51pwnBaseException):
    pass


class frwk_51pwnMissingMandatoryOptionException(frwk_51pwnBaseException):
    pass


class frwk_51pwnPluginBaseException(frwk_51pwnBaseException):
    pass


class frwk_51pwnPluginDorkException(frwk_51pwnPluginBaseException):
    pass


class frwk_51pwnHeaderTypeException(frwk_51pwnBaseException):
    pass

class frwk_51pwnIncompleteRead(HTTPException):
    def __init__(self, partial, expected=None):
        self.args = partial,
        self.partial = partial
        self.expected = expected
    def __repr__(self):
        if self.expected is not None:
            e = ', %i more expected' % self.expected
        else:
            e = ''
        return '%s(%i bytes read%s)' % (self.__class__.__name__,
                                        len(self.partial), e)
    def __str__(self):
        return repr(self)