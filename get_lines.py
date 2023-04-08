from bs4 import BeautifulSoup

NEW_LINWS = []
LINKS = []
with open('soundboard.html', 'r') as file_name:
    lines = [line.rstrip() for line in file_name]

    for line in lines:
        if not line.startswith('https') and not line.startswith('<h'):
            NEW_LINWS.append('<p>' + line + '</p>')
        elif line.startswith('https'):
            NEW_LINWS.append('<audio controls src="' + line + '"></audio>')
            LINKS.append(line)
        else:
            NEW_LINWS.append(line)

with open('soundboard.html', mode='wt', encoding='utf-8') as file:
    for line in NEW_LINWS:
        file.write("%s\n" % line)

with open('Links.txt', mode='wt', encoding='utf-8') as file:
    for link in LINKS:
        file.write("%s\n" % link)

LINKS = []
SECTIONS = []

# # with open('webpage.html', 'r') as file_name:
# #     lines = [line.rstrip() for line in file_name]
#
#     section = []
#     lines_to_skip = [
#         '<p>',
#         '<b>',
#         '</b>',
#         '</p>',
#         '<table style="background:transparent">',
#         '<tbody>',
#         '<tr>',
#         '<td>',
#         '</td>',
#         '</tr>',
#         '</tbody>',
#         '</table>',
#         '<div class="floatleft">',
#         '</div>',
#         '<span>',
#         '</audio>',
#         '</span>',
#     ]
#     items_to_skip = [
#         '<td style="color: #b2b7f2;',
#         '<audio hidden="" ',
#         '<a class="ext-audiobutton"',
#         '<img alt="SoundIcon.png"',
#         '<a href="https://static.wikia.nocookie.net/',
#         '<span class="mw-editsection-bracket">',
#         '<span class="mw-editsection">',
#     ]
#
#     for line in lines:
#         line_cleaned = line.strip()

#         if line_cleaned not in lines_to_skip:
#             if not line_cleaned.startswith(tuple(items_to_skip)):
#
#                 if line_cleaned.startswith('<a href="'):
#                     soup = BeautifulSoup(line, 'lxml')
#                     link = soup.find('a')
#                     line_cleaned = link.string
#                 elif line_cleaned.startswith('<source src="https:'):
#                     soup = BeautifulSoup(line, 'lxml')
#                     link = soup.find('source')
#                     line_cleaned = link['src']
#                 # elif line_cleaned.startswith('<span class="mw-headline"'):
#                 #     line_dirty = line + '</span>'
#                 #     soup = BeautifulSoup(line_dirty, 'lxml')
#                 #     link = soup.find('span', {'class': 'mw-headline'})
#                 #     print(link)
#                 #     line_cleaned = link.string
#                 #     if line_cleaned is None or line_cleaned == 'None':
#                 #         print('Is none!')
#                 #         print(line_cleaned)
#                 elif line_cleaned.startswith('<i>'):
#                     line_cleaned = line_cleaned.replace('<i>', '').replace('</i>', '')
#
#                 SECTIONS.append(line_cleaned)
#
# with open('data.html', mode='wt', encoding='utf-8') as file:
#     for line in SECTIONS:
#         file.write("%s\n" % line)


# with open('webpage.html', 'r') as f:
#     soup = BeautifulSoup(f.read(), 'lxml')
#
#
# for paragraph in soup.find_all('p'):
#     section_soup = soup.new_tag('section')
#     section_soup.append(copy(paragraph))
#     if paragraph.findNext('p') is not None:
#         section_soup.append(paragraph.findNext('p'))
#         paragraph.insert_before(section_soup)
#         paragraph.extract()

# with open('data.html', mode='wt', encoding='utf-8') as file:
#     file.write(str(soup))


# TABELs = soup.findAll('table', {'class': 'background:transparent'})
# DIVs = soup.findAll('div', {'class': 'floatleft'})
# TABELS = soup.findAll('audio', {'class':  'ext-audiobutton'})
# TABELS = soup.findAll('table', {'class': 'background:transparent'})