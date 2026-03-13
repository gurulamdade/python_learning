def printLyrics():
    import time

    lyrics = [
        "Haa Manne sambh-sambh rakhe tere jhanjhara ke jode",
        "Meri gail ro-ro ye bhi chhori bawle se hore",
        "Manne aaye jaave khyaal tere khoye jaave khyaal tere",
        "Jeene koni deti haye bairi tanhayi manne",
        "Geeta mein gayi kade chhaati ke lagayi manne",
        "Jad bhi gaya re teri yaad khadi payi manne",
        "Sambh sambh rakhi bahut chhaati ke lagayi manne",
        "Jad bhi gaya re teri yaad khadi payi manne"
    ]

    delays = [0.5, 0.8, 1, 1.2, 1.1, 1, 1, 0.9]

    for i, line in enumerate(lyrics):
        for char in line:
            print(char, end="", flush=True)
            time.sleep(0.055)
        time.sleep(delays[i])
        print()

printLyrics()