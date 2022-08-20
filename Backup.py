from pyrogram import Client as Alpha, filters
from pyrogram.types import Message
from config import *
from sqldb import *
from pyrogram.errors import FloodWait
import asyncio

Alf = Alpha("yashu-alpha", api_id = API_ID, api_hash = API_HASH, session_string = STRING_SESSION)

@Alf.on_message(filters.command("backup", "$"))
async def back(_, m):
    if not m.from_user.is_self:
        return
    if str(m.chat.id)[0] == "-":
        return await eor(_, m, "Only can backup private chats...")
    await eor(_, m, "Backing up chat.....")
    ch = _.get_chat_history(m.chat.id)
    MSG_ID = []
    ok = await m.reply("forwarding messages....")
    async for i in ch:
        MSG_ID.append(i.id)
    await eor(_, m, f"{len(MSG_ID)} messages found...")
    b = 0
    a = 0
    n = len(MSG_ID)//50
    for id in MSG_ID:
        try:
            await _.forward_messages(LOG, m.chat.id, id)
            a += 1
            b += 1
        except FloodWait as e:
            flood_time = 10
            await ok.edit(f"sleeping for {flood_time}s..")
            await asyncio.sleep(flood_time)
        if n == a:
            try:
                await ok.edit(f"{b} messages backed up.....")
            except:
                pass
            a = 0
    await ok.delete()
    return await eor(_, m, "all msges backed up successfully...")
        

if YA == "YashuAlpha":
    Alf.run()
    print("Pyro adder started successfully 🇮🇳🎊🎉")
else:
    print("password you entered is wrong")
