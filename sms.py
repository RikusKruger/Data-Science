#An SMS Simulation
##################
# CODE
##################


class SMSMessage:
    def __init__(self, number, messageText):
        self.hasBeenRead = False
        self.messageText = messageText
        self.fromNumber = number

    def MarkAsRead(self, read):
        read = True
        return read

SMSStore = []
readMessages = []
userChoice = ""


def add_sms(number, text):
    new_message = SMSMessage(number, text)
    SMSStore.append(new_message)

def get_count():
    tot_messages = len(SMSStore)
    return tot_messages

def get_message(number):
    reading = readMessages[number-1]
    text = reading.messageText
    return text

def get_unread_message(number):
    reading = SMSStore.pop(number - 1)
    readMessages.append(reading)
    SMSMessage.MarkAsRead(reading, reading.hasBeenRead)
    text = reading.messageText
    return text


def remove(number):
    readMessages.remove(number-1)
    return



while userChoice != "quit":
    userChoice = input("What would you like to do - read/send/remove/quit?")
    if userChoice == "read":
        print(f"You have {get_count()} unread messages.")
        if get_count() > 0:
            messageNumber = int(input("Please enter the number of the message you would like to read: "))
            try:
                text = get_unread_message(messageNumber)
                print(f"Message {messageNumber} is:\n {text}")
            except ValueError:
                messageNumber = int(input("NOT A NUMBER!! \nPlease enter the number of the message you would like to read: "))
            except IndexError:
                print("You do not have that many messages")
        else:
            read = input("Would you like to pick a previously read message?(y/n): ")
            if read == "y":
                if len(readMessages) > 0:
                    print(f"You have {len(readMessages)} read messages.")
                    try:
                        read_message = int(input("Please enter the message number: "))
                    except ValueError:
                        messageNumber = int(input("NOT A NUMBER!! \nPlease enter the number of the message you would like to read: "))
                    try:
                        print(f"The message reads: \n {get_message(read_message)}")
                    except IndexError:
                        print("You do not have that many messages")
                else:
                    print(f"You have {len(readMessages)} read messages.")
                    continue
            else:
                continue
    elif userChoice == "send":
            num = input("Please enter your number: ")
            message = input("Please enter your message: ")
            add_sms(num, message)
            print("Message sent!")

    elif userChoice == "quit":
        print("Goodbye")
        exit()
    elif userChoice == "remove":
        if len(readMessages) > 0:
            num = int(input("Please enter the number of the message you wish to remove: "))
            remove(num)
            print(f"Message {num} removed")
        else:
            print("No messages to delete.")
    else:
        print("Oops - incorrect input")
