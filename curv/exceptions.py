class CurvRequestException(Exception):
    def __init__(self, message):
        self.__message = message

    def __str__(self):
        return "CurvRequestException: {}".format(self.get_message())

    def get_message():
    	return self.__message

class CurvMissingParams(Exception):
    def __init__(self, message):
        self.__message = message

    def __str__(self):
        return "CurvMissingParams: {}".format(self.get_message())

    def get_message():
    	return self.__message