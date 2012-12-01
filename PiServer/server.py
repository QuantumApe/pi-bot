import socket

class server(object):
  """This class creates a quick TCP server"""
  def __init(self):
    pass
  
  def setup(self, PORT, MaxConnections):
    """ This function sets up the TCP server at a port"""
    ADDR=('',PORT)
    instance=socket.socket( socket.AF_INET, socket.SOCK_STREAM )    
    instance.bind((ADDR))
    instance.listen(MaxConnections)
    print 'listening'
    return instance   