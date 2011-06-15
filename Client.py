import ParsingRequest
# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="ChuongNN"
__date__ ="$Jun 13, 2011 2:21:00 PM$"

import gearman

from ParsingRequest import ParsingRequest
from ParsingRequestQueue import ParsingRequestQueue
from ultis import encode
from ultis import decode
class Client:

	def __init__(self,
				serverAddressList,
				clientManager):
		self._serverAddressList = serverAddressList
		self._gearmanClient = gearman.GearmanClient(self._serverAddressList)
		self._clientManager = clientManager

		self._parsingRequestQueue = ParsingRequestQueue()

	def getStatus(self,
					requestSequenceNumber="all"):
		return self._parsingRequestQueue.getRequestStatus(requestSequenceNumber)

	def submitRequest(self,
					parsingRequest):
		parsingRequest.setStatus(ParsingRequest.CONST_STATUS_SUBMITING)
		self._parsingRequestQueue.add(parsingRequest)

		input = encode(parsingRequest)

		submittedRequest = self._gearmanClient.submit_job("parsing",
															input,
															background=False,
															wait_until_complete=False)
		parsingRequest.setStatus(ParsingRequest.CONST_STATUS_PROCESSING)

		#completed_request = self._gearmanClient.([submitted_request,])

		parsingRequest.setStatus(ParsingRequest.CONST_STATUS_FINISH)
		output = decode(completed_request.result)

	def run(self):
		pass