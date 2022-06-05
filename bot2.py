from array import array
import discord
from discord.ext import commands
from discord import client
import logging
from discord.utils import get
import requests
import csv
import config
from datetime import datetime
from datetime import date
from threading import Thread
import time

settings = {
'token': 'OTgyODI0ODY1ODcyNjE3NDgy.G-qumj.H_BQ5BJjCnm0jZ5Fr6uS4wcntYeoYK35rRvg6o',
'bot': 'BotVezdekod2.0',
'id': 982824865872617482,
'prefix': '!'
}





students = []

 
with open('text.csv', newline='',  encoding='utf-8') as File:  
    reader = csv.reader(File)
    
    for row in reader:
        if(row != []):
            students.append(row)

print(students[0])

students[2] = [s.split(',') for s in students[2]]
print(students)
studList = []
day = []
for i in range(len(students[0])):
    day.append([0]*24*7)
    studList.append([])

for i in range(len(students[0])):
    k = 0
    j = 8
    if(students[1][i].split(" - ")[0] == 'понедельник'):
        k = 1
    elif(students[1][i].split(" - ")[0] == 'вторник'):
        k = 2
    elif(students[1][i].split(" - ")[0] == 'среда'):
        k = 3
    elif(students[1][i].split(" - ")[0] == 'четверг'):
        k = 4
    elif(students[1][i].split(" - ")[0] == 'пятница'):
        k = 5
    elif(students[1][i].split(" - ")[0] == 'суббота'):
        k = 6
    elif(students[1][i].split(" - ")[0] == 'воскресенье'):
        k = 7

    if(students[1][i].split(" - ")[1] == 'понедельник'):
        j = 1
    elif(students[1][i].split(" - ")[1] == 'вторник'):
        j = 2
    elif(students[1][i].split(" - ")[1] == 'среда'):
        j = 3
    elif(students[1][i].split(" - ")[1] == 'четверг'):
        j = 4
    elif(students[1][i].split(" - ")[1] == 'пятница'):
        j = 5
    elif(students[1][i].split(" - ")[1] == 'суббота'):
        j = 6
    elif(students[1][i].split(" - ")[1] == 'воскресенье'):
        j = 7
    print(students[1][i].split(" - "), "\n")
    print(k, " ", j)

    if(j > k):
        f = int(students[2][i][0].split(" - ")[0].split(":")[0])
        z = int(students[2][i][0].split(" - ")[1].split(":")[0])
        
        for m in range(k,j+1):
            
            for p in range(f,z+1):
                
                day[i][24*m-24+p] = 1
    else:
        f = int(students[2][i][0].split(" - ")[0].split(":")[0])
        z = int(students[2][i][0].split(" - ")[1].split(":")[0])
        
        for m in range(k,8):
            
            for p in range(f,z+1):
                
                day[i][24*m-24+p] = 1
        for m in range(1,j+1):
            
            for p in range(f,z+1):
                
                day[i][24*m-24+p] = 1




bot = commands.Bot(command_prefix = settings['prefix'])



def loop():
    while True:
        begFlag = 0
        today = date.today().weekday()
        now = datetime.now().hour
        
        for n, i in enumerate(day):
            if(i[today*24+now]==1 and begFlag==0):
                
                #Раскомментить для проверки
                # f =  open("log.txt", mode="w", encoding='utf-8')
                # for i in studList[n]:

                #     f.write(i)


                #Закомментить для проверки 
                studList[n] = []

                begFlag = 1
            elif(i[today*24+now]==0 and begFlag==1):
                begFlag = 0
                
                f =  open("log.txt", mode="w", encoding='utf-8')
                for i in studList[n]:
                    f.write(i)

        time.sleep(1)


for _ in range(1):
    t = Thread(target=loop)
    t.daemon = True
    t.start()





@bot.event
async def on_voice_state_update(member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
    for i in range(len(students[0])):
        if((str(member) in students[3][i])==True and str(after.channel)==students[0][i]):
            today = date.today().weekday()
            now = datetime.now().hour
            if(day[i][today*24+now] == 1):
                studList[i].append(str(member) + " ")
                
                    
    

   


bot.run(settings['token'])


try:
    while True:
        time.sleep(0.05)
except KeyboardInterrupt:
    print("Stop script")