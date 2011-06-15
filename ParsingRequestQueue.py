# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="ChuongNN"
__date__ ="$Jun 13, 2011 4:21:12 PM$"

from ParsingRequest import ParsingRequest

class ParsingRequestQueue:

	def __init__(self):
		self._requestDict = dict()

	def get(self,
					requestSequenceNumber):
		return self._requestDict.get(requestSequenceNumber, None)

	def add(self,
					request):
		if(request!=None):
			self._requestDict[request.getSequenceNumber()] = request

	def remove(self,
						requestSequenceNumber="all"):
		if(requestSequenceNumber=="all"):
			self._requestDict.clear()
		else:
			del self._requestDict[requestSequenceNumber]

	def getRequestStatus(self,
						requestSequenceNumber="all"):
		returnString = ""
		if(requestSequenceNumber=="all"):
			for key in self._requestDict.keys():
				returnString += "Request No." + \
								str(key) + \
								": " + \
								str(self._requestDict[key].getStatus()) + \
								"\n"
		else:
			request = self.get(requestSequenceNumber)
			if(request!=None):
				returnString += "Request No." + \
								str(request.getSequenceNumber()) + \
								": " + \
								str(request.getStatus())

		return returnString
	