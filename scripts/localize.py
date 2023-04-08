import re

NEW_LINWS = []
LOCALIZE_PATTERN_PART_1 = r'\/revision\/latest\?cb=\d*'
LOCALIZE_PATTERN_PART_2 = r'https:\/\/static.wikia.nocookie.net\/darkestdungeon_gamepedia\/images\/.\/..\/'

with open('soundboard.html', 'r') as file_name:
    lines = [line.rstrip() for line in file_name]

    for line in lines:
        tmp_line = re.sub(LOCALIZE_PATTERN_PART_1, '', line, count=0, flags=0)
        NEW_LINWS.append(re.sub(LOCALIZE_PATTERN_PART_2, 'audio/', tmp_line, count=0, flags=0))

with open('localized_soundboard.html', mode='wt', encoding='utf-8') as file:
    for line in NEW_LINWS:
        file.write("%s\n" % line)