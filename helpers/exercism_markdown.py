# Generate tabbed markdown code blocks from Exercism solutions
from os import walk, path
from textwrap import indent

ROOT = path.join('helpers', 'exercism')

rules = {
  'javascript': (lambda x: x+'.js', "## Setup"),
  'python': (lambda x: x.replace('-', '_')+'.py', "## Exception messages"),
  'rust': (lambda x: 'src/lib.rs', "## Rust Installation"),
}

langs = [l for l in next(walk(ROOT))[1] if not l.startswith('.')]

exercises = {}
for l in langs:
  for e in next(walk(path.join(ROOT, l)))[1]:
    exercises.setdefault(e, []).append(l)

def readall(p):
  with open(p,mode='r') as f:
    return f.read()

def readme(exercise,lang):
  with open(path.join(ROOT, lang, exercise, 'README.md'),mode='r') as f:
    lines = f.readlines()
    #desc = ''.join(lines[3:]).split(rules[lang][1])[0].strip('\n')
    #return (lines[2].strip('\n'), desc)
    title = lines[2].lstrip('#').strip('\n ')
    return f"{title} - [view](https://exercism.io/tracks/{lang}/exercises/{exercise})\n"

md = '# Exercism\n[My exercism profile: c6p](https://exercism.io/profiles/c6p)\n\n'
for exercise, langs in sorted(exercises.items()):
  md += f'### {exercise}\n\n'  # title
  md += f'{{{{< tabs "{exercise}" >}}}}\n'
  files = [(path.join(ROOT, l, exercise, rules[l][0](exercise)), l) for l in langs]
  for code, lang in files:
    md += f'{{{{< tab "{lang}" >}}}}\n'
    #title, desc = readme(exercise,lang)
    #md += indent(f'??? note "{title}"\n' + indent(desc, '    '), '    ') + '\n\n'
    md += readme(exercise,lang)
    md += f'```{lang}\n{readall(code)}\n```\n'
    md += '{{< /tab >}}\n'
  md += '{{< /tabs >}}\n\n'

print(md)
