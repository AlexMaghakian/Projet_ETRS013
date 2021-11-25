## author MAGHAKIAN Alex
from spyne.model.primitive.string import String
from spyne.server.wsgi import WsgiApplication
from spyne.protocol.soap import Soap11
from spyne.service import ServiceBase
from spyne.application import Application
from spyne.decorator import rpc
from spyne.model.primitive import Integer, Unicode
from spyne.model.complex import Iterable
from wsgiref.simple_server import make_server
from config import *

class service(ServiceBase):
    @rpc(String, String, Integer, _returns=String)
    def infos(ctx, destination, departure, mileage):
        return trajectory(destination, departure, mileage)

    @rpc(Integer, Integer,Integer,  _returns=Iterable(Integer))
    def time_calculation (time,distance, autonomie, temps_rechargement):
        return duration()
application = Application(
    [service],
    'spyne.examples.hello.soap',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)
wsgi_application = WsgiApplication(application)

server = make_server('127.0.0.1', 8080, wsgi_application)
server.serve_forever()