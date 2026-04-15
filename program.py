import requests
url = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/"
parametry = {
    "key": "", #Your API key here
    "steamid": "", #Your Steam ID here
    "include_appinfo": "true",
    "include_played_free_games": "true"
}
odpowiedz = requests.get(url, params=parametry)
dane = odpowiedz.json()
moje_gry = dane["response"]["games"]
najdluzszy_czas = 0
licznik_niegranych = 0
nie_grane_gry = []
ulubiona_gra = ""
trzy_ulubione_gry = []
for gra in moje_gry:
    if gra["playtime_forever"] > najdluzszy_czas:
        najdluzszy_czas = gra["playtime_forever"]
        ulubiona_gra = gra["name"]
    if gra["playtime_forever"] == 0:
        licznik_niegranych += 1
        nie_grane_gry.append(gra["name"])

print(f"My favourite game is: {ulubiona_gra} with playtime of {najdluzszy_czas/60 :.1f} hours.")
print(f"I haven't played {licznik_niegranych} games.")
print("Unplayed games:")
for gra in nie_grane_gry:
    print(f" - {gra}")
print("Three favourite games:")
ulubione_gry = sorted(moje_gry, key=lambda x: x["playtime_forever"], reverse=True)[:3]
for gra in ulubione_gry:
    print(f" - {gra['name']} with playtime of {gra['playtime_forever']/60 :.1f} hours.")