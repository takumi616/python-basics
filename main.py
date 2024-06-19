def list():
    genais = ["gemini", "llama", "chatgpt"]
    print(genais)
#stack like
    genais.pop()
    print(genais)

    genais.append("cohere")
    print(genais)
#stack like

    genais.remove("llama")
    print(genais)

list()


def dictionary():
    songs = {"Avril lavigne": "complicated", "Jin Akanishi": "care", "Justin": "sorry"}
    print(songs)

    songs.pop("Justin")
    print(songs)

    song_name = songs.values()
    print(song_name)
    singers = songs.keys()
    print(singers)

    items = songs.items()
    print(items)           # dict_items([('Avril lavigne', 'complicated'), ('Jin Akanishi', 'care')])

    avril_song = songs.get("Avril lavigne")
    print(avril_song)

    # add new key value pairs
    songs["Zedd"] = "clarity"
    print(songs)

dictionary()

