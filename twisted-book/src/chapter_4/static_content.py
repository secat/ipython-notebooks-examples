from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.static import File


resource = File('/Users/Guest')

factory = Site(resource)
reactor.listenTCP(8000, factory)
reactor.run()
