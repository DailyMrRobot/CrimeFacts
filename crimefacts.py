import os
import random
import discord
import requests
import json
import youtube_dl
import asyncio

from discord.ext import commands
from dotenv import load_dotenv
from discord import FFmpegPCMAudio
from discord import client
intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents)




load_dotenv()
TOKEN = os.getenv('OTUwMzEyODk3NzU2NjcyMDQx.YiXF2g.66yUZ4HlBV7WjxiY5tIQep83wiA')

bot = commands.Bot(command_prefix='.')

@bot.command(name='jd')
async def jeffy(ctx):
    jeffery_dahmer_facts = [
            "When he was put on trial for his horrendous crimes, he was given multiple psychiatric evaluations and it was concluded that he suffered from borderline personality disorder, schizotypal personality disorder, and multiple psychotic disorders.",
            "Before the age of four he was a happy and jovial child, however after he had a double hernia operation just before his fourth birthday. He became quiet and timid.",
            "He liked to dissect animals, especially animals that were killed on the road due to accidents",
            "Jeffrey Dahmer gave the people in his apartment building sandwiches that could've possibly been made from his victims’ flesh.",
            "Jeffrey Dahmer had so many bodies in his apartment that he ran out of room and stored one victim in his bathtub. He proceeded to shower over him everyday for a month!",
            "Jeffrey Dahmer was neglected by his parents in childhood and hadn't even seen his mother for 10 years prior to incarceration. At sentencing, his father and stepmother asked for 10 minutes to say goodbye and hug. His father often visited him in prison, and he had weekly phone calls with his mother. Despite the heinous crimes, they seemed to have some kind of unconditional love.",
            "Jeffrey Dahmer didn't eat people with tattoos because he said the ink made the flesh taste weird.",
            "Jeffery Dahmer started drinking alcohol at the age of fourteen.",
            "Dahmer nearly commited his first serious offense at the age of sixteen.",
            "However two years later at the age of eighteen Dahmer had committed his first crime.",
]

    response = random.choice(jeffery_dahmer_facts)
    await ctx.send(response)

@bot.command(name='jwg')
async def JWG(ctx):
    john_wayne_gacy_facts = [
            "Gacy's murders could have been solved at least six years earlier.",
            "Just 7 months before he got married he commited his first crime.",
            "Gacy kept his victims belongings as 'trophies'.",
            "After Gacy's death his brain was extracted.",
            "If you wrote John Wayne Gacy, he would send you a questionnaire to see if you were good enough to be friends with him.",
            "In the John Wayne Gacy case, there were so many bodies crammed underneath the house that the bodies melted together, and the bones had to be sorted for more than two years to put together the full skeletons.",
            "He used to dress up as a clown and called himself 'Pogo the clown'.",
            "Due to his father being an alcoholic and abusive person Gacy was more of a mama's boy.",
            "John Wayne Gacy was a necrophiliac.",
            "John Wayne Gacy was a KFC Manager.",
]

    response = random.choice(john_wayne_gacy_facts)
    await ctx.send(response)

@bot.command(name='TB')
async def ted(ctx):
    ted_bundy_facts = [
        "Ted Bundy was actually a bastard child and his grandparents thought it would be easier to say that he was adopted from an orphanage to avoid the embarassment of having a bastard child.",
        "While Bundy was in college he was actually a suicide prevention hotline worker.",
        "Bundy also saved a 3 year old who fell into a lake.",
        "Bundy was a people-pleaser.",
        "Like John Wayne Gacy, Ted Bundy was also a Necrophiliac.",
        "Ted Bundy helped in the investigation of the Green River Killer and made a psych profile, which ended up being closer to the actual Green River Killer than the FBI's own psych profile. That was also a huge part of the inspiration for Silence of the Lambs. Bundy also tried to masturbate to photos of his crime scene when Detective Keppel brought them in — which is why he stopped letting Bundy keep the files.",
        "Ted Bundy was someone who returned to his crime scenes afte he committed the acts.",
        "Bundy's first victim was a man.",
        "He decapitated at least 12 of his victims.",
        "Ted Bundy actually escaped twice.",
]   
    response = random.choice(ted_bundy_facts)
    await ctx.send(response)

@bot.command(name='Zodiac')
async def zod(ctx):
    zodiac_killer_facts = [
        "The zodiac killer actually wanted to go viral, after his second murder attempt he called police to report the crime and to take credit for a previous attack the year prior.",
        "Out of all his victims only two survived.",
        "An ex-cartoonist wrote the most popular book on the case.",
        "He was really obsessed with numbers, specifically twos and threes.",
        "The Zodiac Killer was never caught.",
        "The Riddler in the batman movie(2022) was inspired by the zodiac killer.",
        "In the 2016 game Watch Dogs 2 there is a mission in which you track down a 'new' zodiac killer.",
        "He really liked dumping bodies in lakes.",
        "The Zodiac Killers outfit was inspired by the medieval ages.",
        "A YouTube video lead to the solution of one of the zodiac's ciphers. "
 ]
    response = random.choice(zodiac_killer_facts)
    await ctx.send(response)


bot.run('')

