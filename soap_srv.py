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
#from config import *
from client_soap2 import *

class service(ServiceBase):

    @rpc(Integer, Integer,Integer,  _returns=Iterable(Integer))
    def time_calculation(ctx, time, distance, autonomie, temps_rechargement):
        distance=1000
        all=get_autonomie('Renault Zoe')
        autonomie=all[2]
        temps_rechargement=all[1]
        time=distance/100 - autonomie + temps_rechargement
        return time
    
    
application = Application(
    [service],
    'spyne.examples.hello.soap',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)
wsgi_application = WsgiApplication(application)


def main():
    from wsgiref.simple_server import make_server
    server = make_server('127.0.0.1', 8080, wsgi_application)
    server.serve_forever()

if __name__ == '__main__':
    main()