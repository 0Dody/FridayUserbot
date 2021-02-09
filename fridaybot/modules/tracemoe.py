#    Copyright (C) Midhun KM 2020-2021
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

import tracemoepy
import os
import glob
import asyncio
import math
import os
import time
from telethon.tl.types import DocumentAttributeAudio
from fridaybot.function import progress, humanbytes, time_formatter, convert_to_image
from fridaybot.function.FastTelethon import upload_file

@friday.on(friday_on_cmd(pattern="animereverse$"))
async def anime_name(event):
    tracemoe = tracemoepy.tracemoe.TraceMoe()
    file_s = await convert_to_image(event, friday)
    c_time = time.time()
    await event.edit("`Searching For This Anime. Bruh.`")
    try:
      ws = tracemoe.search(file_s, encode=True)
    except:
      await event.edit("`SomeThing is Sad, Failed.`")
      return
    video = tracemoe.natural_preview(ws)
    with open('preview@FridayOT.mp4', 'wb') as f:
      f.write(video)
    starkfile = 'preview@FridayOT.mp4'
    warner = await upload_file(
            file_name=f"{ws.docs[0].title}.mp4",
            client=borg,
            file=open(starkfile, 'rb'),
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(
                    d, t, event, c_time, "Uploading Your Preview!", starkfile
                )
            ),
        )
    await event.delete()
    await friday.send_file(event.chat_id,
      warner,
      caption=str(ws.docs[0].title)
      )
