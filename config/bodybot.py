
import discord
from discord.ext import commands
from discord import client
from confBot import settings
import requests

bot = commands.Bot(command_prefix = settings['prefix'])



@bot.command() # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
async def hello(ctx): # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author # Объявляем переменную author и записываем туда информацию об авторе.
    await ctx.send(f'Hello, {author.mention}!') # Выводим сообщение с упоминанием автора, обращаясь к переменной author.
    


@bot.command()
async def listOfGuys(ctx):
    await ctx.message.channel.send("Введите никнеймы пользователей через пробел:")
    @bot.event  
    async def on_message(message):
        if message.author.bot:
            return  # ignore bots
        else:
            mySet = set()
            for i in message.content.split(" "):
                handle = i
                try:
                    
                    x = requests.get(f'https://codeforces.com/api/user.status?handle={handle}&from=1&count=1000000000').json()
                    if(x['status'] == 'FAILED'):
                        await message.channel.send(f"Данного ника не сущесвтует: {handle}")
                        continue
                except: 
                    await message.channel.send(f"Ошибка при получении задач по пользователю")
                    continue

                for i in x["result"]:
                    if(i["verdict"] == "OK" ):
                        mySet.add(i["problem"]["name"])
           
            y = requests.get(f' https://codeforces.com/api/problemset.problems').json()["result"]["problems"]
            
            i = 0
            while((y[i]["name"] in mySet)== True):
                i += 1
            contestId = y[i]["contestId"]
            index = y[i]["index"]
            await message.channel.send(f'https://codeforces.com/problemset/problem/{contestId}/{index}')

bot.run(settings['token']) # Обращаемся к словарю settings с ключом token, для получения токена
#https://discord.com/api/oauth2/authorize?client_id=982665838874214430&permissions=8&scope=bot