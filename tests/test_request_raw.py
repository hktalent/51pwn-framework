import unittest
from frwk_51pwn.api import requests, init_frwk_51pwn


class TestCase(unittest.TestCase):
    def setUp(self):
        init_frwk_51pwn()

    def tearDown(self):
        pass

    def test_get(self):
        raw = '''
        GET /get?a=1&b=2 HTTP/1.1
        Host: httpbin.org
        Connection: keep-alive
        Upgrade-Insecure-Requests: 1
        User-Agent: frwk_51pwn v3.0
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
        Accept-Encoding: gzip, deflate
        Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
        Cookie: _gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1
        '''
        r = requests.httpraw(raw)
        self.assertTrue(r.json()['args'] == {'a': '1', 'b': '2'})

    def test_post(self):
        raw = '''
        POST /post HTTP/1.1
        Host: httpbin.org
        Connection: keep-alive
        Upgrade-Insecure-Requests: 1
        User-Agent: frwk_51pwn v3.0
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
        Accept-Encoding: gzip, deflate
        Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
        Cookie: _gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1
            
        a=1&b=2
        '''
        r = requests.httpraw(raw)
        self.assertTrue(r.json()['data'] == 'a=1&b=2')

    def test_json(self):
        raw = '''
        POST /post HTTP/1.1
        Host: httpbin.org
        Connection: keep-alive
        Upgrade-Insecure-Requests: 1
        User-Agent: frwk_51pwn v3.0
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
        Accept-Encoding: gzip, deflate
        Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
        Cookie: _gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1
        
        {"frwk_51pwn":"v3.0"}
        '''
        r = requests.httpraw(raw)
        self.assertTrue(r.json()['json'] == '{"frwk_51pwn":"v3.0"}')
