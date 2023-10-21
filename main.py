import settings
import zombiesAPI
import discord
from discord.ext import commands
import embedsMaker
from replit import db
from keepAlive import keepAlive

logger = settings.logging.getLogger("bot")

if "cache" in db.keys():
  del db["cache"]

class SimpleView(discord.ui.View):
  data: dict = None

  async def disable_all_items(self):
    for item in self.children:
      item.disabled = True
    await self.message.edit(view=self)

  async def on_timeout(self) -> None:
    await self.disable_all_items()

  @discord.ui.button(label="Dead End", style=discord.ButtonStyle.success)
  async def deadend(self, interaction: discord.Interaction, button: discord.ui.Button):
    embed = embedsMaker.makeStatsEmbed(self.data, "Dead-End")
    await interaction.response.send_message(embed=embed[0])
    # await interaction.followup.send(embed=embeds[1])
    # await interaction.followup.send(embed=embeds[2])
    self.stop()

  @discord.ui.button(label="Bad Blood", style=discord.ButtonStyle.red)
  async def badblood(self, interaction: discord.Interaction, button: discord.ui.Button):
    embed = embedsMaker.makeStatsEmbed(self.data, "Bad-Blood")
    await interaction.response.send_message(embed=embed[0])
    # await interaction.followup.send(embed=embeds[1])
    # await interaction.followup.send(embed=embeds[2])
    self.stop()

  @discord.ui.button(label="Alien Arcadium", style=discord.ButtonStyle.blurple)
  async def alienarcade(self, interaction: discord.Interaction, button: discord.ui.Button):
    embed = embedsMaker.makeStatsEmbed(self.data, "Alien-Arcadium")
    await interaction.response.send_message(embed=embed)
    self.stop()


def run():
  intents = discord.Intents.default()
  intents.message_content = True
  discord.Intents.all()
  bot = commands.Bot(command_prefix="!", intents=intents)

  @bot.event
  async def on_ready():
    print(bot.user)

  @bot.event
  async def on_command_error(ctx, error):
    return

  @bot.command(
    aliases=['g', 'stats', 's'],
    help="Retrieves the given player's General Zombies stats",
    description="Description:",
    brief="General Stats",
    enabled=True,
    hidden=False
  )
  async def general(ctx, *player_names):
    if player_names:
      for player_name in player_names:
        print()
        player_data = zombiesAPI.generalStats(player_name)
  
        player_data = await settings.errorHandling(ctx, player_data, player_name)
        if not player_data:
          continue
  
        embed = embedsMaker.makeStatsEmbed(player_data)
  
        await ctx.send(embed=embed)
        
        view = SimpleView(timeout=50)
        view.data = player_data
        
        message = await ctx.send(view=view)
      
      view.message = message
      await view.wait()
      await view.disable_all_items()
    else:
      await ctx.send("Please give a player name")

  @bot.command(
    aliases=['de'],
    help="Retrieves the given player's Dead End Zombies stats",
    description="Description:",
    brief="Dead End Stats",
    enabled=True,
    hidden=False
  )
  async def deadend(ctx, mode: str = None, *player_names):
    if player_names:
      for player_name in player_names:
        player_data = zombiesAPI.generalStats(player_name)
        
        player_data = await settings.errorHandling(ctx, player_data, player_name)
        if not player_data:
          continue

        embeds = embedsMaker.makeStatsEmbed(player_data, "Dead-End", mode)
        for embed in embeds:
          await ctx.send(embed=embed)
    else:
      embed = embedsMaker.makeErrorEmbed(902, "Please specify player name/s")
      await ctx.send(embed=embed)

  @bot.command(
    aliases=['bb'],
    help="Retrieves the given player's Bad Blood Zombies stats",
    description="Description:",
    brief="Bad Blood Stats",
    enabled=True,
    hidden=False
  )
  async def badblood(ctx, mode: str = None, *player_names):
    if player_names:
      for player_name in player_names:
        player_data = zombiesAPI.generalStats(player_name)
        
        player_data = await settings.errorHandling(ctx, player_data, player_name)
        if not player_data:
          continue
        
        embeds = embedsMaker.makeStatsEmbed(player_data, "Bad-Blood", mode)
        for embed in embeds:
          await ctx.send(embed=embed)
    else:
      embed = embedsMaker.makeErrorEmbed(902, "Please specify player name/s")
      await ctx.send(embed=embed)

  @bot.command(
    aliases=['aa'],
    help="Retrieves the given player's Alien Arcadium Zombies stats",
    description="Description:",
    brief="Alien Arcadium Stats",
    enabled=True,
    hidden=False)
  async def alienarcadium(ctx, *player_names):
    if player_names:
      for player_name in player_names:
        print()
        player_data = zombiesAPI.generalStats(player_name)
  
        player_data = await settings.errorHandling(ctx, player_data, player_name)
        if not player_data:
          continue
  
        view = SimpleView(timeout=50)
        view.data = player_data
  
        embed = embedsMaker.makeStatsEmbed(player_data, "Alien-Arcadium")
  
        await ctx.send(embed=embed)

  keepAlive()
  bot.run(settings.DISCORD_TOKEN, root_logger=True)


if __name__ == '__main__':
  run()
