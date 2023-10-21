import requests
import json
import math
import settings


def formatSecs(timer: int):
  if timer < 3600:
    return f"{str(math.floor(timer / 60)).zfill(2)}:{str(math.floor((timer % 60))).zfill(2)}"
  else:
    return f"{math.floor(timer / 3600)}:{str(math.floor((timer % 3600) / 60)).zfill(2)}:{str(math.floor((timer % 60))).zfill(2)}"


def fixKeyError(stats: dict, key: str):
  try:
    return stats[key]
  except KeyError:
    return 0


def generalStats(name):
  print(f'{settings.API_LINK}{name}')
  player_data = (requests.get(f'{settings.API_LINK}{name}')).json()
  print(player_data['success'])
  
  if not player_data['success']:
    if player_data['cause'] == "Invalid API key":
      return player_data['cause']
    elif player_data['cause'] == "You have already looked up this name recently":
      return "Timeout"
    elif player_data['cause'] == "Key throttle":
      return player_data['cause']
    else:
      return player_data['cause']
    
  if player_data['player'] is None:
    return "No Such Players"
  if "stats" in player_data['player'] and "Arcade" in player_data['player']['stats']:
    arc_stats: dict = player_data['player']['stats']['Arcade']
    denominatorA = 1 if fixKeyError(arc_stats, 'bullets_shot_zombies') == 0 else fixKeyError(arc_stats, 'bullets_shot_zombies')
    denominatorB = 1 if fixKeyError(arc_stats, 'bullets_hit_zombies') == 0 else fixKeyError(arc_stats, 'bullets_hit_zombies')
    denominatorC = 1 if fixKeyError(arc_stats, 'deaths_zombies') == 0 else fixKeyError(arc_stats, 'deaths_zombies')
    stats = {
      "General": {
        "Name": player_data['player']['displayname'], 
        "UUID": player_data['player']['uuid'], 
        "Wins": fixKeyError(arc_stats, 'wins_zombies'),
        "TRS": fixKeyError(arc_stats, 'total_rounds_survived_zombies'),
        "Kills": fixKeyError(arc_stats, 'zombie_kills_zombies'),
        "Accuracy": round((fixKeyError(arc_stats, 'bullets_hit_zombies') / denominatorA * 100)),
        "Headshots": round((fixKeyError(arc_stats, 'headshots_zombies') / denominatorB * 100)),
        "K/D": round(fixKeyError(arc_stats, 'zombie_kills_zombies') / denominatorC),
        "Revives": fixKeyError(arc_stats, 'players_revived_zombies'),
        "Downs": fixKeyError(arc_stats, 'times_knocked_down_zombies'),
        "Deaths": fixKeyError(arc_stats, 'deaths_zombies'),
        "Doors": fixKeyError(arc_stats, 'doors_opened_zombies'),
        "Windows": fixKeyError(arc_stats, 'windows_repaired_zombies'),
      },
      "Dead-End": {
        "General": {
          "Wins": fixKeyError(arc_stats, 'wins_zombies_deadend'),
          "Kills": fixKeyError(arc_stats, 'zombie_kills_zombies_deadend'),
          "Revives": fixKeyError(arc_stats, 'players_revived_zombies_deadend'),
          "Downs": fixKeyError(arc_stats, 'times_knocked_down_zombies_deadend'),
          "Deaths": fixKeyError(arc_stats, 'deaths_zombies_deadend'),
          "TRS": fixKeyError(arc_stats, 'total_rounds_survived_zombies_deadend'),
          "Doors": fixKeyError(arc_stats, 'doors_opened_zombies_deadend'),
          "Windows": fixKeyError(arc_stats, 'windows_repaired_zombies_deadend'),
        },
        "Normal": {
          "Wins": fixKeyError(arc_stats, 'wins_zombies_deadend_normal'),
          "BR": fixKeyError(arc_stats, 'best_round_zombies_deadend_normal'),
          "FTB-R10": formatSecs( fixKeyError(arc_stats, 'fastest_time_10_zombies_deadend_normal')),
          "FTB-R20": formatSecs( fixKeyError(arc_stats, 'fastest_time_20_zombies_deadend_normal')),
          "FTB-R30": formatSecs( fixKeyError(arc_stats, 'fastest_time_30_zombies_deadend_normal')),
          "Kills": fixKeyError(arc_stats, 'zombie_kills_zombies_deadend_normal'),
          "Revives": fixKeyError(arc_stats, 'players_revived_zombies_deadend_normal'),
          "Downs": fixKeyError(arc_stats, 'times_knocked_down_zombies_deadend_normal'),
          "Deaths": fixKeyError(arc_stats, 'deaths_zombies_deadend_normal'),
          "TRS": fixKeyError(arc_stats, 'total_rounds_survived_zombies_deadend_normal'),
          "Doors": fixKeyError(arc_stats, 'doors_opened_zombies_deadend_normal'),
          "Windows": fixKeyError(arc_stats, 'windows_repaired_zombies_deadend_normal'),
        },
        "Hard": {
          "Wins": fixKeyError(arc_stats, 'wins_zombies_deadend_hard'),
          "BR": fixKeyError(arc_stats, 'best_round_zombies_deadend_hard'),
          "FTB-R10": formatSecs(fixKeyError(arc_stats, 'fastest_time_10_zombies_deadend_hard')),
          "FTB-R20": formatSecs(fixKeyError(arc_stats, 'fastest_time_20_zombies_deadend_hard')),
          "FTB-R30": formatSecs(fixKeyError(arc_stats, 'fastest_time_30_zombies_deadend_hard')),
          "Kills": fixKeyError(arc_stats, 'zombie_kills_zombies_deadend_hard'),
          "Revives": fixKeyError(arc_stats, 'players_revived_zombies_deadend_hard'),
          "Downs": fixKeyError(arc_stats, 'times_knocked_down_zombies_deadend_hard'),
          "Deaths": fixKeyError(arc_stats, 'deaths_zombies_deadend_hard'),
          "TRS": fixKeyError(arc_stats, 'total_rounds_survived_zombies_deadend_hard'),
          "Doors": fixKeyError(arc_stats, 'doors_opened_zombies_deadend_hard'),
          "Windows": fixKeyError(arc_stats, 'windows_repaired_zombies_deadend_hard'),
        },
        "RIP": {
          "Wins": fixKeyError(arc_stats, 'wins_zombies_deadend_rip'),
          "BR": fixKeyError(arc_stats, 'best_round_zombies_deadend_rip'),
          "FTB-R10": formatSecs(fixKeyError(arc_stats, 'fastest_time_10_zombies_deadend_rip')),
          "FTB-R20": formatSecs(fixKeyError(arc_stats, 'fastest_time_20_zombies_deadend_rip')),
          "FTB-R30": formatSecs(fixKeyError(arc_stats, 'fastest_time_30_zombies_deadend_rip')),
          "Kills": fixKeyError(arc_stats, 'zombie_kills_zombies_deadend_rip'),
          "Revives": fixKeyError(arc_stats, 'players_revived_zombies_deadend_rip'),
          "Downs": fixKeyError(arc_stats, 'times_knocked_down_zombies_deadend_rip'),
          "Deaths": fixKeyError(arc_stats, 'deaths_zombies_deadend_rip'),
          "TRS": fixKeyError(arc_stats, 'total_rounds_survived_zombies_deadend_rip'),
          "Doors": fixKeyError(arc_stats, 'doors_opened_zombies_deadend_rip'),
          "Windows": fixKeyError(arc_stats, 'windows_repaired_zombies_deadend_rip'),
        }
      },
      "Bad-Blood": {
        "General": {
          "Wins": fixKeyError(arc_stats, 'wins_zombies_badblood'),
          "Kills": fixKeyError(arc_stats, 'zombie_kills_zombies_badblood'),
          "Revives": fixKeyError(arc_stats, 'players_revived_zombies_badblood'),
          "Downs": fixKeyError(arc_stats, 'times_knocked_down_zombies_badblood'),
          "Deaths": fixKeyError(arc_stats, 'deaths_zombies_badblood'),
          "TRS": fixKeyError(arc_stats, 'total_rounds_survived_zombies_badblood'),
          "Doors": fixKeyError(arc_stats, 'doors_opened_zombies_badblood'),
          "Windows": fixKeyError(arc_stats, 'windows_repaired_zombies_badblood'),
        },
        "Normal": {
          "Wins": fixKeyError(arc_stats, 'wins_zombies_badblood_normal'),
          "BR": fixKeyError(arc_stats, 'best_round_zombies_badblood_normal'),
          "FTB-R10": formatSecs(fixKeyError(arc_stats, 'fastest_time_10_zombies_badblood_normal')),
          "FTB-R20": formatSecs(fixKeyError(arc_stats, 'fastest_time_20_zombies_badblood_normal')),
          "FTB-R30": formatSecs(fixKeyError(arc_stats, 'fastest_time_30_zombies_badblood_normal')),
          "Kills": fixKeyError(arc_stats, 'zombie_kills_zombies_badblood_normal'),
          "Revives": fixKeyError(arc_stats, 'players_revived_zombies_badblood_normal'),
          "Downs": fixKeyError(arc_stats, 'times_knocked_down_zombies_badblood_normal'),
          "Deaths": fixKeyError(arc_stats, 'deaths_zombies_badblood_normal'),
          "TRS": fixKeyError(arc_stats, 'total_rounds_survived_zombies_badblood_normal'),
          "Doors": fixKeyError(arc_stats, 'doors_opened_zombies_badblood_normal'),
          "Windows": fixKeyError(arc_stats, 'windows_repaired_zombies_badblood_normal'),
        },
        "Hard": {
          "Wins": fixKeyError(arc_stats, 'wins_zombies_badblood_hard'),
          "BR": fixKeyError(arc_stats, 'best_round_zombies_badblood_hard'),
          "FTB-R10": formatSecs(fixKeyError(arc_stats, 'fastest_time_10_zombies_badblood_hard')),
          "FTB-R20": formatSecs(fixKeyError(arc_stats, 'fastest_time_20_zombies_badblood_hard')),
          "FTB-R30":formatSecs(fixKeyError(arc_stats, 'fastest_time_30_zombies_badblood_hard')),
          "Kills": fixKeyError(arc_stats, 'zombie_kills_zombies_badblood_hard'),
          "Revives": fixKeyError(arc_stats, 'players_revived_zombies_badblood_hard'),
          "Downs": fixKeyError(arc_stats, 'times_knocked_down_zombies_badblood_hard'),
          "Deaths": fixKeyError(arc_stats, 'deaths_zombies_badblood_hard'),
          "TRS": fixKeyError(arc_stats, 'total_rounds_survived_zombies_badblood_hard'),
          "Doors": fixKeyError(arc_stats, 'doors_opened_zombies_badblood_hard'),
          "Windows": fixKeyError(arc_stats, 'windows_repaired_zombies_badblood_hard'),
        },
        "RIP": {
          "Wins": fixKeyError(arc_stats, 'wins_zombies_badblood_rip'),
          "BR": fixKeyError(arc_stats, 'best_round_zombies_badblood_rip'),
          "FTB-R10": formatSecs(fixKeyError(arc_stats, 'fastest_time_10_zombies_badblood_rip')),
          "FTB-R20": formatSecs(fixKeyError(arc_stats, 'fastest_time_20_zombies_badblood_rip')),
          "FTB-R30": formatSecs(fixKeyError(arc_stats, 'fastest_time_30_zombies_badblood_rip')),
          "Kills": fixKeyError(arc_stats, 'zombie_kills_zombies_badblood_rip'),
          "Revives": fixKeyError(arc_stats, 'players_revived_zombies_badblood_rip'),
          "Downs": fixKeyError(arc_stats, 'times_knocked_down_zombies_badblood_rip'),
          "Deaths": fixKeyError(arc_stats, 'deaths_zombies_badblood_rip'),
          "TRS": fixKeyError(arc_stats, 'total_rounds_survived_zombies_badblood_rip'),
          "Doors": fixKeyError(arc_stats, 'doors_opened_zombies_badblood_rip'),
          "Windows": fixKeyError(arc_stats, 'windows_repaired_zombies_badblood_rip'),
        }
      },
      "Alien-Arcadium": {
        "Wins": fixKeyError(arc_stats, 'wins_zombies_alienarcadium_normal'),
        "BR": fixKeyError(arc_stats, 'best_round_zombies_alienarcadium'),
        "FTB-R10": formatSecs(fixKeyError(arc_stats, 'fastest_time_10_zombies_alienarcadium_normal')),
        "FTB-R20": formatSecs(fixKeyError(arc_stats, 'fastest_time_20_zombies_alienarcadium_normal')),
        "Kills": fixKeyError(arc_stats, 'zombie_kills_zombies_alienarcadium'),
        "Revives": fixKeyError(arc_stats, 'players_revived_zombies_alienarcadium'),
        "Downs": fixKeyError(arc_stats, 'times_knocked_down_zombies_alienarcadium'),
        "Deaths": fixKeyError(arc_stats, 'deaths_zombies_alienarcadium'),
        "TRS": fixKeyError(arc_stats, 'total_rounds_survived_zombies_alienarcadium'),
        "Doors": fixKeyError(arc_stats, 'doors_opened_zombies_alienarcadium'),
        "Windows": fixKeyError(arc_stats, 'windows_repaired_zombies_alienarcadium')
      }
    }

    return stats
  return "No Arcade Data"
