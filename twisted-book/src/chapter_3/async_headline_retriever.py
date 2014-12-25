from twisted.internet import (
    defer,
    reactor
)
from twisted.python.failure import DefaultException


class HeadlineRetriever(object):
    def process_headline(self, headline):
        if len(headline) > 50:
            self.d.errback(
                DefaultException(
                    "The headline '{}' is too long".format(headline)
                )
            )
        else:
            self.d.callback(headline)

    def _to_html(self, result):
        return "<h1>{}<h1>".format(result)

    def get_headline(self, in_data):
        self.d = defer.Deferred()
        reactor.callLater(1, self.process_headline, in_data)
        self.d.addCallback(self._to_html)

        return self.d


def print_data(result):
    print(result)
    reactor.stop()


def print_error(result):
    print(result)
    reactor.stop()
