import discord
from discord.ext import commands, tasks
from itertools import cycle
import random
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

bot_status = cycle(["Type !commands for help", "Taking over the World", "Making Spaghetti Code"])

@tasks.loop(hours=1)

async def change_status():
    await client.change_presence(activity=discord.Game(next(bot_status)))

@client.event
async def on_ready():
    print("Success: Bot is connected to Discord")
    change_status.start()

@client.command()
async def commands(ctx):
    embed_message = discord.Embed(title ="Command List", description="Minion-Bot can respond to the following commands:")

    embed_message.add_field(name="!affirmation", value="", inline=False)
    embed_message.add_field(name="!cop", value="", inline=False)
    embed_message.add_field(name="!engineer", value="", inline=False)
    embed_message.add_field(name="!ephemeral", value="", inline=False)
    embed_message.add_field(name="!lisa_frank", value="", inline=False)
    embed_message.add_field(name="!pray", value="", inline=False)
    embed_message.add_field(name="!recruiter", value="", inline=False)
    embed_message.add_field(name="!rules", value="", inline=False)
    embed_message.add_field(name="!salary", value="", inline=False)
    embed_message.add_field(name="!soon", value="", inline=False)
    await ctx.send(embed = embed_message)

@client.command()
async def affirmation(ctx):
    list = ["You are enough.", "You are in the right place, doing the right thing, at the right time.", "You're allowed to take up take space.", "Progress not perfection.", "Do it with the audacity of a mediocre white man.", "I possess the qualities I need to be successful.", "I persevere. I am relentless. I keep going.", "I need to give myself credit for what I do every day.", "I acknowledge my fear and I do it anyway.", "I am talented and capable.", "I am proud of what I’ve done and what I’m doing.", "I believe in my skills and talents."]

    await ctx.send(random.choice(list))

@client.command()
async def rules(ctx):
    await ctx.send("The only rule of Hardcore Backend is there are no rules.")

@client.command()
async def pray(ctx):
    await ctx.send("Pray for me <@" + str(927024050767794227) + ">")

@client.command()
async def salary(ctx):
    await ctx.send("While salary/compensation is important to me, my ideal role would also be comprised of things like good team culture, colleagues passionate about the work they do, and benefits. What salary range has been allotted for this position?")

@client.command()
async def engineer(ctx):
    await ctx.send("Hi (name), I'm a software engineer and I noticed that (company) has openings in the engineering department right now. If you have time in the next few weeks, I would love to find a time to chat about your experience working there. Best, (Your Name)")

@client.command()
async def recruiter(ctx):
    await ctx.send("Hi (name), I'm a software engineer and I noticed that (company) has openings in the engineering department right now. If you have time in the next few weeks, I would love to find a time to chat about open roles. Best, (Your Name)")

@client.command()
async def lisa_frank(ctx):
    await ctx.send("https://giphy.com/embed/vVQTaBaY5d6ak")

@client.command()
async def ephemeral(ctx):
    await ctx.send("There's a channel for that! \n https://tenor.com/view/writing-calligraphy-fountain-pen-ephemeral-gif-8071362")

@client.command()
async def cop(ctx):
    await ctx.send("https://tenor.com/view/police-car-cops-serious-gif-14703298")

@client.command()
async def werk_it(ctx):
    await ctx.send("https://tenor.com/view/zyonu-on-zyonu-on-police-rp-zyonu-on-the-toilet-zyonu-in-his-freetime-gif-14494496")

@client.command()
async def soon(ctx):
    await ctx.send("https://cdn3.emoji.gg/emojis/4081_SoonTM.png")

client.run(TOKEN)