#!/usr/bin/python

from Subfact_ina219 import INA219
from time import sleep

ina = INA219()
result = ina.getBusVoltage_V()

mamps = ("%.3f" % ina.getCurrent_mA())
amps = (float(mamps) / 1000)



try:
   while True:
      print(chr(27) + "[2J")
      mvolts = ina.getShuntVoltage_mV()
      volts = ina.getBusVoltage_V()
      mamps = ina.getCurrent_mA()
      amps = (float("%.5f"%mamps) / 1000)
      print "Shunt   : %.3f mV" % mvolts
      print "Bus     : %.3f V" % volts
      print "Current : %.3f A" % amps
      #print "Current : %.3f mA" % float(mamps)


      sleep(1)

except KeyboardInterrupt:
    print "Measurement stopped by user"




