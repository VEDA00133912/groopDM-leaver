# groopDM-leaver
Discord.py-selfを使った全グループDMの自動退出
<br>
・`pip install discord.py-self`, `pip install python_dotenv`を実行してdpy-selfとdotenvをインストール<br>
・`python main.py`で実行<br>
・少し待って`ユーザー名#---- is online！`と表示されると自動退出が開始します<br>
・退出が完了するとコンソールに`◯個のグループDMの退出が完了しました`と表示されます
<br>
・もし退出したくないグループDMがある場合はそのグループのIDをDM_IDSに入れておくとそこは除外されます
<br>
```python
import discord  
import os
from dotenv import load_dotenv
load_dotenv()

client = discord.Client()

TOKEN = os.getenv("TOKEN")

# もし退出したくないグループDMがある場合はここにIDを書いておく
# DM_IDS = ["", ""] 

@client.event
async def on_ready():
    print(f"{client.user} is online！")
    group_dms = [dm for dm in client.private_channels if isinstance(dm, discord.GroupChannel)]
    left_count = 0
    for dm in group_dms:
      # DM_IDSを入力した場合はこれを書いておく
      # if str(dm.id) not in DM_IDS:
            await dm.leave()
            left_count += 1
    print(f"{left_count}件のグループDMからの退出が完了しました")

client.run(TOKEN)
```
```python
DM_IDS = ["12345678", "23456789"]

@client.event
async def on_ready():
    print(f"{client.user} is online！")
    group_dms = [dm for dm in client.private_channels if isinstance(dm, discord.GroupChannel)]
    left_count = 0
    for dm in group_dms:
        if str(dm.id) not in DM_IDS:
            await dm.leave()
```
