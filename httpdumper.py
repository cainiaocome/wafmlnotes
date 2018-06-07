#!/usr/bin/env python

'''
    pydoc mitmproxy.http

    howto example:
    
    mitmdump --listen-host 127.0.0.1 --listen-port 8000 -s httpdumper.py
'''

import json
from mitmproxy import ctx

f = open('dumpresult.txt', 'w')

class Counter:
    def __init__(self):
        self.num = 0

    def request(self, flow):
        self.num = self.num + 1
        ctx.log.info("We've seen %d flows" % self.num)

        print(flow.request.url)
        data = {
            'url':flow.request.url,
            'method':flow.request.method,
            'host':flow.request.host,
        }
        f.write(json.dumps(data)+'\n')
        f.flush()

addons = [
    Counter()
]
