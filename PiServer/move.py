from GPIO import * #get the GPIO control for the PI



class move(object):
  """ This class drives the robot around given the pin numbers it's connected to"""
  def __init(self,RF,RR,LF,LR):
    pass   
    
  def setup(self,RF,RR,LF,LR):
    """This will set up the GPIO pins to move the robot"""
    self.RF=RF
    self.RR=RR
    self.LF=LF
    self.LR=LR
    
    OUT='out'
    IN='in'
    self.pins = GPIO()
    self.pins.setup(self.RF, OUT)
    self.pins.setup(self.RR, OUT)
    self.pins.setup(self.LF, OUT)
    self.pins.setup(self.LR, OUT) 

  def forward(self):
    """Turns pins on to move forward"""
    self.stop()
    self.pins.write(self.RF,1)
    self.pins.write(self.RR,0)
    self.pins.write(self.LF,1)
    self.pins.write(self.LR,0)
    
  def reverse(self):
    """Turns pins on to move backward"""
    self.stop()
    self.pins.write(self.RF,0)
    self.pins.write(self.RR,1)
    self.pins.write(self.LF,0)
    self.pins.write(self.LR,1)
    
  def right(self):
    """Turns pins to pivot right"""
    self.stop()
    self.pins.write(self.RF,0)
    self.pins.write(self.RR,1)
    self.pins.write(self.LF,1)
    self.pins.write(self.LR,0)

  def left(self):
    """Turns pins to pivot left"""
    self.stop()
    self.pins.write(self.RF,1)
    self.pins.write(self.RR,0)
    self.pins.write(self.LF,0)
    self.pins.write(self.LR,1)
    
  def stop(self):
    """Turns all pins off to stop"""
    self.pins.write(self.RF,0)
    self.pins.write(self.RR,0)
    self.pins.write(self.LF,0)
    self.pins.write(self.LR,0)    

  def dispatch(self):
    """Unexport all pins used"""
    self.pins.clean(self.RF)
    self.pins.clean(self.RR)
    self.pins.clean(self.LF)
    self.pins.clean(self.LR)