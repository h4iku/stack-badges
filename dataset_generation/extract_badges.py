from collections import defaultdict

import xmltodict

begin_year = 2008
end_year = 2010

user_badges = defaultdict(set)

with open('Badges.xml') as xml_file:
    for element in xml_file:
        if element.strip().startswith('<row'):
            row = xmltodict.parse(element)['row']
            if begin_year <= int(row['@Date'].split('-')[0]) <= end_year:
                user_badges[row['@UserId']].add(row['@Name'])

with open('badges.csv', 'w') as output:
    for user, badges in user_badges.items():
        output.write(user + ',' + ','.join(badges) + '\n')
