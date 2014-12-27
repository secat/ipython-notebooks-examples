import time

from twisted.internet import reactor
from twisted.web.resource import Resource
from twisted.web.server import Site


class ClockPage(Resource):
    isLeaf = True

    def render_GET(self, request):
        return "The local time is {}".format(time.ctime())


resource = ClockPage()
factory = Site(resource)

reactor.listenTCP(8000, factory)
reactor.run()
