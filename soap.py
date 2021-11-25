# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 10:20:59 2021

@author: Alex
"""

# service SOAP à développer pour calculer le temps de parcours en fonction du
#nombre de kilomètres à parcourir et en tenant compte du temps de chargement. 

from spyne import Application, rpc, ServiceBase, Unicode, Integer, Iterable
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class HelloWorldService(ServiceBase):               
    @rpc(Integer, Integer, _returns=Iterable(Integer))
    def time_calculation (time,d, v): 
        time=d/v
        yield time

application = Application([HelloWorldService], 'spyne.examples.hello.soap',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())
wsgi_application = WsgiApplication(application)



def main():
    from wsgiref.simple_server import make_server
    server = make_server('127.0.0.1', 8000, wsgi_application)
    server.serve_forever()

if __name__ == '__main__':
    main()