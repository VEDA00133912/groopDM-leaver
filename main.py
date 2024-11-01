import discord  
import os
from dotenv import load_dotenv
load_dotenv()

client = discord.Client()

TOKEN = os.getenv("TOKEN")

@client.event
async def on_ready():
    print(f"{client.user} is online！")
    group_dms = [dm for dm in client.private_channels if isinstance(dm, discord.GroupChannel)]
    for dm in group_dms:
        await dm.leave()
    print(f"{len(group_dms)}件のグループDMからの退出が完了しました")

client.run(TOKEN)
