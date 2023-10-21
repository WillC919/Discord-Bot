import os
import logging
import embedsMaker
from logging.config import dictConfig
import storage

DISCORD_TOKEN = os.environ['TOKEN']
API_KEY = os.environ['KEY']

API_LINK = f'https://api.hypixel.net/player?key={API_KEY}&name='
SKIN_LINK = "https://api.mineatar.io/body/full/"
ERROR_IMG_LINK = "https://icons.iconarchive.com/icons/paomedia/small-n-flat/256/sign-error-icon.png"

async def errorHandling(ctx, player_data, player_name):
  retrieveCache = False

  if player_data == "Timeout":
    retrieveCache = True
    player_data = storage.getTheCacheData(player_name)

    if player_data == "No Match" or player_data == "No Cache":
      embed = embedsMaker.makeErrorEmbed(501, f"**{player_name}**'s dataset found. Unable to retrieve it. Try again in 1 min!")
      await ctx.send(embed=embed)
      return False 
  elif player_data == "No Such Players":
    embed = embedsMaker.makeErrorEmbed(201, f"**{player_name}** does not exist in Hypixel's Databases!")
    await ctx.send(embed=embed)
    return False
  elif player_data == "No Arcade Data":
    embed = embedsMaker.makeErrorEmbed(202, f"**{player_name}** has not played any Arcade Games!")
    await ctx.send(embed=embed)
    return False
  elif player_data == "Invalid API key":
    embed = embedsMaker.makeErrorEmbed(403, "Current API Key is invalid. A new API Key is required!")
    await ctx.send(embed=embed)
    return False
  elif player_data == "Key throttle":
    embed = embedsMaker.makeErrorEmbed(429, "Maximum number of API requests has been exceeded! Try again in 5 mins!")
    await ctx.send(embed=embed)
    return False
  
  if not retrieveCache:
    storage.cacheTheData(player_data)
  
  return player_data


LOGGING_CONFIG = {
  "version": 1,
  "disabled_existing_loggers": False,
  "formatters": {
    "verbose": {
      "format": "%(levelname)-10s - %(asctime)s - %(module)-15s : %(message)s"
    },
    "standard": {
      "format": "%(levelname)-10s - %(name)-15s : %(message)s"
    },
  },
  "handlers": {
    "console": {
      "level": "DEBUG",
      "class": "logging.StreamHandler",
      "formatter": "standard",
    },
    "console2": {
      "level": "WARNING",
      "class": "logging.StreamHandler",
      "formatter": "standard",
    },
    "file": {
      "level": "INFO",
      "class": "logging.FileHandler",
      "filename": "logs/infos.log",
      "mode": "w",
      "formatter": "verbose",
    },
  },
  "loggers": {
    "bot": {
      "handlers": ["console"],
      "level": "INFO",
      "propagate": False
    },
    "discord": {
      "handlers": ["console2", "file"],
      "level": "INFO",
      "propagate": False,
    },
  },
}

dictConfig(LOGGING_CONFIG)
