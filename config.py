import os

from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

if os.path.exists(".env"):
    load_dotenv(".env")

API_ID = int(os.getenv("API_ID"13124829"))
API_HASH = os.getenv("API_HASH"03ed39256d133866b23b2d37ee7f3d67")
SESSION = os.getenv("SESSION"-AgBw-KgLWHTtKFwxoTM8mxIenrHpeYjyD114pN2OX1bLP25M9trR0RlqoDFLHgxb7QJAO-pNs7FZXWGuUf-IMXtCK-FWc5_tAgcxQ6M9yG3rgZ94ljZ87W_XIjqNSLtBOiXV7JgucbI9UV6rDQvqqj0xLqePglCKs_Z2aGlhjEWWcBqAPMnc1ejggYjl8-yCzupkIOHjFkRxAnm4G-0T58jbBgt9ibHqcOuO5v2Yf1KtEkwc8-y2Ul6KMxfe7ipBXoOQ40V68a7c9sOo31qrvmJwVUJtDog7Nhlt82coV0JRWkBw1U7v4I1qUqNRAqQYwDV168pq4GxMgmMvb0vfoFEFAAAAATqRNTEA-)
OWNER_NAME = os.getenv("OWNER_NAME"jano")
CHANNEL = os.getenv("CHANNEL"akd444s")
PHOTO_CH = os.getenv("PHOTO_CH")
HNDLR = os.getenv("HNDLR", "#")
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS").split()))


contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)

bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="Musicjepthon"))
call_py = PyTgCalls(bot)
