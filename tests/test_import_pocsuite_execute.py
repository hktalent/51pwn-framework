import unittest
from frwk_51pwn.api import init_frwk_51pwn
from frwk_51pwn.api import start_frwk_51pwn
from frwk_51pwn.api import get_results


class TestCase(unittest.TestCase):
    def setUp(self):
        self.config = {
            'url': 'http://127.0.0.1:8080',
            'poc': 'ecshop_rce',
        }
        init_frwk_51pwn(self.config)

    def tearDown(self):
        pass

    def verify_result(self):
        result = get_results().pop()
        self.assertTrue(result[5] == 'success')

    @unittest.skip(reason='test')
    def test_import_run(self):
        start_frwk_51pwn()
        self.verify_result()
