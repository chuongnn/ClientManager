# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="ChuongNN"
__date__ ="$Jun 8, 2011 1:51:56 PM$"

import os.path
import xml.dom.minidom
import pickle

import constants

#########################readUserChoice()#######################################
def readUserChoice(argumentName,
					defaultValue="",
					guide="",
					validValues=None):

	#Now, we print out promt & wait until use enters her choice
	choice = ""
	if(defaultValue!=""):
		if(guide==""):
			choice = raw_input("Enter value for %s(default:%s):\n>"%(argumentName, defaultValue))
		else:
			choice = raw_input("Enter value for %s(default:%s):\n%s\n>"%(argumentName, defaultValue, guide))
	else:
		if(guide==""):
			choice = raw_input("Enter value for %s:\n>"%(argumentName))
		else:
			choice = raw_input("Enter value for %s:\n%s\n>"%(argumentName, guide))

	#Let's check & hope that she doesn't enter a foolish thing. Otherway, let's
	#try to return default value if it's available
	if (validValues!=None):
		validFlag = False
		for validValue in validValues:
			if(choice==validValue):
				validFlag = True
		if(validFlag==False):
			if(defaultValue==""):
				print("Invalid value for %s entered. No action will b performed"%(argumentName))
			else:
				print("Invalid value for %s entered. Use default value(%s)"%(argumentName, defaultValue))
				choice = defaultValue
	else:
		if(defaultValue!="" and choice==""):
			print("Invalid value for %s entered. Use default value(%s)"%(argumentName, defaultValue))
			choice = defaultValue

	return choice

######################printInvalidParameterEnteredWarning()#####################
def printInvalidParameterEnteredWarning(parameterName, 
										parameterValue,
										deniedAction):

	if(parameterValue==""):
		print("You have just entered an invalid %s, %s"%(parameterName, deniedAction) +\
			" can't be made!")
	else:
		print("You have just entered an invalid %s(invalid value: %s), %s" \
		%(parameterName, parameterValue, deniedAction) + \
			 "can't be made!")

######################readParsingInfoFromXMLRequestFile()#######################
def readParsingInfoFromXMLRequestFile(filePath, parsingRequest):

	dom = xml.dom.minidom.parse(filePath)
	folderPathList = list()
	regexList = list()
	validFlag = False

	#Read General Node
	parsingNode = dom.getElementsByTagName(constants.XML_TAG_PARSING_REQUEST)
	if(len(parsingNode)!=1):
		parsingRequest.setValidFlag(False)
		return

	#Read & check folder paths for parsing
	folderPathNodes = dom.getElementsByTagName(constants.XML_TAG_FOLDER_PATH)
	if(len(folderPathNodes)==0):
		parsingRequest.setValidFlag(False)
		return
	validFlag = False
	for folderPathNode in folderPathNodes:
		folderPath = folderPathNode.getAttribute(constants.XML_ATTRIBUTE_VALUE)
		if(os.path.isdir(folderPath)):
			validFlag = True
			folderPathList.append(folderPath)
		else:
			printInvalidParameterEnteredWarning("folder path",
												folderPath,
												"parsing on this folder")
	if(validFlag==False):
		parsingRequest.setValidFlag(False)
		printInvalidParameterEnteredWarning("folder path list",
											"",
											"parsing request in this file")
		return
	else:
		parsingRequest.setParameter(constants.INPUT_FOLDER_PATH_LIST, 
									folderPathList)

	#Read & check regexs for parsing
	regexNodes = dom.getElementsByTagName(constants.XML_TAG_REGEX)
	if(len(regexNodes)==0):
		parsingRequest.setValidFlag(False)
		return
	for regexNode in regexNodes:
		regex = regexNode.getAttribute(constants.XML_ATTRIBUTE_VALUE)
		regexList.append(regex)
	parsingRequest.setParameter(constants.REGEX_LIST,
								regexList)
	return

############################encode() & decode()#################################
def encode(structured_data):
	return pickle.dumps(structured_data)

def decode(decodable_string):
	return pickle.loads(decodable_string)
################################################################################