# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="ChuongNN"
__date__ ="$Jun 8, 2011 1:44:53 PM$"

import os.path

import constants

from ultis import readUserChoice
from ultis import printInvalidParameterEnteredWarning
from ultis import readParsingInfoFromXMLRequestFile
from ParsingRequest import ParsingRequest

class UserInterface:

	_clientManager = None
	_runFlag = False

	def __init__(self,
				clientManager):
		self._clientManager = clientManager

	def start(self):
		self._runFlag = True
		self.workingLoop()

	def stop(self):
		self._runFlag = False

	def workingLoop(self):
		argumentName = constants.USER_CHOICE
		defaultValue = str(constants.USER_CHOICE_DEFAULT)
		guide = "Your choices:\n" + \
					"%s: quit\n"%str(constants.USER_CHOICE_QUIT) + \
					"%s: do nothing\n"%str(constants.USER_CHOICE_DO_NOTHING) + \
					"%s: view manager status\n"%str(constants.USER_CHOICE_VIEW_MANAGER_STATUS) + \
					"%s: submit parsing job"%str(constants.USER_CHOICE_SUBMIT_PARSING_JOB)
												
		validValues = [str(constants.USER_CHOICE_QUIT),
						str(constants.USER_CHOICE_DO_NOTHING),
						str(constants.USER_CHOICE_VIEW_MANAGER_STATUS),
						str(constants.USER_CHOICE_SUBMIT_PARSING_JOB)]
						
		while(self._runFlag):
			self.processUserRequest(int(readUserChoice(argumentName,
														defaultValue,
														guide,
														validValues)))
														
	def processUserRequest(self,
							userRequest):

		if(userRequest==constants.USER_CHOICE_QUIT):
			self.stop()
			print("bye")

		elif(userRequest==constants.USER_CHOICE_DO_NOTHING):
			pass

		elif(userRequest==constants.USER_CHOICE_VIEW_MANAGER_STATUS):
			print(self._clientManager.readStatus())

		elif(userRequest==constants.USER_CHOICE_SUBMIT_PARSING_JOB):
			parsingRequest = self.readParsingInfo()
			if(parsingRequest.isValid()):
				self._clientManager.submitParsingRequest(parsingRequest)
				print("Submit following parsing request:")
				print(parsingRequest.getDebugString())
			else:
				printInvalidParameterEnteredWarning("parsing request file",
									"",
									"parsing request based this file")

		else:
			pass

	def readParsingInfo(self):
		parsingRequest = ParsingRequest()
		
		parsingRequestFile = readUserChoice(constants.PARSING_REQUEST_FILE,
											constants.PARSING_REQUEST_FILE_DEFAULT)
		if(os.path.isfile(parsingRequestFile)):
			readParsingInfoFromXMLRequestFile(parsingRequestFile, parsingRequest)
		else:
			parsingRequest.setValidFlag(False)
			deniedAction = "parsing request based this file"
			printInvalidParameterEnteredWarning(constants.PARSING_REQUEST_FILE,
												parsingRequestFile,
												deniedAction)
			
		return parsingRequest
		