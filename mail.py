import helper

def getMAILMessage():
    # getting the mail text
    message = helper.getMessage(
        filePath="SPAM_UK.txt", numberOfCharacters=250, msgType='MAIL')
    return message
