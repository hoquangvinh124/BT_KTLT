import xml.etree.ElementTree as ET
from ClassInfo import *

class MusicManager:
    def __init__(self):
        self.singers = []
        self.songs = []

    def load_singers(self, filename="singer.xml"):
        tree = ET.parse(filename)
        root = tree.getroot()
        for elem in root.findall("Singer"):
            code = elem.find("SingerCode").text
            name = elem.find("SingerName").text
            self.singers.append(Singer(code, name))

    def load_songs(self, filename="song.xml"):
        tree = ET.parse(filename)
        root = tree.getroot()
        for elem in root.findall("Song"):
            song_code = elem.find("SongCode").text
            song_name = elem.find("SongName").text
            composer_name = elem.find("ComposerName").text
            singer_codes = [s.text for s in elem.find("Singers").findall("SingerCode")]
            self.songs.append(Song(song_code, song_name, composer_name, singer_codes))

    def get_singer_list(self):
        return [s.singer_name for s in self.singers]

    def get_songs_by_singer(self, singer_name):
        singer_code = None
        for singer in self.singers:
            if singer.singer_name == singer_name:
                singer_code = singer.singer_code
                break

        if not singer_code:
            return []

        result = []
        for song in self.songs:
            if singer_code in song.singer_codes:
                result.append((song.song_name, song.composer_name))
        return result

