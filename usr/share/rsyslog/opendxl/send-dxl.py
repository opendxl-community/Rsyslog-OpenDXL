#!/usr/bin/python
import sys, getopt,socket,json,os

from dxlclient.client import DxlClient
from dxlclient.client_config import DxlClientConfig
config = DxlClientConfig.create_dxl_config_from_file(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dxl.conf'))

from dxlclient.message import Event

IP = socket.gethostname()

DXL_MESSAGE = {}

def main(argv):
	TOPIC_DESTINATION = '/events/syslog'
	TYPE_PAYLOAD = 'syslog'
	PAYLOAD = sys.argv[1]

	DXL_MESSAGE['SRC_HOST'] = IP
	DXL_MESSAGE['TYPE_PAYLOAD'] = TYPE_PAYLOAD
	DXL_MESSAGE['PAYLOAD'] = PAYLOAD

	with DxlClient(config) as client:
		client.connect()
	    	event = Event(TOPIC_DESTINATION)
	    	event.payload = str(json.dumps(DXL_MESSAGE)).encode()
		client.send_event(event)


if __name__ == "__main__":
   main(sys.argv[1:])










