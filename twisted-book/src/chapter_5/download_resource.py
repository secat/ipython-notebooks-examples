import sys

from twisted.internet import reactor
from twisted.web.client import downloadPage


def printError(failure):
    print >> sys.stderr, failure


def stop(result):
    reactor.stop()


if len(sys.argv) != 3:
    print >> sys.stderr, "Usage: python print_resource.py <URL> <output file>"
    sys.exit(1)

d = downloadPage(sys.argv[1], sys.argv[2])
d.addErrback(printError)
d.addBoth(stop)

reactor.run()
