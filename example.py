from time import sleep
from azure.iot.device import IoTHubModuleClient
from random import randint
def main ():
    connection_string = "HostName=iot3bhwii22-es.azure-devices.net;DeviceId=Notebook-es;SharedAccessKey=S+VsJvpF90xN6m9VLrTdb5/YurTU6DhrNUCRwHUYL3c="
    client = IoTHubModuleClient.create_from_connection_string(connection_string) 

    client.connect()

    client.send_message(str(randint(15,25)))

    client.disconnect()
    client.shutdown()



main()
