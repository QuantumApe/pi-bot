import os

class GPIO(object):
  """A simple test class for GPIO pins on the rasberry pi"""

  def __init(self):
    pass

  def setup(self,pin,direction):
    """Setup a pin with a particular direction"""
    pin=str(pin)
    direction=str(direction)

    #If the pin hasn't been exported yet, export it
    if os.path.exists('/sys/class/gpio/gpio%s'%pin) == 0:
      with open('/sys/class/gpio/export', 'w') as f:
        f.write(pin)
    with open('/sys/class/gpio/gpio%s/direction'%pin, 'w') as f:
      f.write(direction)

  def clean(self,pin):
    """ unexport a pin from the system"""
    pin=str(pin)
    if os.path.exists('/sys/class/gpio/gpio%s'%pin):
      with open('/sys/class/gpio/unexport', 'w') as f:
        f.write(pin)


  def write(self, pin, value):
    """Write a value to pin"""
    pin=str(pin)
    value=str(value)
   # value = '1' if value else '0'
    with open('/sys/class/gpio/gpio%s/value'%pin, 'w') as f:
      f.write(value)