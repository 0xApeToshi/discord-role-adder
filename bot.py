# bot.py
import os
import pandas as pd
from discord.utils import get

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
ROLE_ID = 943555622148915291

intents = discord.Intents().all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")

    # for guild in client.guilds:
    #     for member in guild.members:
    #         print("Member:", member)
    #         return

    df = pd.read_csv("list.csv")

    # for id in df["discord id"]:
    #     print("Discord id:", id)

    guild = client.guilds[0]
    role = get(guild.roles, id=ROLE_ID)
    print("Assigning role:", role)

    users = await guild.query_members(user_ids=list(df["discord id"]))

    for user in users:
        try:
            await user.add_roles(role)
            print("[ADDED]:", user)
        except Exception as e:
            print("[EXCEPTION]:", e)
    print("Done!")
    client.close()

client.run(TOKEN)
