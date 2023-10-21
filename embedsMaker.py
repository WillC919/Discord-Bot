import settings
import discord
from discord.ext import commands


def makeStatsEmbed(player_data: dict, map: str = None, mode: str = "g"):
  if map == None:
    embed = discord.Embed(
        title=f"{reformatUsername(player_data['General']['Name'])}",
        description="General Zombies Statistics",
        colour=discord.Colour.lighter_gray()
    )
    embed.set_thumbnail(url=f"{settings.SKIN_LINK}{player_data['General']['UUID']}")
    
    embed.add_field(name="Grade Score\t\t\t‎ㅤㅤ", value="```WIP```")
    embed.add_field(name="Wins\t\t\t\t\t\t\t\t    ‎", value=f"```{format(player_data['General']['Wins'], ',')}```")
    embed.add_field(name="Total Rounds Survived ‎", value=f"```{format(player_data['General']['TRS'], ',')}```")

    embed.add_field(name="Hit Accuracy", value=f"```{player_data['General']['Accuracy']}%```")
    embed.add_field(name="Headshots Accuracy", value=f"```{player_data['General']['Headshots']}%```")
    embed.add_field(name="Kill/Death Ratio", value=f"```{format(player_data['General']['K/D'], ',')}```")

    embed.add_field(name="Kills", value=f"```{format(player_data['General']['Kills'], ',')}```")
    embed.add_field(name="Downs", value=f"```{format(player_data['General']['Downs'], ',')}```")
    embed.add_field(name="Deaths", value=f"```{format(player_data['General']['Deaths'], ',')}```")

    embed.add_field(name="Revives", value=f"```{format(player_data['General']['Revives'], ',')}```")
    embed.add_field(name="Doors Opened", value=f"```{format(player_data['General']['Doors'], ',')}```")
    embed.add_field(name="Windows Repaired", value=f"```{format(player_data['General']['Windows'], ',')}```")
    return embed
  elif map == "Dead-End" or map == "Bad-Blood":
    if mode:
      colors = [discord.Colour.light_grey()]
      mode = mode.lower()
      if mode == "g" or mode == "gen" or mode == "general" or mode == "0":
        mode = "General"
      elif mode == "n" or mode == "norm" or mode == "normal" or mode == "1":
        mode = ["Normal"]
        colors = [discord.Colour.brand_green()]
      elif mode == "h" or mode == "hard" or mode == "2":
        mode = ["Hard"]
        colors = [discord.Colour.yellow()]
      elif mode == "r" or mode == "rip" or mode == "3":
        mode = ["RIP"]
        colors = [discord.Colour.red()]
      elif mode == "a" or mode == "all" or mode == "4":
        mode = ['Normal', 'Hard', 'RIP']
        colors = [discord.Colour.brand_green(), discord.Colour.yellow(), discord.Colour.red()]
      else:
        return [makeErrorEmbed(901, "Please specify a valid mode")]
    else:
      return [makeErrorEmbed(900, "Please specify a mode")]

    map_name = "Dead End"
    if map == "Bad-Blood":
      map_name = "Bad Blood"

    if mode == "General":
      embed = discord.Embed(
        title=f"{reformatUsername(player_data['General']['Name'])}",
        description=f"General {map_name} Zombies Statistics",
        colour=discord.Colour.dark_teal() if map == "Dead-End" else discord.Colour.dark_red()
      )
      embed.set_thumbnail(url=f"{settings.SKIN_LINK}{player_data['General']['UUID']}")

      embed.add_field(name="Grade Score\t\t\t\t\t ‎", value="```WIP```")
      embed.add_field(name="Wins\t\t\t\t\t\t\t\t   ‎", value=f"```{format(player_data[map]['General']['Wins'], ',')}```")
      embed.add_field(name="Total Rounds Survived ‎", value=f"```{format(player_data[map]['General']['TRS'], ',')}```")
      
      embed.add_field(name="Normal Best Rounds", value=f"```{player_data[map]['Normal']['BR']}```")
      embed.add_field(name="Hard Best Rounds", value=f"```{player_data[map]['Hard']['BR']}```")
      embed.add_field(name="RIP Best Rounds", value=f"```{player_data[map]['RIP']['BR']}```")
  
      embed.add_field(name="Normal FTB R30", value=f"```{player_data[map]['Normal']['FTB-R30']}```")
      embed.add_field(name="Hard FTB R30", value=f"```{player_data[map]['Hard']['FTB-R30']}```")
      embed.add_field(name="RIP FTB R30", value=f"```{player_data[map]['RIP']['FTB-R30']}```")

      embed.add_field(name="Kills", value=f"```{format(player_data[map]['General']['Kills'], ',')}```")
      embed.add_field(name="Deaths", value=f"```{format(player_data[map]['General']['Deaths'], ',')}```")
      embed.add_field(name="Revives", value=f"```{format(player_data[map]['General']['Revives'], ',')}```")
      
      # embed.add_field(name="Knocked\nDowns", value=f"`{format(player_data[map]['General']['Downs'])
      # embed.add_field(name="Doors\nOpened", value=f"`{format(player_data[map]['General']['Doors'])
      # embed.add_field(name="Windows\nRepaired", value=f"`{format(player_data[map]['General']['Windows'])
      return [embed]
    else:
      embeds = []
      for m in mode:
        embed = discord.Embed(
          title=f"{reformatUsername(player_data['General']['Name'])}",
          description=f"[{m}] {map_name} Zombies Statistics",
          colour=colors[mode.index(m)]
        )
        embed.set_thumbnail(url=f"{settings.SKIN_LINK}{player_data['General']['UUID']}")
        
        embed.add_field(name="Wins\t\t\t\t\t\t\t\t   ‎", value=f"```{format(player_data[map][m]['Wins'], ',')}```")
        embed.add_field(name="Best Rounds\t\t\t\t\t ‎", value=f"```{player_data[map][m]['BR']}```")
        embed.add_field(name="Total Rounds Survived ‎", value=f"```{format(player_data[map][m]['TRS'], ',')}```")
    
        embed.add_field(name="Fastest Time by R10", value=f"```{player_data[map][m]['FTB-R10']}```")
        embed.add_field(name="Fastest Time by R20", value=f"```{player_data[map][m]['FTB-R20']}```")
        embed.add_field(name="Fastest Time by R30", value=f"```{player_data[map][m]['FTB-R30']}```")
    
        embed.add_field(name="Kills", value=f"```{format(player_data[map][m]['Kills'], ',')}```")
        embed.add_field(name="Downs", value=f"```{format(player_data[map][m]['Downs'], ',')}```")
        embed.add_field(name="Deaths", value=f"```{format(player_data[map][m]['Deaths'], ',')}```")
    
        embed.add_field(name="Revives", value=f"```{format(player_data[map][m]['Revives'], ',')}```")
        embed.add_field(name="Doors Opened", value=f"```{format(player_data[map][m]['Doors'], ',')}```")
        embed.add_field(name="Windows Repaired", value=f"```{format(player_data[map][m]['Windows'], ',')}```")
        
        embeds.append(embed)
      return embeds
  elif map == "Alien-Arcadium":
    embed = discord.Embed(
      title=f"{reformatUsername(player_data['General']['Name'])}",
      description="Alien Arcadium Zombies Statistics",
      colour=discord.Colour.blurple()
    )
    embed.set_thumbnail(url=f"{settings.SKIN_LINK}{player_data['General']['UUID']}")
    
    embed.add_field(name="Grade Score\t\t\t\t\t ‎", value="```WIP```")
    embed.add_field(name="Wins\t\t\t\t\t\t\t\t   ‎", value=f"```{format(player_data['Alien-Arcadium']['Wins'], ',')}```")
    embed.add_field(name="Best Rounds\t\t\t\t\t ‎", value=f"```{player_data['Alien-Arcadium']['BR']}```")
    
    embed.add_field(name="Total Rounds Survived", value=f"```{format(player_data['Alien-Arcadium']['TRS'], ',')}```")
    embed.add_field(name="Fastest Time by R10", value=f"```{player_data['Alien-Arcadium']['FTB-R10']}```")
    embed.add_field(name="Fastest Time by R20", value=f"```{player_data['Alien-Arcadium']['FTB-R20']}```")

    embed.add_field(name="Kills", value=f"```{format(player_data['Alien-Arcadium']['Kills'], ',')}```")
    embed.add_field(name="Downs", value=f"```{format(player_data['Alien-Arcadium']['Downs'], ',')}```")
    embed.add_field(name="Deaths", value=f"```{format(player_data['Alien-Arcadium']['Deaths'], ',')}```")

    embed.add_field(name="Revives", value=f"```{format(player_data['Alien-Arcadium']['Revives'], ',')}```")
    embed.add_field(name="Doors Opened", value=f"```{format(player_data['Alien-Arcadium']['Doors'], ',')}```")
    embed.add_field(name="Windows Repaired", value=f"```{format(player_data['Alien-Arcadium']['Windows'], ',')}```")
    return embed


def makeErrorEmbed(num: int = 0, error_msg: str = ""):
  embed = discord.Embed(
    title=f"ERROR {num}",
    description=error_msg,
    colour=discord.Colour.red()
  )
  # embed.set_thumbnail(url=settings.ERROR_IMG_LINK)
  return embed

def reformatUsername(name: str):
  reformatedName = ""
  for i in range(len(name)):
    if name[i] == "_":
      reformatedName += "\_"
    else:
      reformatedName += name[i]
  return reformatedName