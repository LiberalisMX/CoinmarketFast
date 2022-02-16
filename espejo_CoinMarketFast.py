from telethon import TelegramClient, events
from telethon.tl.custom import Button
import pymongo


## setup db
mongodb_key = "mongodb+srv://Xicano22:CiudadDelSolG20@cluster0.jt7sg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = pymongo.MongoClient(mongodb_key)
db_name = "Bote"
collection_name = "BoteCol"
db = client[db_name][collection_name]

phone_number = '525612720431'
api_id = '7504340'
api_hash = 'a2d9b532bfc53b81ae70eb0293944b26'

tgclient = TelegramClient(phone_number, api_id, api_hash)

id_Canal_Copia = -1001793288513
#id_canal_original = -1001519789792
id_canal_original = -1001252203928 #####Canal de prueba
@tgclient.on(events.NewMessage(id_canal_original))
async def my_event_handler(event):    
    text = event.raw_text
    media = event.media
    poocoin_url = event.message.buttons[0][0].url
    bsc_scan_url = event.message.buttons[1][0].url
    stay_safu_url = event.message.buttons[1][1].url
    #print(text)
    print("Poocoin link: " + poocoin_url)
    print("BSC Scan link: " + bsc_scan_url)
    print("Stay Safu link: " + stay_safu_url)   
    text = text + " -\n\nPoocoin: " + poocoin_url  + " -\nBSC Scan: " + bsc_scan_url + " -\nStay Safu: " + stay_safu_url  + " -"
    #Detectar si el mensaje contiene texto o imagenes y reenviar al canal destino
    if media != None and text != None:
        file = await tgclient.download_media(event.message.media, file=bytes)
        await tgclient.send_file(id_Canal_Copia, file=file, caption=text)
    else:
        if text != None: 
            await tgclient.send_message(id_Canal_Copia, text)
        if media != None:
            file = await tgclient.download_media(event.message.media, file=bytes)
            await tgclient.send_file(id_Canal_Copia, file=file)

#Reacciona cuando un mensaje es editado
@tgclient.on(events.MessageEdited(id_canal_original))
async def handler(event):
    text = event.raw_text
    id_Canal_Original_Evento = event.chat_id
    id_Canal_Copia = conectar_canales(id_Canal_Original_Evento)
    #Bucle en rango que busca el canal origianl para hacer match entre los canales originales y la copia  

    #tgclient.edit_message(event.chat_id, event.id, text)
    mensajes= await tgclient.get_messages(id_Canal_Copia)
    mensaje = mensajes[-1]
    try:
        await tgclient.edit_message(id_Canal_Copia, mensaje.id, text)
    except:
        await tgclient.delete_messages(id_Canal_Copia, mensaje)
        mensajes= await tgclient.get_messages(event.chat_id)
        mensaje = mensajes[-1]
        #print(mensaje)
        file = await tgclient.download_media(mensaje, file=bytes)    
        await tgclient.send_file(id_Canal_Copia, file=file, caption=text)    
    #print('Message text: ', text, ' Chat id: ', chat_id, ' Message ID: ', event_id) 

#Reacciona cuando una acción es descadenada (foto de perfil, mensajes fijados, etc..)    
@tgclient.on(events.ChatAction(id_canal_original))
async def my_event_handler(event):
    id_Canal_Original_Evento = event.chat_id
    id_Canal_Copia = conectar_canales(id_Canal_Original_Evento)

    #Si hay una nueva foto de perfil enviar la imagen al canal destino en forma de imagen       
    try:
        if event.new_photo:
            print("Nueva foto de perfil")
            photos = await tgclient.get_profile_photos(event.chat_id)
            image = await tgclient.download_media(photos[0], file=bytes, thumb=3)
            await tgclient.send_file(id_Canal_Copia, file=image)
    except:
        print("Hubo un error con la descargando la foto de perfil")

tgclient.start()
tgclient.run_until_disconnected()
