class Painting:
    museum = "Louvre"

    def __init__(self, title, artist, year):
        self.year = year
        self.artist = artist
        self.title = title
        self.descr = f'"{title}" by {artist} ({year}) hangs in the {self.museum}.'

print(Painting(input(), input(), input()).descr)