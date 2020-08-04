#gets stuff to make bot (pulling necessary info)
import discord
import os
from discord.ext import commands, tasks
from itertools import cycle
from discord.ext.commands import Bot
import random

client  = commands.Bot(command_prefix = ".")

status = cycle(["My bro is eating", "Im watching TV", "My dad is on his phone"])

@client.event
async def on_ready():
    print("I'm ready!")
   #await client.change_presence(status=discord.Status.idle, activity=discord.Game("Under construction..."))
    change_status.start()

@client.event
async def on_member_join(member):
    print(f"{member} has joined the server!")

@client.event
async def on_member_remove(member):
    print(f"{member} has left the server!")    

@client.command(aliases = ["8ball", "balls"])
async def _8ball(ctx, *, question):
    
    responses = ["Yes", "No", "Maybe"]
    await ctx.send(f"Question: {question} \n Answer: {random.choice(responses)}")

@client.command()
async def clear(ctx, amount = 3):
    await ctx.channel.purge(limit = amount)

@client.command()
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason = reason)

@client.command(aliases = ['magicconch','conch'])
async def _mconch(ctx, *,question):
    responses = ["Yes","No","Maybe"]
    await ctx.send(f'Question: {question} \n Answer: {random.choice(responses)}')



@tasks.loop(seconds = 15)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))



#Event - code that executes when the bot detects something in particular 
# @client.event
# async def on_ready():
#     print("IM READY!")

client.run(os.environ.get('MendBot_token'))

