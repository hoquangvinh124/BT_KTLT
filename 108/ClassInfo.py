class Singer:
    def __init__(self, singer_code, singer_name):
        self.singer_code = singer_code
        self.singer_name = singer_name

    def __str__(self):
        return f"{self.singer_name} ({self.singer_code})"

class Song:
    def __init__(self, song_code, song_name, composer_name, singer_codes):
        self.song_code = song_code
        self.song_name = song_name
        self.composer_name = composer_name
        self.singer_codes = singer_codes

    def __str__(self):
        return f"{self.song_name} - {self.composer_name}"