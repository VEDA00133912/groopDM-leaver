import discord  
import os
from dotenv import load_dotenv
load_dotenv()

client = discord.Client()

TOKEN = os.getenv("TOKEN")

# もし退出したくないグループDMがある場合はここにIDを書いておく
# EXCLUDE_DM_IDS = ["", ""] 

@client.event
async def on_ready():
    print(f"{client.user} is online！")
    group_dms = [dm for dm in client.private_channels if isinstance(dm, discord.GroupChannel)]
    left_count = 0
    for dm in group_dms:
      # EXCLUDE_DM_IDSを入力した場合はこれを書いておく
      # if str(dm.id) not in EXCLUDE_DM_IDS:
            await dm.leave()
            left_count += 1
    print(f"{left_count}件のグループDMからの退出が完了しました")

client.run(TOKEN)
