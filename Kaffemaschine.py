from time import sleep
from typing_extensions import Self
from azure.iot.device import IoTHubModuleClient
from random import randint
import datetime 
import json

RECEIVED_MESSAGES = 0 
Kaffesorte = "KaffeLatte" 

class Kaffee_maschine():
    def __init__(self) :
        self.Kaffee_Maschine_ID = ""
        self.Time_of_execution = datetime()
        self.Kaffee_menge = 0
        self.Kaffee_sorte = ""
        
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)


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