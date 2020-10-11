from sys import argv
from csv import reader

print('# Resources\n')

csvpath = argv[1]
html = ''
with open(csvpath, 'r') as csvfile:
    resources = reader(csvfile)
    next(resources) # discard header
    line = ["Topic", "Type", "Resource", "Detail"]
    html += '<div class="md-typeset__table"><table id="resource">'
    html += f"""<tr class="header">{''.join([f'<th class="left">{c}</th>' for c in line])}</tr>"""
    topics, types = set([(""," Select Topic...")]), set([(""," Select Type...")])
    for r in sorted(resources, key=lambda x: (x[0], x[2])):
        t0, t2 = f'{r[0]}1', f'{r[2]}1'
        topics.add((t0, r[0]))
        types.add((t2, r[2]))
        line = [r[0], r[2], f'<a href="{r[4]}">{r[3]}</a>', r[5] + (f'<br><img class="thumb" src="{r[6]}">' if r[6] else '')]
        html += f"""<tr class="{t0} {t2}">{''.join([f'<td class="left">{c}</td>' for c in line])}</tr>"""
    html += '</table></div>'

    print(f"""<select id="resource_topic" onchange="filter_resources()">{''.join([f'<option value="{v}">{t}</option>' for v,t in sorted(topics)])}</select>""",
    f"""<select id="resource_type" onchange="filter_resources()">{''.join([f'<option value="{v}">{t}</option>' for v,t in sorted(types)])}</select>""",
    html)
