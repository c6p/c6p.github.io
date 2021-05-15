from csv import reader
from os import system

with open('skills.csv') as f:
  c = reader(f, delimiter=';', quotechar='"')
  next(c)
  d = {r[0]:r for r in c} # 0:id, 1:name, 2:type, 3:status, 4:depends, 5:url, 6:desc
  nodes = '\n'.join([f'''"{r[1]}" [id="{r[0]}" title="{r[6]} " {'href="'+r[5]+'"' if r[5] else ''} class="{r[2]} size-{r[3]}" label=<<font point-size="{float(r[3])/2+10}">{r[1]} <b>{r[3]}</b></font>>]''' for k,r in d.items()])
  edges = '\n'.join([f'"{d[e][1]}" -> "{r[1]}"' for k,r in d.items() for e in r[4].split(',') if e in d])

  with open('skills.dot', 'w') as svg:
    svg.write(f'''digraph "skills" {{
      outputorder=edgesfirst
      graph[id="skills" rankdir=LR, center=true, margin=0, nodesep=0, ranksep=0]
      node[shape=none, margin=0.01]
      edge[arrowsize=0.6, arrowhead=vee color="#c9d1d9"]
      {nodes}
      {edges}
    }}''')

  system('dot -Tsvg skills.dot -o ../assets/skills.svg')