import logging
from azure.data.tables import TableServiceClient
from datetime import datetime
import azure.functions as func
import json 
connection_string = "DefaultEndpointsProtocol=https;AccountName=uc3bhwii;AccountKey=XUEDCBkPBnQg1Hb2DR2lYDigRRzKcNLYO98AlbLTbLIgRr2ivt94gTxFgByvJwnJe1Ui/tifNCnxURTKBdJM8A==;EndpointSuffix=core.windows.net"
service = TableServiceClient.from_connection_string(conn_str=connection_string)


class Kaffee_maschine():
    def __init__(self) :
        self.Kaffee_Maschine_ID = 0
        self.Time_of_execution = datetime()
        self.Kaffee_menge = 0
        self.Kaffee_sorte = ""
        
    def fromJson(messwert_als_json_string):
        messwert_geparst = json.loads(messwert_als_json_string)

        messwertObjekt = Kaffee_maschine()
        messwertObjekt.Kaffee_Maschine_ID = messwert_geparst["Kaffee_Maschine_ID"]
        messwertObjekt.Time_of_execution = messwert_geparst["Time_of_execution"]
        messwertObjekt.Kaffee_menge = messwert_geparst["Kaffee_menge"]
        messwertObjekt.Kaffee_sorte = messwert_geparst["Kaffee_sorte"]
        #messwertObjekt.status = messwert_geparst["status"]

        return messwertObjekt

def main(msg: func.ServiceBusMessage):
    Kaffee_maschine_object = Kaffee_maschine()
    Kaffee_maschine_object.fromJson(logging.info('Python ServiceBus queue trigger processed message: %s', msg.get_body().decode('utf-8')))

    my_entity = {

        u'Kaffee_Maschine_ID': Kaffee_maschine_object.Kaffee_Maschine_ID,
        u'Time_of_execution': Kaffee_maschine_object.Time_of_execution,
        u'Kaffee_menge': Kaffee_maschine_object.Kaffee_menge,
        u'Kaffee_sorte': Kaffee_maschine_object.Kaffee_sorte

    }

    table_client = service.get_table_client(table_name="kaffeDatensatz")

    entity = table_client.create_entity(entity=my_entity)






