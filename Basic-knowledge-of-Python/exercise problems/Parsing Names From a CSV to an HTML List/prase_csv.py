# -*- coding: utf-8 -*-
import  csv

html_output = ''
names = []

with open('prase.csv', 'r') as data_file:
    csv_data = csv.DictReader(data_file)

    # we don't want first line of bad data
    next(csv_data)

    for line in csv_data:
        if line['Firstname'] == 'Reward':
            continue
        names.append(f"{line['Firstname']} {line['Lastname']}")

html_output += f'<p>There are currently {len(names)} public contributors. Thank You!</p>'
html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'

html_output += '\n</ul>'
print(html_output)
