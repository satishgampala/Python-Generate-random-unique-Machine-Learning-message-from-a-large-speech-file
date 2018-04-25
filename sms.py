import helper


def getSMSMessage():
    # getting the sms text
    message = helper.getMessage(
        filePath="SPAM_UK.txt", numberOfCharacters=165, msgType='SMS')
    return message
