from utils.color import bcolors

# Print with colors
class Info_Log:
    def __init__(self, message):
        print(bcolors.OKGREEN + "[ INFO ] " + bcolors.ENDC + message)

class Warning_Log:
    def __init__(self, message):
        print(bcolors.WARNING + "[ WARNING ] " + bcolors.ENDC + message)

class Error_Log:
    def __init__(self, message):
        print(bcolors.FAIL + "[ ERROR ] " + bcolors.ENDC + message)
