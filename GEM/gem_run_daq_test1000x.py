#!/usr/bin/python2.7

import sys,os,time
from os import system
from daqconf import BeamDaqConfiguration, AsyncRunner
from pydaq import RemoteDaq
from pydaq import TestbeamGemDaq

EVENT_COUNT=1000 #65*1000 # Can read only up to 65535 events for now.

def Speak(msg):
    os.system("ssh -Tf beam-daq 'espeak -a 250 -v m7 \"%s\"'  >/dev/null 2>&1" % [msg])


conf = BeamDaqConfiguration()

#run=False
run=True

enabled_systems = set("tb-gem lecroy".split())
#enabled_systems = set("tb-gem calo".split())
print("Enabled systems: %s" % str(enabled_systems))

#NOTE: daq now prints little to no data per event
#Enable this for verbose event printing
#Watch deadtime if you do so.
if 1:
	conf.gemDaq.setPrintEvents(True)
	conf.lecroy2249.setPrintEvents(False)
	conf.daq.eventWritePrintInterval(1)


#These settings have default values in BeamDaqConfiguration

# 1 - cntTarget, 2 - cntOut, 4 - cntCalo, 8 - calo (not use 8 - phase, 16 - generator <-> LSO)
#conf.triggerMask = 10 #high rate
###conf.triggerMask = 14 #precise energy
#conf.triggerMask = 1 #cntTarget for test
#conf.triggerMask = 2 #cntOut for trigger test
#conf.triggerMask = 12
#conf.triggerMask = 32 #laser

# Noise Mask
conf.triggerMask = 8 # 16 #14 #16 #2 #8

#conf.daq.setIgnoreSyncronizationProblems(True)  # ACHTUNG!
conf.daq.setIgnoreSyncronizationProblems(False)
conf.daq.setSyncInterval(10000)
conf.daq.setAsyncRunInitDelay(0)
#conf.daq.setTriggerInterval(3700) #for GEM readout without veto
conf.daq.setTriggerInterval(1500) #for GEM readout without veto
conf.daq.setRunSize(EVENT_COUNT)
#conf.daq.setRunSize(15000)

#This call configures trigger writes gates and attenuations to hardware
conf.configureHardware()
##conf.configureFARICH()

#Each subsystem to be collected should be registered below
conf.daq.addDaq(conf.service)

print conf.runname

if "gem" in enabled_systems:
   gemDaq = conf.gemDaq
   gemDaq.setHost("localhost", 2313, 2333)
   gemDaq.setMandatory(True)
   conf.daq.addDaq(conf.gemDaq)
else:
   print "gem(obsolete) readout disabled"

#if "remote-gem" in enabled_systems:
#   remoteDaq = RemoteDaq("remote-gem")
#   remoteDaq.setFilename(conf.runname)
#   remoteDaq.bind("localhost:4000")
#   conf.daq.addDaq(remoteDaq)


if "tb-gem" in enabled_systems:
	tbGemDaq = []
	tbgem_names = ["tbgem3", "tbgem1", "tbgem2"] # = ["tbgem"+i for i in "312"]
	gem_print_events = False #True
	
	for name in tbgem_names:
		daq = TestbeamGemDaq(name)
		daq.setPrintEvents(gem_print_events)
		tbGemDaq.append(daq)
		conf.daq.addDaq(daq)
else:
	print "tb-gem      readout disabled"

#if "remote-dummy" in enabled_systems:
#   remoteDaq2 = RemoteDaq("remote-dummy")
#   remoteDaq2.setFilename(conf.runname)
#   remoteDaq2.bind("localhost:4001")
#   conf.daq.addDaq(remoteDaq2)

if "trb" in enabled_systems:
   remoteDaq3 = RemoteDaq("remote-trb")
   remoteDaq3.setFilename(conf.runname)
   remoteDaq3.bind("localhost:40000")
   conf.daq.addDaq(remoteDaq3)
else:
   print "trb         readout disabled"

if "mkp" in enabled_systems:
   remoteDaq4 = RemoteDaq("remote-mkp")
   remoteDaq4.setFilename(conf.runname)
   remoteDaq4.bind("trb-new:4002")
   conf.daq.addDaq(remoteDaq4)
else:
   print "mkp         readout disabled"

if "calo" in enabled_systems:
   conf.daq.addDaq(conf.calorimeter)
else:
   print "calorimeter readout disabled"

if "lecroy" in enabled_systems:
   conf.daq.addDaq(conf.lecroy2249)
else:
   print "lecroy2249  readout disabled"

#conf.daq.setEventIndexSource(None)


#Actual run start
if run:
    try:
        #Speak('Begin.')
        #os.system('xterm -geometry 45x14+2250+260 -T "keep_trg" -e bash -c "keep_trg.py 90 50" &') # keep trigger rate
        runner = AsyncRunner(conf.run)
        runner.runInterruptible(conf.daq.interrupt)
        #os.system('pkill -INT -ex "keep_trg.py"')
        #time.sleep(1)
        #os.system('pkill -ex "keep_trg.py"')
        #os.system("ssh -Tf beam-daq 'aplay Music/endrun.wav' >/dev/null 2>&1")
        Speak('Run finished.')
    except KeyboardInterrupt:
        Speak('Control C!')
        raise
    except RuntimeError:
        Speak('Fail!')
        raise

