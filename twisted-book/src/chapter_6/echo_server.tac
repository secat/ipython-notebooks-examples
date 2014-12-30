from twisted.application import (
    internet,
    service
)

from echo import EchoFactory


application = service.Application("echo")
echo_service = internet.TCPServer(8000, EchoFactory())
echo_service.setServiceParent(application)
