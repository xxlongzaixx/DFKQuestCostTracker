import aiohttp
from src.dfk_rewards import QUEST_GAS_USED, cv_fishing

DEXSCREENER_URL = "https://api.dexscreener.io/latest/dex/pairs"

async def get_quest_cost_breakeven():
    # Get Jewel price
    jewel = await get_jewel()
    jewel_usd = float(jewel["pair"]["priceUsd"])

    # Get quest expected value
    cv_fishing_loots_prices = await get_loots_prices("avalanchedfk", cv_fishing)
    cv_fishing_loots_ev = get_loots_expected_value(cv_fishing_loots_prices)
    cv_fishing_breakeven = get_breakeven_gwei(cv_fishing_loots_ev, jewel_usd, "fishing")

    response = {"cv_fishing": cv_fishing_breakeven}
    return response


def get_breakeven_gwei(loots_ev, jewel_usd, profession):
    breakeven_gwei = round(
        loots_ev / (jewel_usd * QUEST_GAS_USED[profession]) * 1_000_000_000, 1
    )
    return breakeven_gwei


def get_loots_expected_value(data):
    total_ev = 0
    for item in data:
        ev = (item[2] / 100) * item[3]  # Multiply the chance of looting and price
        total_ev += ev
    return total_ev * 5  # 5 tries


async def fetch(client, params):
    url = f"{DEXSCREENER_URL}/{params['chainId']}/{params['pairAddress']}"
    async with client.get(url) as resp:
        return await resp.json()


async def get_prices(params):
    async with aiohttp.ClientSession() as client:
        r = await fetch(client, params)
        return r


async def get_jewel():
    chain_id = "avalanchedfk"
    pair_address = "0xCF329b34049033dE26e4449aeBCb41f1992724D3"
    params = {"chainId": chain_id, "pairAddress": pair_address}
    r = await get_prices(params)
    return r


async def get_loots_prices(chain_id, loots_list):
    pair_address = ",".join([item[0] for item in loots_list])
    params = {"chainId": chain_id, "pairAddress": pair_address}
    price_response = await get_prices(params)

    price_mapping = {
        pair["pairAddress"].lower(): float(pair["priceUsd"])
        for pair in price_response["pairs"]
    }
    updated_loots_list = [
        entry + (price_mapping.get(entry[0].lower()),) for entry in cv_fishing
    ]

    return updated_loots_list
