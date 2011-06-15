# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="ChuongNN"
__date__ ="$Jun 8, 2011 9:31:57 AM$"

if __name__ == "__main__":
	print "Hello World"

RUN_MODE_DAEMON = 1
RUN_MODE_FOREGROUND = 2

USER_CHOICE = "next action"

USER_CHOICE_QUIT = 0
USER_CHOICE_DO_NOTHING = 1
USER_CHOICE_VIEW_MANAGER_STATUS = 2
USER_CHOICE_SUBMIT_PARSING_JOB = 3
USER_CHOICE_DEFAULT = USER_CHOICE_DO_NOTHING

INPUT_FOLDER_PATH_LIST = "input folder path list"
INPUT_FOLDER_PATH_LIST_DEFAULT = ["/root/",]

REGEX_LIST = "regex list"
REGEX_LIST_DEFAULT = ["/root/",]

PARSING_REQUEST_FILE = "parsing request file"
PARSING_REQUEST_FILE_DEFAULT = "/root/NetBeansProjects/ClientManager/src/parsingRequest.xml"

INPUT_METHOD = "input method"
INPUT_METHOD_TERMINAL = 1
INPUT_METHOD_FILE = 2
INPUT_METHOD_DEFAULT = INPUT_METHOD_TERMINAL

XML_TAG_PARSING_REQUEST = "parsingRequest"
XML_TAG_FOLDER_PATH = "folderPath"
XML_TAG_REGEX = "regex"
XML_ATTRIBUTE_VALUE = "value"