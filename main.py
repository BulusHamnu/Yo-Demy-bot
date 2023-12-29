

from replit import db 
import discord
from discord.ext import commands
import os

intents = discord.Intents().all()

bot = commands.Bot (command_prefix = '!',intents = intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

    print("yo demy is running successful!")
  
@bot.event
async def on_message (message) :
    if message.author == bot.user :
        return 
    if message.content.lower().startswith('hey') :
        await message.channel.send('hey,how are you doing?')
    if message.content.lower().startswith ("hello") :
       await message.channel.send ("welcome mate 💪🏿")
    await bot.process_commands(message)
"""
#welcoming event
@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="welcome")
    if channel:
        welcome_message = (
            f"@everyone {member.name} just joined the server.\n"
            f"{member.mention}, welcome to Demy Thekidd server we are glad to have you here. don't forget to check the #rules channel and also follow Demy Thekidd on Instagram: "
            f"https://instagram.com/demy_thekidd?igshid=YzU1NGVlODEzOA== for updates... Thank you."
        )
        await channel.send(welcome_message)
    role = discord.utils.get(member.guild.roles, name="fan")

    if role and role not in member.roles:
        await member.add_roles(role)
"""
#all commands
#command for sending dm
@ bot.command(name = "Send_dm", help = "send a direct message to a user")
async def Send_dm(ctx, user: discord.User, *, message=None):
  message = message or "This Message is sent via DM"
  await user.send(message)

#command for posting message to a channel
@bot.command(name="new_post", help="post some message to a specific channel")
async def send_message(ctx, channel_name, *, message=None):
    # Get the channel object by name
    channel = discord.utils.get(ctx.guild.channels, name=channel_name)

    if channel:
        message = message or "Hello 👋"
        await channel.send(message)
    else:
        await ctx.send(f"Channel '{channel_name}' not found.")

#command for music
@bot.command(name = "lyric_of",help = "play demy's songs")
async def play_song (ctx,lyric_name) :
  lyric = db [lyric_name]
  await ctx.send (f"{ctx.author.mention} {lyric}")

@bot.command(name = "del_lyric", help = "del lyrics from data base")
async def stop_song (ctx, lyric_name) :
  del db [lyric_name] 

@bot.command(name = "add_lyric", help = "add demy Song lyrics")
async def add_lyric (ctx,lyric_name,*,lyric) :
  db [lyric_name] = lyric

token = os.environ['Token']

if __name__ == "__main__":
    bot.run(token)
