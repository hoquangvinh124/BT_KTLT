import re

ex = input(r"Vui long nhap duong dan bai hat: ")

def path_with_mp3(s):
    res = re.split(r'[\\/]', s)
    return res[-1]

def path_without_mp3(s):
    with_music_path = path_with_mp3(s)
    without_music_path = with_music_path.split(".")
    return without_music_path[0]

print(path_with_mp3(ex))
print(path_without_mp3(ex))



