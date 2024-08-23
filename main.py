import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv, find_dotenv
import os

# Connect the path with your '.env' file name
load_dotenv()


# Set the token.
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Define whatever this is.
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=".",intents=intents)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)

@bot.tree.command(name="echo",description="echo text")
async def slash_command(interaction:discord.Interaction, msg: str):
    
    await interaction.response.send_message("‎", ephemeral=True)

    await interaction.followup.send(msg)


    #delete the response here




@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    await bot.tree.sync()



bot.run(DISCORD_TOKEN)


    
