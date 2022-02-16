import asyncio 
from telethon import TelegramClient
from telethon import functions, types, events
from telethon.tl.custom import Button

# start the bot client
tgclient = TelegramClient('BOT_REENVIO', 'id', 'hash')
tgclient.start(bot_token='token')

id_Canal_Copia = -10017932885
#id_canal_original = -1001519789
id_CoinmarketFast_ES = -10012522039 #####Canal de prueba
@tgclient.on(events.NewMessage(id_Canal_Copia))
# function that sends the message
async def my_event_handler(event): 
    text = event.raw_text
    print(text)
    texto = text.split('-')[0]
    try:
        texto = texto.replace("Coin name", "<b>Nombre</b>")
    except:
        pass
    try:
        texto = texto.replace("Address:", "<b>Contrato:</b>")
    except:
        pass
    try:
        texto = texto.replace("Platform", "<b>BlockChain</b>")
    except:
        pass
    try:
        texto = texto.replace("Time", "<b>Hora</b>")
    except:
        pass
    try:
        texto = texto.replace("Liquidity", "<b>Liquidéz</b>")
    except:
        pass
    try:
        texto = texto.replace("Slippage (estimated)", "<b>Slippage estimado</b>")
    except:
        pass
    try:
        texto = texto.replace("Insider info received for possible CMC listing. Coin not listed anywhere yet (listing in 15 minutes aprox.) Buy now to be the first (first pump).", "<i>Información privilegiada recibida por posible listado en CMC. El token NO está listado en ningún sitio todavía(se lista en 15 minutos aprox. Compra ahora antes del primer Pump!</i>")
    except:
        pass
    try:
        texto = texto.replace('This is the first time the coin appear in the official CMC API. Its unranked pending to be listed (second pump).', '<i>Esta es la primera vez que el token aparece en la API oficial de CMC. Todavía no se encuentra rankeado (Segundo Pump!) </i>')
    except:
        pass     
    try:
        texto = texto.replace('The coin is officially listed in CMC and appears in the recently added coins (third pump).', '<i>El token ha sido oficialmente listado en CMC y ya aparece en el apartado "Agregado recientemente"(Tercer Pump!)</i>')
    except:
        pass      

    pooCoin = text.split('Poocoin: ')[1].split(' ')[0] 
    bscScan = text.split('BSC Scan: ')[1].split(' ')[0]   
    staySafu = text.split('Stay Safu: ')[1].split(' ')[0] 
    textoContrato = text.split('Address:         ')[1].splitlines()[0]
    texto = texto.replace(textoContrato, "<code>" + textoContrato + "</code>")
    if "🔴" in texto:
        await tgclient.send_message(id_CoinmarketFast_ES, texto, buttons=[[Button.url('POOCOIN', pooCoin)],[Button.url('BSC SCAN', bscScan), Button.url('STAY SAFU SCAN', staySafu)]], parse_mode='html')                         
    else:
        await tgclient.send_message(id_CoinmarketFast_ES, texto, buttons=[[Button.url('POOCOIN', pooCoin)],[Button.url('BSC SCAN', bscScan), Button.url('STAY SAFU SCAN', staySafu)]], parse_mode='html', silent=True)

tgclient.start()
tgclient.run_until_disconnected()
