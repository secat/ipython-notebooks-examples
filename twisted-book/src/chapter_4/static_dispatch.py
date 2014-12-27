from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.static import File


root = File('/Users/Guest')
root.putChild('doc', File('/usr/share/doc/bash'))
root.putChild('logs', File('/var/log'))

factory = Site(root)
reactor.listenTCP(8000, factory)
reactor.run()
