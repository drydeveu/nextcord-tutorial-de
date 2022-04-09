import nextcord
import config
from nextcord.ext import commands

bot = commands.Bot(command_prefix="!") # create the bot object

@bot.event # create a event 
async def on_ready(): # when the bot is ready
    print(f"{bot.user.name} is ready! :)") # print the bot's name and that it is ready

@bot.slash_command(name="test", description="test command", guild_ids=[config.guild_id])    # create a slash command
async def test(interaction: nextcord.Interaction):                                          # define the function
    await interaction.response.send_message(f"Hello {interaction.user.mention}!")           # send a message to the user
    
bot.run(config.token) # run the bot