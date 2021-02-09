#    Copyright (C) DevsExpo 2020-2021
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from telethon import functions
from fridaybot.function import get_all_admin_chats, is_admin, is_nsfw
import requests
import string 
import random 
from fridaybot.modules.sql_helper.nsfw_watch_sql import add_nsfwatch, rmnsfwatch, get_all_nsfw_enabled_chat, is_nsfwatch_indb

@friday.on(friday_on_cmd(pattern="anw$"))
async def nsfw_watch(event):
    if not event.is_group:
        await event.edit("You Can Only Nsfw Watch in Groups.")
        return
    if not await is_admin(event, bot.uid): 
        await event.edit("`You Should Be Admin To Do This!`")
        return
    if is_nsfwatch_indb(str(event.chat_id)):
        await event.edit("`This Chat is Has Already Nsfw Watch.`")
        return
    add_nsfwatch(str(event.chat_id))
    await event.edit(f"**Added Chat {event.chat.title} With Id {event.chat_id} To Database. This Groups Nsfw Contents Will Be Deleted And Will Will Be Logged in Logger Groupp**")

@friday.on(friday_on_cmd(pattern="rmnw$"))
async def disable_nsfw(event):
    if not event.is_group:
        await event.edit("You Can Only Disable Nsfw Mode in Groups.")
        return
    if not await is_admin(event, bot.uid): 
        await event.edit("`You Should Be Admin To Do This!`")
        return
    if not is_nsfwatch_indb(str(event.chat_id)):
        await event.edit("This Chat is Has Not Enabled Nsfw Watch.")
        return
    rmnsfwatch(str(event.chat_id))
    await event.edit(f"**Removed Chat {event.chat.title} With Id {event.chat_id} From Nsfw Watch**")
    
warner_starkz = get_all_nsfw_enabled_chat()

if len(warner_starkz.chat_id) != 0:
    @bot.on(events.NewMessage())        
    async def ws(event):
        if not is_nsfwatch_indb(str(event.chat_id)):
            return
        if not event.media:
            return
        if not is_admin(event, bot.uid):
            return
        hmmstark = await is_nsfw(event)
        his_id = event.sender_id
        if hmmstark is True:
            try:
                await event.delete()
            except:
                pass
            lolchat = await event.get_chat()
            ctitle = event.chat.title
            if lolchat.username:
                hehe = lolchat.username
            else:
                hehe = event.chat_id
            wstark = await event.client.get_entity(his_id)
            if wstark.username:
                ujwal = wstark.username
            else:
                ujwal = wstark.id
            try:
                await borg.send_message(Config.PRIVATE_GROUP_ID, f"**#NSFW_WATCH** \n**Chat :** `{hehe}` \n**User / Bot :** `{ujwal}` \n**Chat Title:** `{ctitle}`")       
            except:
                pass
        else:
            return
