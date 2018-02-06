# by Sangheli a.savel.vic@gmail.com

import json
from src import CommandList, ComboList
import os

def process():
    path = os.getcwd()
    file = path + os.sep + "commands.json"

    json_data = json.load(open(file))

    combolist = []
    combonames = []

    for cn in json_data:

        command_name = []
        command_str = []

        for command in json_data[cn][0]:
            command_name.append(command)
            command_str.append(json_data[cn][0][command])

        dictionary = dict(zip(command_name, command_str))
        dictionary = sorted(dictionary.items())

        command_name = []
        command_str = []

        for item in dictionary:
            command_name.append(item[0])
            command_str.append(item[1])

        comlist = CommandList.CommandList(command_name, command_str)
        combo = ComboList.ComboList(cn, comlist)

        combolist.append(combo)

        combonames.append(cn)


    return combolist,combonames