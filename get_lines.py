from bs4 import BeautifulSoup

LINKS = []
SECTIONS = []

with open('test.html', 'r') as file_name:
    lines = [line.rstrip() for line in file_name]

    section = []
    lines_to_skip = [
        '<p>',
        '<b>',
        '</b>',
        '</p>',
        '<table style="background:transparent">',
        '<tbody>',
        '<tr>',
        '<td>',
        '</td>',
        '</tr>',
        '</tbody>',
        '</table>',
        '<div class="floatleft">',
        '</div>',
        '<span>',
        '</audio>',
        '</span>',
    ]
    items_to_skip = [
        '<td style="color: #b2b7f2;',
        '<audio hidden="" ',
        '<a class="ext-audiobutton"',
    ]

    for line in lines:
        line_cleaned = line.strip()

        if line_cleaned.startswith('<p>'):
            if section:
                SECTIONS.append(section)
            section = []

        if line_cleaned not in lines_to_skip:
            if not line_cleaned.startswith(tuple(items_to_skip)):
                section.append(line_cleaned)

    SECTIONS.append(section)

    print(SECTIONS)

with open('data.html', mode='wt', encoding='utf-8') as file:
    for line in SECTIONS:
        file.write("%s\n" % line)


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