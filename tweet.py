import helper

def getTWEETMessage():
    # getting the helper text
    message = helper.getMessage(
        filePath="SPAM_UK.txt", numberOfCharacters=140, msgType='TWEET')
    return message
