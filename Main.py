import sys
import os

import logging
import discord
from discord.ext import commands
import random
import tweepy, time
import urllib3
import math
import calendar, datetime, time
import requests
import asyncio


CurrentClass = 1

if CurrentClass == 1: #Advaned Linear Algebra
    Token = '[Groupme Account Tocken]'
    BotID = '[Specific ID for Bot]'
    GroupID = '[Self Explainatory]'
    DiscordToken = '[Tocken Discord Uses for the Bot]'
    MainDiscordChannel = '[Which Discord Channel to Post Messages Too]'
elif CurrentClass == 2: #Introduction to Programming
    Token = '[Groupme Account Tocken]'
    BotID = '[Specific ID for Bot]'
    GroupID = '[Self Explainatory]'
    DiscordToken = '[Tocken Discord Uses for the Bot]'
    MainDiscordChannel = '[Which Discord Channel to Post Messages Too]'
elif CurrentClass == 3: #Leadership Theory and Practice
    Token = '[Groupme Account Tocken]'
    BotID = '[Specific ID for Bot]'
    GroupID = '[Self Explainatory]'
    DiscordToken = '[Tocken Discord Uses for the Bot]'
    MainDiscordChannel = '[Which Discord Channel to Post Messages Too]'
elif CurrentClass == 4: #Org Leadership and Supervision
    Token = '[Groupme Account Tocken]'
    BotID = '[Specific ID for Bot]'
    GroupID = '[Self Explainatory]'
    DiscordToken = '[Tocken Discord Uses for the Bot]'
    MainDiscordChannel = '[Which Discord Channel to Post Messages Too]'

request_params = {'token': Token}
response_messages = \
requests.get('https://api.groupme.com/v3/groups/' + GroupID + '/messages', params=request_params).json()[
    'response']['messages']
print(response_messages)
print("HERE IS THE LAST 20 MESSAGES\n--------------------------\n")
last_messages = ["" for y in range(20)]
i = 0
for message in response_messages:
    print(message['text'])
    last_messages[i] = message['text']
    i += 1
time.sleep(1)


# DISCORD CREATE EVENT ---------------------------------------------
bot = commands.Bot(command_prefix='', description='''I am the class bot, you know?''')

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

#discord.version_info
print(discord.__version__)

#Runs every second
async def updateDiscordWithGroupme():
    await bot.wait_until_ready()
    while not bot.is_closed:
        response_messages = requests.get('https://api.groupme.com/v3/groups/' + GroupID + '/messages', params=request_params).json()['response']['messages']
        #print(last_messages)
        for message in response_messages:
            #print(message['text'])
            if message['text'] not in last_messages:
                if message['sender_type'] != 'bot':
                    #print("-------------------------------------------------------")
                    await bot.send_message(bot.get_channel(MainDiscordChannel),content=message['name'] + ": " + message['text'])
        i = 0
        for message in response_messages:
            last_messages[i] = message['text']
            i += 1

        await asyncio.sleep(4)

def variable_set():

    global testing

    testing = False

def saveglobalints(): #Misc Variables related to people
    global globalints

    F = open("globalints.txt", 'w')
    for x in range(0, len(globalints)):
        F.write(str(globalints[x]) + "\n")
    F.close()

def loadglobalints():
    global globalints

    F = open("globalints.txt", 'r')
    for x in range(0,len(globalints)):
        v = F.readline()
        if v == '':
            v = 0
        globalints[x]= int(v)
    F.close()

def setglobalints(varslot,var):

    globalints[varslot-1] = var
    saveglobalints()

def getglobalints(varslot):
    return globalints[varslot-1]

async def delete_delay(message):
    time.sleep(10)
    await bot.delete_message(message)

def UTC_time_to_epoch(timestamp):
    return calendar.timegm(timestamp.utctimetuple())

async def addrole(member,role):
    print("Trying to add " + str(role))
    rolelist = ""
    for x in range(0, len(member.roles)):
        rolelist = rolelist + str(member.roles[x].id)
        rolelist += " "

    if role not in rolelist:
        await bot.add_roles(member, discord.Object(id=role))

async def removerole(member,role):
    print("Trying to remove "+str(role))
    rolelist = ""
    for x in range(0, len(member.roles)):
        rolelist = rolelist + str(member.roles[x].id)
        rolelist += " "

    if role in rolelist:
        await bot.remove_roles(member, discord.Object(id=role))



# DISCORD EVENTS ---------------------------------------------
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    variable_set()



#@bot.event
#async def on_server_join(server):



@bot.event
async def on_message(message):
    await bot.process_commands(message)

    if not message.author.bot:
        to_send = str(message.author)[:-5] + ": "+str(message.clean_content)
        post_params = {'bot_id': BotID, 'text': to_send}
        requests.post('https://api.groupme.com/v3/bots/post', params=post_params)


#@bot.event
#async def on_typing(channel,user,when):

#@bot.event
#async def on_member_join(member):

#@bot.event
#async def on_member_remove(member):

#@bot.event
#async def on_member_update(before,after):

#@bot.event
#async def on_channel_create(channel):

#@bot.event
#async def on_channel_delete(channel):

#@bot.event
#async def on_server_role_create(role):

#@bot.event
#async def on_server_role_delete(role):

#@bot.event
#async def on_server_role_update(before,after):

#@bot.event
#async def on_member_ban(member):

#@bot.event
#async def on_member_unban(server,user):


@bot.command(pass_context = True)
async def nothing(ctx):
    """Does Absolutely Nothing, trust me"""
    await bot.delete_message(ctx.message)


