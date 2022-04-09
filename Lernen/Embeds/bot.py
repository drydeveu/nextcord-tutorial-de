import imp
import nextcord
import config
from nextcord.ext import commands
import datetime

bot = commands.Bot(command_prefix="!") # erstelle das Bot Objekt

@bot.event # erstelle ein Event
async def on_ready(): # wenn der Bot bereit ist
    print(f"{bot.user.name} is ready! :)") # dann gib den Namen des Bots aus

@bot.slash_command(name="test", description="test command", guild_ids=[config.guild_id])    # erstelle ein Slash Command
async def test(interaction: nextcord.Interaction):                                          # definiere die Funktion
    
    embed_test = nextcord.Embed(                                                            # erstelle ein Embed
        color=0x7289da,                                                                     # setze die Farbe  (0x7289da = #7289da)
        title="Test Embed",                                                                 # setze den Titel
        description="Das ist ein Test Embed!",                                              # setze die Beschreibung
        timestamp=datetime.datetime.utcnow(),                                               # setze den Timestamp zur akutellen Zeit
    )
    embed_test.set_author(icon_url=interaction.user.avatar_url, name=interaction.user.name) # setze den Autor Name und Bild
    embed_test.set_footer(text="Test Footer", icon_url=interaction.user.avatar_url)        # setze den Footer Name und Bild
    embed_test.add_field(name="Test Field Inline", value="Test Value", inline=True)        # füge ein Feld hinzu Inline
    embed_test.add_field(name="Test Field Inline", value="Test Value", inline=True)       # füge ein Feld hinzu Inline
    embed_test.add_field(name="Test Field not Inline", value="Test Value", inline=False) # füge ein Feld hinzu nicht Inline
    embed_test.add_field(name="Test Field not Inline", value="Test Value", inline=False) # füge ein Feld hinzu nicht Inline
    embed_test.set_image(url="https://hypecord.eu/media/hypecord/hypecord.png")          # setze das Große untere Bild
    embed_test.set_thumbnail(url="https://hypecord.eu/media/hc/hc.png")                  # setze das kleine obere Bild
    
    await interaction.response.send_message(embed=embed_test)                                  # sende das Embed
    
bot.run(config.token) # run the bot