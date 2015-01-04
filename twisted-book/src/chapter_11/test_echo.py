from twisted.test import proto_helpers
from twisted.trial import unittest

from echo import EchoFactory


class EchoServerTestCase(unittest.TestCase):
    def test_echo(self):
        factory = EchoFactory()

        # 1. Build a protocol instance
        self.proto = factory.buildProtocol(("localhost", 0))

        # 2. Giving it a mock transport
        self.transport = proto_helpers.StringTransport()

        # 3. Faking client communication
        self.proto.makeConnection(self.transport)
        self.proto.dataReceived("test\r\n")

        # 4. Inspecting the mocked transport data
        self.assertEqual(self.transport.value(), "test\r\n")
