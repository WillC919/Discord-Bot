from replit import db


def cacheTheData(player_data: dict):
  if "cache" not in db.keys():
    db["cache"] = [player_data]
  else:
    cache = db["cache"]
    for i in range(len(cache)):
      if cache[i]["General"]["Name"].lower() in player_data["General"]["Name"].lower():
        cache[i] = player_data
        db["cache"] = cache
        return
    if len(cache) >= 10:
      cache.pop(0)
    cache.append(player_data)
    db["cache"] = cache


def getTheCacheData(player_name: str):
  if "cache" not in db.keys():
    db["cache"] = []
    return "No Cache"
  else:
    cache = db["cache"]
    for i in range(len(cache) - 1, -1, -1):
      if player_name.lower() in cache[i]["General"]["Name"].lower():
        return cache[i]
    return "No Match"
