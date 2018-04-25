import sys
import os
import json
import sms
import tweet
import mail
import randomText

print(" Phishing Text Generator")

# This function will take the user option as a input


def getuseroption():
    print(" Choose your options from below:")
    print(" Do you want to generate : ")
    print(" A) SMS Text. B) Tweets . C) Instant Messaging Text. D) Random Experimental Text")
    userpotion = str(input(" Pease enter A/B/C/D : "))
    return userpotion

# This function will take the number of messages to print as a input
def getNoOfMessages():
    resultcount = input("Please enter the amount of Short Message Text's to be generated : ")
    return int(resultcount)

while(True):
    # checkig whether the json file is already existed, if no creating the file
    # and writing a default JSON template.
    if not (os.path.exists("./globalData.JSON")):
        globalDictionary = {'SMS': [],
                            'TWEET': [],
                            'MAIL': [],
                            'RANDOM': []}
        jsondata = json.dumps(globalDictionary)
        with open("./globalData.JSON", "w+") as file:
            file.write(jsondata)

    # reading the data from the JSON file
    finalJSONData = json.load(open("./globalData.JSON"))

    useroption = getuseroption()
    noOfMessages = getNoOfMessages()

    try:
        # creating a output file to store the generated data
        outputFile = open("Output.txt", "a")

        # putting coditions based on useroption
        if(useroption == 'A'):
            # looping through no.of messages user asking for
            i = 1
            while(i <= noOfMessages):
                # getting the message
                message = sms.getSMSMessage()
                # Checking whether the generated message is already existed in the json or not
                # If no printing the message, and putting new message in json
                if message not in finalJSONData['SMS']:
                    print('SMS : ')
                    print(message + "\n" + "http:\\sampleURL" + "\n\n")
                    # writing the message in output text file
                    outputFile.write(message + "\n" + "http:\\sampleURL" + "\n\n")
                    #putting new message in json
                    finalJSONData['SMS'].append(message)
                    with open("./globalData.JSON", "w+") as file:
                        jsonString = json.dumps(finalJSONData)
                        file.write(jsonString)
                    i = i+1

        elif(useroption == 'B'):
            i = 1
            # getting the message
            while(i <= noOfMessages):
                message = tweet.getTWEETMessage()
                # Checking whether the generated message is already existed in the json or not
                # If no printing the message, and putting new message in json
                if message not in finalJSONData['TWEET']:
                    print('TWEET : ')
                    print(message + "\n" + "http:\\sampleURL" + "\n\n")
                    outputFile.write(message + "\n" + "http:\\sampleURL" + "\n\n")
                    #putting new message in json
                    finalJSONData['TWEET'].append(message)
                    with open("./globalData.JSON", "w+") as file:
                        jsonString = json.dumps(finalJSONData)
                        file.write(jsonString)
                    i = i+1
        elif(useroption == 'C'):
            i = 1
            while(i <= noOfMessages):
                message = mail.getMAILMessage()
                if message not in finalJSONData['MAIL']:
                    print('MAIL : ')
                    print(message + "\n" + "http:\\sampleURL" + "\n\n")
                    outputFile.write(message + "\n" + "http:\\sampleURL" + "\n\n")
                    finalJSONData['MAIL'].append(message)
                    with open("./globalData.JSON", "w+") as file:
                        jsonString = json.dumps(finalJSONData)
                        file.write(jsonString)
                    i = i+1
        elif(useroption == 'D'):
            i = 1
            while(i <= noOfMessages):
                message = randomText.getRANDOMMessage()
                if message not in finalJSONData['RANDOM']:
                    print('RANDOM : ')
                    print(message + "\n" + "http:\\sampleURL" + "\n\n")
                    outputFile.write(message + "\n" + "http:\\sampleURL" + "\n\n")
                    finalJSONData['RANDOM'].append(message)
                    with open("./globalData.JSON", "w+") as file:
                        jsonString = json.dumps(finalJSONData)
                        file.write(jsonString)
                    i = i+1
        else:
            print ("Please enter the valid input A/B/C/D")
    except Exception as e:
        print("Exception : ", str(e))
    finally:
        outputFile.close()
        exitOption = input("Do you want to re-generate the messages (Y/N) : ")
        if(exitOption == 'Y' ):
            break
        elif(exitOption == 'N' ):
            pass
        else:
            print ("Invalid Input")
            break