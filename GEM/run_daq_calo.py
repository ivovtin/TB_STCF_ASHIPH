#!/usr/bin/python

import sys
import argparse
import os
import time

from daqconf import BeamDaqConfiguration, AsyncRunner
from pydaq import TestbeamGemDaq

# 1 - cntTarget, 2 - cntOut, 4 - cntCalo, 8 - calo (not use 8 - phase, 16 - generator <-> LSO)
id_mask = {
	6:'cntOut + cntCalo',
	8:'calo',
	10:'cntOut + calo',
	12:'cntCalo + calo',
	14:'cntOut + cntCalo + calo',
	16:'cntPipe',
	32:'custom'
}


# ----- CreateParser() -----
def CreateParser():
	parser = argparse.ArgumentParser(description='Run DAQ for calorimeter test')
	parser.add_argument ('-r', type=int, default=50, dest='rate', help='setting trigger rate [Hz] (by default %(default)i)')
	parser.add_argument ('-m', type=int, default=14, dest='mask', help='setting trigger mask (by default %(default)i)')
	parser.add_argument ('-s', type=int, default=10000, dest='size', help='setting run size (by default %(default)i)')
	parser.add_argument ('--printMask', default=False, action='store_const', const=True, help='just print trigger mask and exit (by default \"%(default)s\")')
	parser.add_argument ('-k', '--keep', default=False, action='store_const', const=True, help='enable KEEP (by default \"%(default)s\")')
	parser.add_argument ('-g', '--gem', default=False, action='store_const', const=True, help='enable GEM (by default \"%(default)s\")')
	parser.add_argument ('-t', '--test', default=False, action='store_const', const=True, help='make test not run (by default \"%(default)s\")')
	return parser


# ----- Main -----
if __name__ == "__main__":
	parser = CreateParser()
	argSpace = parser.parse_args(sys.argv[1:])

	if argSpace.printMask:
		for _id, _mask in sorted(id_mask.items()):
			print '\t mask %2d -> trigger \'%s\''%(_id, _mask)
		exit(0)

	conf = BeamDaqConfiguration()

	conf.triggerMask = argSpace.mask
	if argSpace.mask in id_mask:
		print 'Trigger mask is %d <-> \"%s\"'%(argSpace.mask, id_mask[argSpace.mask])
	else:
		print 'Custom mask is %d' % (argSpace.mask)

	#conf.gemDaq.setPrintEvents(True)
	conf.calorimeter.setPrintEvents(False)
	conf.lecroy2249.setPrintEvents(True)
	conf.daq.eventWritePrintInterval(1)

	conf.daq.setIgnoreSyncronizationProblems(False)

	conf.daq.setSyncInterval(60) # seconds
	conf.daq.setTriggerInterval(2000) if argSpace.gem else conf.daq.setTriggerInterval(10) # microseconds

	conf.daq.setAsyncRunInitDelay(2)

	# - run size
	conf.daq.setRunSize(argSpace.size)
	#conf.daq.setRunTime(7200) # <->  2 hours

	# - this call configures trigger writes gates and attenuations to hardware
	conf.configureHardware()

	# - each subsystem to be collected should be registered below
	#conf.daq.addDaq(conf.calorimeter)
	conf.daq.addDaq(conf.lecroy2249)
	conf.daq.addDaq(conf.service)
	#conf.daq.addDaq(conf.triggerCount)

	#conf.calorimeter.setMandatory(False)
	conf.lecroy2249.setMandatory(True)
	#conf.lock.setMandatory(False)

	if argSpace.gem:
		gem_print_events = False
		#tbGemDaq0 = TestbeamGemDaq("tbgem0")
		tbGemDaq1 = TestbeamGemDaq("tbgem1")
   		tbGemDaq2 = TestbeamGemDaq("tbgem2") 
   		tbGemDaq3 = TestbeamGemDaq("tbgem3") 
   		#tbGemDaq0.setPrintEvents(gem_print_events)
   		tbGemDaq1.setPrintEvents(gem_print_events)
   		tbGemDaq2.setPrintEvents(gem_print_events)
   		tbGemDaq3.setPrintEvents(gem_print_events)
   		#conf.daq.addDaq(tbGemDaq0)
   		conf.daq.addDaq(tbGemDaq1)
   		conf.daq.addDaq(tbGemDaq2)
   		conf.daq.addDaq(tbGemDaq3)



	# - actual run start
	if not argSpace.test:
		if argSpace.keep:
			_min_rate = int(0.75*argSpace.rate)
			_keep_cmd = 'keep_trg.py %d %d'%(argSpace.rate, _min_rate)
			os.system('xterm -fn 9x15 -geometry 45x30+870+517 -e bash -c "%s" &'%_keep_cmd) # keep trigger rate

		runner = AsyncRunner(conf.run)
		runner.runInterruptible(conf.daq.interrupt)

		if argSpace.keep:
			os.system('xterm -geometry 54x14+2250+260 -T "keep_trg" -e bash -c "keep_trg_sk.py 110 74000" &') # keep trigger rate: 1 - rate, 2 - position in steps
			os.system('pkill -INT -ex "keep_trg_sk.py"')
			time.sleep(1)
			os.system('pkill -ex "keep_trg_sk.py"')

		os.system("ssh -Tf beam-daq 'aplay Music/endrun.wav' >/dev/null 2>&1")








