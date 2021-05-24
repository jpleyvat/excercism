present = [
    "a Partridge in a Pear Tree.",
    "two Turtle Doves, ",
    "three French Hens, ",
    "four Calling Birds, ",
    "five Gold Rings, ",
    "six Geese-a-Laying, ",
    "seven Swans-a-Swimming, ",
    "eight Maids-a-Milking, ",
    "nine Ladies Dancing, ",
    "ten Lords-a-Leaping, ",
    "eleven Pipers Piping, ",
    "twelve Drummers Drumming, ",
]

days = {
    "1": "first",
    "2": "second",
    "3": "third",
    "4": "fourth",
    "5": "fifth",
    "6": "sixth",
    "7": "seventh",
    "8": "eighth",
    "9": "ninth",
    "10": "tenth",
    "11": "eleventh",
    "12": "twelfth",
}


def recite(start_verse, end_verse, last_verse=0, song=None, presents_memo=None):

    if end_verse > last_verse:
        song, presents_memo = [], []
        last_verse = end_verse

    if end_verse != 1:
        recite(
            start_verse,
            end_verse - 1,
            last_verse=last_verse,
            song=song,
            presents_memo=presents_memo,
        )
        if end_verse == 2:
            presents_memo[0] = ["and " + present[0]]
        presents = [present[end_verse - 1]]
        presents.extend(presents_memo[end_verse - 2])
        presents_memo.append(presents)

    else:
        presents = [present[end_verse - 1]]
        presents_memo.append([presents])

    if end_verse >= start_verse:
        day_of_christmas = (
            f"On the {days[str(end_verse)]} day of Christmas my true love gave to me: "
        )

        song.append((day_of_christmas, presents))

    if last_verse == end_verse:
        song_days = (verse[0] for verse in song)
        song_presents = tuple(
            map(lambda presents: "".join(presents), [verse[1] for verse in song])
        )

        answer = list(
            map(lambda verse: ["".join(verse)], zip(song_days, song_presents))
        )

        return ["".join(verse) for verse in answer]
