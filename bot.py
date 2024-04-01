import config
import discord
from discord.ext import commands
import random


intents = discord.Intents.default()
intents.members = True  # For on_member_join
intents.presences = True  # For presence information
intents.message_content = True  # Used for processes message content

bot = commands.Bot(command_prefix='$', intents=intents)

def get_random_adjective(file_path):
    with open(file_path, 'r') as file:
        adjectives = file.readlines()
    # Strips the new line from the text file
    adjectives = [adjective.strip() for adjective in adjectives]
    return random.choice(adjectives)

@bot.event
async def on_member_join(member):
        file_path = 'english-adjectives.txt'
        prefix = get_random_adjective(file_path)
        membersName = member.display_name
        newName = prefix + 'bug(' + membersName + ')'
        try: 
            await member.edit(nick=newName)
        except Exception as e:
            print("Name could not be changed")
            
@bot.event         
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')    
    
    
bot.run(config.API_KEY)
    