from nextcord.ext import commands
import datetime

bot = commands.Bot(command_prefix="!") # erstelle das Bot Objekt

@bot.event # erstelle ein Event
async def on_ready(): # wenn der Bot bereit ist
    print(f"{bot.user.name} is ready! :)") # dann gib den Namen des Bots aus

bot.slash_command(name="test", description="test command", guild_ids=[config.guild_id])    
async def test(interaction: nextcord.Interaction):                                          
    
    embed_test = nextcord.Embed(                                                            
        color=0x7289da,                                                                     
        title="Test Embed",                                                                 
        description="Das ist ein Test Embed!",                                              
        timestamp=datetime.datetime.utcnow(),                                               
    )
    embed_test.set_author(icon_url=interaction.user.avatar_url, name=interaction.user.name) 
    embed_test.set_footer(text="Test Footer", icon_url=interaction.user.avatar_url)        
    embed_test.add_field(name="Test Field Inline", value="Test Value", inline=True)       
    embed_test.add_field(name="Test Field not Inline", value="Test Value", inline=False) 
    embed_test.add_field(name="Test Field not Inline", value="Test Value", inline=False) 
    embed_test.set_image(url="https://hypecord.eu/media/hypecord/hypecord.png")          
    embed_test.set_thumbnail(url="https://hypecord.eu/media/hc/hc.png")                  
    
    class Select(nextcord.ui.Select):
        def __init__(self):
            options=[
                nextcord.SelectOption(label="Option 1", description="Option 1", value="option1"),
                nextcord.SelectOption(label="Option 2", description="Option 2", value="option2"),
                ]
            super().__init__(placeholder="Select an option",max_values=1,min_values=1,options=options)
        async def callback(self, interaction: nextcord.Interaction):
            if self.values[0] == "option1":
                await interaction.send_message(content="Option 1!")
            elif self.values[0] == "option2":
                await interaction.response.send_message(content="Option 2!")
                
    class SelectView(ui.View):
        def __init__(self, *, timeout = 180):
            super().__init__(timeout=timeout)
            self.add_item(Select())
    
    await interaction.response.send_message(embed=embed_test, view=SelectView())                            
    
bot.run(config.token) # run the bot