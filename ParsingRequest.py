# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="ChuongNN"
__date__ ="$Jun 8, 2011 4:37:25 PM$"

import sys

class Request:

	#Here we define command code for different types of request. Every particular
	#request which inherits from Request class will init their command data
	#attribute with one of following values:
	CONST_COMMAND_PARSING = "parsing"

	#Here, we define a int varaiable for parsing request tracking purpose
	requestIndex = 0

	def __init__(self):
		self._parameter = {}
		self._data = None
		self._command = None

		self._validFlag = True
		self._requestSequenceNumber = 0

		self.assignSequenceNumber()

	def assignSequenceNumber(self):
		self.__class__.requestIndex = (self.__class__.requestIndex + 1)%sys.maxint
		self._requestSequenceNumber = self.__class__.requestIndex

	def setParameter(self,
					parameterName,
					parameterValue):
		self._parameter[parameterName] = parameterValue

	def getParameter(self,
					parameterName):
		return self._parameter[parameterName]

	def setData(self,
				data):
		self._data = data

	def getData(self):
		return self._data

	def setCommand(self,
					command):
		self._command = command

	def getCommand(self):
		return self._command

	def setValidFlag(self,
					value):
		self._validFlag = value

	def isValid(self):
		return self._validFlag

	def getSequenceNumber(self):
		return self._requestSequenceNumber

	#Debug methods
	def getDebugString(self):
		debugString = "Parsing request content:\n"
		debugString += "Parameters:\n"
		for key in self._parameter.keys():
			debugString += "**" + str(key) +": " + str(self._parameter[key]) + "\n"
		debugString += "Data:\n" + "**" + str(self._data) + "\n"
		debugString += "Command:\n" + "**" + str(self._command) + "\n"
		debugString += "Valid Flag:\n" + "**" + str(self._validFlag) + "\n"
		debugString += "Sequence Number:\n" + "**" + str(self._requestSequenceNumber) + "\n"

		return debugString


class ParsingRequest(Request):

	#Here, we define a set of parsing request status. Generally, following
	#actions will be performced on a well prcocessed request:
	#submit --> queue at job server --> process --> import to database
	#	^		(crashed/rejected)		(failed)
	#	|				|					|
	#	|				v					v
	#	+<------------retry<----------------+
	#	^		(no server available)
	#	|				|
	#	|				v
	#	+<-------------halt
	#Then, we have following possible statuses for one request:

	CONST_STATUS_INIT = "init"
	CONST_STATUS_SUBMITING = "submiting"
	CONST_STATUS_QUEUEING = "queueing"
	CONST_STATUS_PENDING = "pending"
	CONST_STATUS_PROCESSING = "processing"
	CONST_STATUS_FINISH = "finished"

	def __init__(self):
		#For father class
		Request.__init__(self)
		Request.setCommand(self, Request.CONST_COMMAND_PARSING)
		
		#For ParsingRequest class
		self._status = ParsingRequest.CONST_STATUS_INIT

	def getStatus(self):
		return self._status

	def setStatus(self,
					status):
		self._status = status

	#Debug method
	def getDebugString(self):
		debugString = Request.getDebugString(self)
		debugString += "Status:\n" + "**" + str(self._status) + "\n"

		return debugString