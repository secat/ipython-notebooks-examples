from twisted.internet import (
    protocol,
    reactor
)


class EchoProcessProtocol(protocol.ProcessProtocol):
    def connectionMade(self):
        print("connectionMade called")
        reactor.callLater(10, self.terminateProcess)

    def terminateProcess(self):
        self.transport.signalProcess('TERM')

    def outReceived(self, data):
        print(
            "outReceived called with {} bytes of data: \n{}".format(
                len(data), data)
        )

    def errReceived(self, data):
        print(
            "errReceived called with {} bytes of data: \n{}".format(
                len(data), data)
        )

    def inConnectionLost(self):
        print("inConnectionLost called, stdin closed.")

    def outConnectionLost(self):
        print("outConnectionLost called, stdout closed.")

    def errConnectionLost(self):
        print("errConnectionLost called, stderr closed.")

    def processExited(self, reason):
        print(
            "processExited called with status {}".format(
                reason.value.exitCode)
        )

    def processEnded(self, reason):
        print(
            "processEnded called with status {}".format(
                reason.value.exitCode)
        )
        print(
            "All FDs are now closed, and the process has been reaped"
        )

        reactor.stop()


pp = EchoProcessProtocol()

command_and_args = ["twistd", "-ny", "echo_server.tac"]

reactor.spawnProcess(pp, command_and_args[0], args=command_and_args)
reactor.run()
