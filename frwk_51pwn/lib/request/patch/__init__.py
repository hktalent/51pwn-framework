import urllib3

from frwk_51pwn.lib.core.exception import frwk_51pwnIncompleteRead
from .remove_ssl_verify import remove_ssl_verify
from .remove_warnings import disable_warnings
from .hook_request import patch_session
from .add_httpraw import patch_addraw
from .hook_request_redirect import patch_redirect


def patch_all():
    urllib3.response.HTTPResponse._update_chunk_length = _update_chunk_length
    disable_warnings()
    remove_ssl_verify()
    patch_session()
    patch_addraw()
    patch_redirect()


def _update_chunk_length(self):
    # First, we'll figure out length of a chunk and then
    # we'll try to read it from socket.
    # Fix some chunked errors that urllib3 does not recognize
    if self.chunk_left is not None:
        return
    line = self._fp.fp.readline()
    line = line.split(b";", 1)[0]
    if not line:
        self.chunk_left = 0
        return
    try:
        self.chunk_left = int(line, 16)
    except ValueError:
        # Invalid chunked protocol response, abort.
        self.close()
        raise frwk_51pwnIncompleteRead(line)
