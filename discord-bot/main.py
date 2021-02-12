import discord
import os
import requests
import json
import time
import random
from random import randrange
import aiohttp


client = discord.Client()


@client.event
async def on_ready():
  print('bot {0.user} activated'.format(client))
  await client.change_presence(activity=discord.Game(name="trading"))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('diana'):
      await message.channel.send(' dianita en medio karlos?..XD')

  if message.content.startswith('chapa porfa'):
      await message.channel.send('vale em muteju')

  if message.content.startswith('andrea'):
      await message.channel.send('puc dirli algo?')
  if message.content.startswith('no'):
      await message.channel.send('vale em muteju i menvaig al parke')
      await client.change_presence(activity=discord.Game(name=" en el parke "))

  if message.content.startswith('porfa'):
      await message.channel.send('no')

  if message.content.startswith('go'):
      await message.channel.send('chapa porfa')

  if message.content.startswith('e'):
      await message.channel.send('go?')
      await client.change_presence(activity=discord.Game(name="Free fire"))

  if message.content.startswith("ep"):  # command to start quessing game
      channel = message.channel
      # message that tells about the start of the game
      await channel.send("adivina!")

      # picking random number from 1 - 10 and printing it
      number1 = random.randint(1, 10)
      print(number1)

      number2 = str(number1)  # converting int to str

       def check(m):
            return m.content == number2 and m.channel == channel  # checking answers

        msg = await client.wait_for('message', check=check)
        # tells who got the answer
        await channel.send("correct, {.author}" .format(msg))
  # bitcoin current price
  if message.content.startswith("bitcoin"):
    channel = message.channel
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
      raw_response = await session.get(url)
      response = await raw_response.text()
      response = json.loads(response)
      await channel.send("Bitcoin price is: $" + response['bpi']['USD']['rate'])


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f' {member.name}, type for commands'
    )

client.run(os.getenv('TOKEN'))
