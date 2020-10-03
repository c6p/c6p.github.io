# Generate tabbed markdown code blocks from Exercism solutions
from os import walk, path
from textwrap import indent

ROOT = path.join('assets', 'exercism')

rules = {
  'javascript': lambda x: x+'.js',
  'python': lambda x: x.replace('-', '_')+'.py',
  'rust': lambda x: 'src/lib.rs',
}

langs = [l for l in next(walk(ROOT))[1] if not l.startswith('.')]

exercises = {}
for l in langs:
  for e in next(walk(path.join(ROOT, l)))[1]:
    exercises.setdefault(e, []).append(l)

def readall(path):
  with open(path,mode='r') as f:
    return f.read()

md = '# Exercism\n[My exercism profile: c6p](https://exercism.io/profiles/c6p)\n\n'
for exercise, langs in sorted(exercises.items()):
  md += '### {0}\n\n'.format(exercise)  # title
  files = [(path.join(ROOT, l, exercise, rules[l](exercise)), l) for l in langs]
  for code, lang in files:
    md += '=== "{0}"\n'.format(lang)
    md += indent('```{0}\n{1}\n```\n\n'.format(lang, readall(code)), '    ')

print(md)
