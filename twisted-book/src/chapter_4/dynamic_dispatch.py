from calendar import calendar

from twisted.internet import reactor
from twisted.web.resource import (
    NoResource,
    Resource
)
from twisted.web.server import Site


class YearPage(Resource):
    def __init__(self, year):
        Resource.__init__(self)
        self.year = year

    def render_GET(self, request):
        return "<html><body><pre>{}</pre></body></html>".format(
            calendar(self.year))


class CalendarHome(Resource):
    def getChild(self, name, request):
        if name == '':
            return self
        elif name.isdigit():
            return YearPage(int(name))
        else:
            return NoResource()

    def render_GET(self, request):
        return "<html><body>Welcome to the calendar server!</body></html>"


root = CalendarHome()
factory = Site(root)

reactor.listenTCP(8000, factory)
reactor.run()
