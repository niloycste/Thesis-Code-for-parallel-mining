#/usr/bin/env python

import time
import threading
import os
import sys





def increment():
	pool = 100000
	inflow = 400
	i=0
	pid = str(os.getpid())
	pidfile = "/tmp/mydaemon.pid"
	f= open(pidfile,"w+")
	#file(pidfile, 'w').write(pid)
	f.write(pid)
	
	while True:
		
		
		print(pool)
		time.sleep(1)
		pool = pool + inflow
		
		i += 1


#increment()

t = threading.Thread(target=increment,name='Increment')

t.daemon = True
t.start()
