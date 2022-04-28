from time import sleep
from typing_extensions import Self
from azure.iot.device import IoTHubModuleClient
from random import randint

RECEIVED_MESSAGES = 0 
Kaffesorte = "KaffeLatte" 


def send_a_list_of_messages(sender):
    # create a list of messages
    messages = [ServiceBusMessage("Message in list") for _ in range(5)]
    # send the list of messages to the queue
    sender.send_messages(messages)
    print("Sent a list of 5 messages")

def main ():
    connection_string = "HostName=iot3bhwii22-es.azure-devices.net;DeviceId=Notebook-es;SharedAccessKey=S+VsJvpF90xN6m9VLrTdb5/YurTU6DhrNUCRwHUYL3c="
    client = IoTHubModuleClient.create_from_connection_string(connection_string) 

   # messages = [send_message ("RECEIVED_MESSAGES ++ Kaffesorte") for _ in range(5)]

    client.connect()

    client.send_message(Kaffesorte)
    client.disconnect()
    client.shutdown()

def massage_receiver ():
    global RECEIVED_MESSAGES
    RECEIVED_MESSAGES += 1
    print("")
    print("Message received:")

main()
#massage_receiver()