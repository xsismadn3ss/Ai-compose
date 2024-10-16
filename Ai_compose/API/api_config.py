from .models import *
from .api_client import Routes, API
from os import getenv
from dotenv import load_dotenv

load_dotenv()

routes = Routes(
    tones="/tones/",
    scales="/scales/",
    chords="/chords/",
    notes="/notes/",
    login="/login/",
    register="/register/",
    account="/account/{}",
    chat="/chat/{}",
    new_chat="/chat/create/",
)

api = API(
    server_url=getenv("SERVER_URL"),
    headers={"Accepts": "*/*", "Authorization": "", "Content-Type": "application/json"},
)

# completado ✅
user = User(
    api=api, login=routes.login, register=routes.register, account=routes.register
)
chat = Chat(api=api, chat=routes.chat, new_chat=routes.new_chat)

# esperando implementación de backtracking en el backend...
tones = Tones(api=api, tones=routes.tones)
notes = Notes(api=api, notes=routes.notes)
scales = Scales(api=api, scales=routes.scales)
chords = Chords(api=api, chords=routes.chords)