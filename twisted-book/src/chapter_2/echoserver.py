from twisted.internet import reactor, protocol


class Echo(protocol.Protocol):
    def dataReceived(self, data):
        self.transport.write(data)


class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()


reactor.listenTCP(8000, EchoFactory())
reactor.run()
