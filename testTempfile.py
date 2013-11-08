__author__ = 'vincentc'
import tempfile
import time
fp = tempfile.NamedTemporaryFile()
fp.write(b'Hello world!')
print (fp.name)
time.sleep(50000)
