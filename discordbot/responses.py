from random import choice, randint
import re


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '#miragestairs':
        return 'https://assets.csnades.gg/nades/mirage-smoke-FmNaL1KYD4/hq.webm'
    if lowered == '#miragect':
        return 'https://assets.csnades.gg/nades/mirage-smoke-pbyd3lrrEt/hq.webm'
    if lowered == '#miragetriple':
        return 'https://assets.csnades.gg/nades/mirage-smoke-Xr2OxZ31vZ/hq.webm'
    if lowered == '#miragejungle':
        return 'https://assets.csnades.gg/nades/mirage-smoke-4m9u6244Pc/hq.webm'



def get_response_id(user_input: str) -> str:
    steamid: str = user_input
    steamidcheck = r'^\d{17}$'
    if re.match(steamidcheck, steamid):
        return "https://csstats.gg/player/" + steamid
