import ClientManager
# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="ChuongNN"
__date__ ="$Jun 7, 2011 11:12:30 AM$"

import sys

import constants

from UserInterface import UserInterface
from Client import Client
from ParsingRequestQueue import ParsingRequestQueue

class ClientManager:

	#Attributes
	JOB_SERVER_ADDRESS_LIST = ["127.0.0.1:4730",]

	#Main methods
	def __init__(self):
		
		self._userInterface = None
		self._runMode = constants.RUN_MODE_DAEMON
		self._parsingRequestQueue = ParsingRequestQueue()
		
	def start(self,
				runMode=constants.RUN_MODE_DAEMON):

		self._runMode = runMode

		if (self._runMode==constants.RUN_MODE_DAEMON):
			pass
		else:
			self._userInterface = UserInterface(self)
			self._userInterface.start()

	def stop(self):

		print("clientManager stopping...")
		exit(0)

	#Sub - methods
	def submitParsingRequest(self,
							parsingRequest):

		gearmanClient = Client(ClientManager.JOB_SERVER_ADDRESS_LIST,
								parsingRequest)
		gearmanClient.run()
		gearmanClient = None
		

	def readStatus(self,
					requestSequenceNumber="all"):

		return self._parsingRequestQueue.getStatus(requestSequenceNumber)


if __name__=="__main__":
	_clientManager = ClientManager()
	_runMode = constants.RUN_MODE_DAEMON

	if(len(sys.argv) > 1):
		if(sys.argv[1]=="-f"):
			_runMode = constants.RUN_MODE_FOREGROUND

	#try:
	_clientManager.start(_runMode)
	#except Exception:
	#	_clientManager.stop()
	#	exit(0)
	