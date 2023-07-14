import logging, asyncio

from os import environ
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait

logging.basicConfig(level=logging.ERROR)
       

User     = Client(name = "AcceptUser", api_id=environ.get("API_ID"), api_hash=environ.get("API_HASH"), session_string = environ.get("SESSION"))


@User.on_message(filters.command(["run", "approve", "start"], [".", "/"]) & (filters.group | filters.channel))
async def approve(client: User, message: Message):e):
    Id = message.from_user.id
    await message.delete(True)
 
    try:
       while True: # create loop is better techniq 🙃
           try:
               await User.approve_all_chat_join_requests(Id)
           except FloodWait as t:
               asyncio.sleep(t.value)
               await User.approve_all_chat_join_requests(Id)
           except Exception as e:
               logging.error(str(e))
    except FloodWait as s:
        asyncio.sleep(s.value)
        while True:
           try:
               await User.approve_all_chat_join_requests(Id)     
           except FloodWait as t:
               asyncio.sleep(t.value)
               await User.approve_all_chat_join_requests(Id) 
           except Exception as e:
               logging.error(str(e))

    msg = await client.send_message(NJ, "**Task Completed** ✓ **Approved Pending All Join Request**")
    await asyncio.sleep(3)
    await msg.delete()


logging.info("Bot Started....")
User.run()







