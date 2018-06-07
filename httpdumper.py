#!/usr/bin/env python

'''
    pydoc mitmproxy.http
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
        f.write(flow.request.url+'\n')
        f.flush()

addons = [
    Counter()
]
