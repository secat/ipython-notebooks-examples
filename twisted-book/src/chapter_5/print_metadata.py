import sys

from twisted.internet import reactor
from twisted.web.client import Agent
from twisted.web.http_headers import Headers


def printHeaders(response):
    print('HTTP version: {}'.format(response.version))
    print('Status Code: {}'.format(response.code))
    print('Status phrase: {}'.format(response.phrase))

    print('Response headers:')
    for header, value in response.headers.getAllRawHeaders():
        print('{} {}'.format(header, value))


def printError(failure):
    print >> sys.stderr, failure


def stop(result):
    reactor.stop()


if len(sys.argv) != 2:
    print >> sys.stderr, "Usage: python print_metadata.py <URL>"
    sys.exit(1)

agent = Agent(reactor)

headers = Headers({
    'User-Agent': ['Twisted WebBot'],
    'Content-Type': ['text/x-greeting']
})

d = agent.request('HEAD', sys.argv[1], headers=headers)
d.addCallbacks(printHeaders, printError)
d.addBoth(stop)

reactor.run()