@bot.command(pass_context = True)
async def add(ctx, left : int, right : int):
    """Adds two numbers together."""
    await bot.say(str(left) + " + " + str(right) + " = " + str(left + right), tts=True)

@bot.command(pass_context = True)
async def sub(ctx, left : int, right : int):
    """Subtracts two numbers."""
    await bot.say(str(left) + " - " + str(right) + " = " + str(left - right), tts=True)

@bot.command(pass_context = True)
async def mult(ctx, left : int, right : int):
    """Multiplies two numbers together."""
    await bot.say(str(left) + " x " + str(right) + " = " + str(left * right), tts=True)

@bot.command(pass_context = True)
async def div(ctx, left : int, right : int):
    """Divides two numbers."""
    await bot.say(str(left) + " / " + str(right) + " = " + str(left / right), tts=True)

@bot.command(pass_context = True)
async def roll(ctx, start : int, end : int):
    """Rolls a dice (min,max)"""
    result = random.randint(start, end)
    await bot.say("And the result is.... " + str(result), tts=True)

@bot.command(pass_context = True)
async def choose(ctx, *choices : str):
    """Chooses between multiple choices."""
    if ctx.message.channel.id == MainDiscordChannel:
        await bot.say(random.choice(choices), tts=True)

@bot.command(pass_context = True)
async def joined(ctx, member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member), tts=True)

@bot.group(pass_context=True)
async def cool(ctx):
    """Says if a user is cool. May also insult you."""
    #random.seed(x)
    if ctx.message.channel.id == MainDiscordChannel:
        if ctx.invoked_subcommand is None:
            response = random.randint(0, 5)
            if response == 0:
                await bot.say('No, {0.subcommand_passed} is not cool'.format(ctx), tts=True)
            elif response == 1:
                await bot.say('Yes, {0.subcommand_passed} is cool... I guess'.format(ctx), tts=True)
            elif response == 2:
                await bot.say('Figure it out yourself...', tts=True)
            elif response == 3:
                await bot.say('{0.subcommand_passed} might be cool, but I doubt it'.format(ctx), tts=True)
            elif response == 4:
                await bot.say('Yes, {0.subcommand_passed} is really cool'.format(ctx), tts=True)
            elif response == 5:
                await bot.say('{0.subcommand_passed} is the coolest of them all'.format(ctx), tts=True)


@cool.command(name='bot')
async def _bot():
    """Is the bot cool?"""
    await bot.say('Yes, the bot is cool.')

@cool.command(name='nothing')
async def _bot():
    """Is the bot cool?"""
    await bot.say('Are you trying to pull something here?')


@bot.command(pass_context = True)
async def gg(ctx):
    """Comments on the past game that was played, exclaiming how good it was."""
    if ctx.message.channel.id == MainDiscordChannel:
        k = random.random(0,7)
        if k >= 6:
            await bot.say('Stupendous! A great game it was! Jolly good show!', tts=True)
        elif k >= 5:
            await bot.say('I agree that the state of this game was good.', tts=True)
        elif k >= 4:
            await bot.say('Indeed good sir... that was a fabulous game.', tts=True)
        elif k > 3:
            await bot.say('Yes... that was a good game.', tts=True)
        elif k > 2:
            await bot.say('We are playing a game?', tts=True)
        elif k > 1:
            await bot.say('What are you talking about?', tts=True)
        elif k <= 0:
            await bot.say('What do you mean??? That game sucked!', tts=True)

@bot.command(pass_context=True)
async def hey(ctx):
    """Is for horses"""
    if ctx.message.channel.id == MainDiscordChannel:
        a = str(ctx.message.author)
        await bot.say('Hi '+a[:-5], tts=True)

@bot.command(pass_context=True)
async def Hey(ctx):
    """Is for Horses"""
    if ctx.message.channel.id == MainDiscordChannel:
        a = str(ctx.message.author)
        await bot.say('Whats up '+a[:-5], tts=True)

@bot.command(pass_context=True)
async def hi(ctx):
    """For those times when you just want someone to talk to."""
    if ctx.message.channel.id == MainDiscordChannel:
        a = str(ctx.message.author)
        await bot.say('Hello '+ a[:-5], tts=True)

@bot.command(pass_context=True)
async def Hi(ctx):
    """For those wanting attention."""
    if ctx.message.channel.id == MainDiscordChannel:
        a = str(ctx.message.author)
        await bot.say('Well hello there, '+ a[:-5], tts=True)

@bot.command(pass_context = True)
async def hello(ctx):
    """The lonely people command."""
    if ctx.message.channel.id == MainDiscordChannel:
        await bot.say('Howdy Doody', tts=True)

@bot.command(pass_context=True)
async def Hello(ctx):
    """Just a casual greeting"""
    if ctx.message.channel.id == MainDiscordChannel:
        await bot.say('Howdy', tts=True)

@bot.command(pass_context=True)
async def Howdy(ctx):
    """For those who like to roleplay as a cowboy"""
    if ctx.message.channel.id == MainDiscordChannel:
        await bot.say('Greeting partner', tts=True)

@bot.command(pass_context=True)
async def howdy(ctx):
    """For those who like to roleplay as a cowboy but also dont like caps"""
    if ctx.message.channel.id == MainDiscordChannel:
        await bot.say('Yeee haw! What a fine day it is!', tts=True)

@bot.command(pass_context=True)
async def console(ctx, *args):
    """Prints a message to the console"""
    if ctx.message.channel.id == MainDiscordChannel:
        print(args)
        await bot.say('I sent the message!')

bot.loop.create_task(updateDiscordWithGroupme())
bot.run(DiscordToken)

