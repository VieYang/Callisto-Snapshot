
import os,binascii,sys
from time import gmtime, strftime

from ethereum import utils

snapshot = sys.argv[1]

with open(snapshot) as afile:
    astr = afile.read()
    print("Open file {} ok....".format(snapshot))
    with open("lucky{}.log".format(strftime("%Y%m%d", gmtime())), 'a') as l:
        l.write("lucky..\n")
        l.close()
    while True:
        pkey = binascii.b2a_hex(os.urandom(32))
        raw_address = utils.privtoaddr("{}".format(pkey))
        account_address = utils.checksum_encode(raw_address)
        if account_address in astr:
            print(pkey, account_address)
