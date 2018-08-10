import httplib
import socket
import sys

try:
    print(sys.argv)
    # h1 = httplib.HTTPConnection('test', 10080, timeout=3)
    # h1.request("GET", "/")
    # response = h1.getresponse()
    # print("[PASS]")
except socket.timeout:
    # print("[FAILED]timeout")
    sys.exit(1)
except:
    # print("[FAILED]")
    sys.exit(1)
