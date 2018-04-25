import helper

def getRANDOMMessage():
    # getting the random text
    message = helper.getMessage(
        filePath="SPAM_UK.txt", numberOfCharacters=250, msgType='RANDOM')
    return message
