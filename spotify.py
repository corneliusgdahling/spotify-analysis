import json
import os
from collections import defaultdict

line_with_pipes = "|"+"-"*147+"|"
line = "-"*149

def list_songs_played():
    songs = defaultdict(list)
    with open('StreamingHistory.json') as f:
        json_data = json.load(f)
    num_streams = len(json_data)
    for stream in json_data:
        if stream['trackName'] in songs:
            songs[stream['trackName']] += 1
        else:
            songs[stream['trackName']] = 1
    
    dict_keys = list(songs.keys())
    for key in dict_keys:
        new_key = key
        if len(new_key) <= 50:
            continue
        if "-" in new_key:
            index = new_key.index("-")
            new_key = key[:index]
        if "(" in new_key:
            index = new_key.index("(")
            new_key = key[:index]
        if "[" in new_key:
            index = new_key.index("[")
            new_key = key[:index]
        if len(new_key) > 50:
            key_split = new_key.split()
            counter = 0
            index = 0
            for i, item in enumerate(key_split):
                counter += len(item) + 1 # + 1 because the space is split
                if counter > 50:
                    index = counter - len(item) - 2
                    break
            new_key = key[:index] + " ..."
        songs[new_key] = songs.pop(key, 0)


    tuple_list = [(k, v) for k, v in songs.items()]
    tuple_list.sort(reverse=True, key=lambda x: x[1])

    print(line)
    print("| %6s | %60s | %60s | Percentage |" % ("Index", "Song  name", "Number of streams since 26.05.2018"))
    print(line_with_pipes)
    counter = 1
    for key, value in tuple_list:
        percentage = round((value / num_streams) * 100, 2)
        print("| %6d | %60s | %60s | %9.2f%% |" % (counter, key, value, percentage))
        counter += 1
    print(line_with_pipes)
    
    print("| %6s | %60s | %60s |    100.00%% |" % ("", "Total", num_streams))
    print(line)



list_songs_played()