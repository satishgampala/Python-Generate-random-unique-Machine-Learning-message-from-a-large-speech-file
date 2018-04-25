import markovify


def textdatabase(filePath, msgType):
    # opening and reading the text data file
    with open(filePath) as f:
        fileContent = f.read()
        return fileContent


def getMarkovifyModel(filePath, msgType):
    # getting the model by using markovify module
    fileContent = textdatabase(filePath, msgType)
    model = markovify.Text(fileContent, state_size=2)
    return model


def getMessage(filePath, numberOfCharacters, msgType):
    # getting  message from the model
    model = getMarkovifyModel(filePath, msgType)
    message = model.make_short_sentence(numberOfCharacters)
    return message
