#!/usr/bin/python3

# Decode the values that a Keystone device displays to the Keystone Hardware Wallet app in order
# to verify that only xpub and other non-secure information is allowed to leak from
# a Keystone device.


import sys
sys.path.insert(0, './py_protocol')

import argparse
import gzip
from py_protocol import base_pb2
from ur.ur_decoder import URDecoder
from ur.cbor_lite import CBORDecoder

# Unzipped payload is in serialized proto3, convert it to human readable estring
def getMessageFromPayload(payload):
  message = base_pb2.Base()
  message.ParseFromString(payload)
  return message

def getContentFromUR(content):
  decoder = URDecoder()
  while True:
    for part in content:
      each_part = part.lower().strip()
      decoder.receive_part(each_part)
      if decoder.is_complete():
        break
    if decoder.is_complete():
      break
  if decoder.is_success():
    return decoder.result_message()
  else:
    return None
   
parser = argparse.ArgumentParser(description='Decode a keystone sync message.')
parser.add_argument("--filename", type=str, default="sample_qr_codes.txt",
                    help="Name of the file containing the keystone sync data")
args = parser.parse_args()
with open(args.filename) as f:
    content = f.readlines()
ur = getContentFromUR(content)
(payload, _) = CBORDecoder(ur.cbor).decodeBytes()
unzippedPayload = gzip.decompress(bytearray(payload))
message = getMessageFromPayload(unzippedPayload)
print("*************************************************************")
print("Following is entire message sent via QRCode from vault to app")
print("*************************************************************")
print(message)
print("*************************************************************")
print("")
print("At this point one should verify each of the XPUBs shown above, and")
print("the UUID shown below (also at the top of the above output). See the")
print("README.md for how to do that.")