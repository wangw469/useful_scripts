import httplib
import socket
import sys

try:
    # print(sys.argv[3])
    h1 = httplib.HTTPConnection(sys.argv[3], sys.argv[4], timeout=1)
    h1.request("GET", "/")
    response = h1.getresponse()
    h1.close()
    # print("[PASS]")
except socket.timeout:
    # print("[FAILED]timeout")
    sys.exit(1)
except:
    # print("[FAILED]")
    sys.exit(1)
