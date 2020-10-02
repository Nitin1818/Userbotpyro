from pyrogram import (Client, filters)
from datetime import datetime


@Client.on_message(filters.me & filters.command(['alive'], ['.', '/']))
def live(app, message):
     message.edit(f"**UserBot running** \n"
                  f"**Timestamp:** `{datetime.now()}`\n"
                  f"**Repo:** [GitHub](https://github.com/Nitin1818/Userbotpyro)")
