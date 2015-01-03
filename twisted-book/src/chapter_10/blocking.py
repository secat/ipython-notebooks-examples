import time

from twisted.internet import (
    reactor,
    threads
)
from twisted.internet.task import LoopingCall


def blockingApiCall(arg):
    time.sleep(1)
    return arg


def nonBlockingCall(arg):
    print(arg)


def printResult(result):
    print(result)


def finish():
    reactor.stop()

d = threads.deferToThread(blockingApiCall, "Goose")
d.addCallback(printResult)

LoopingCall(nonBlockingCall, "Duck").start(.25)

reactor.callLater(2, finish)
reactor.run()
