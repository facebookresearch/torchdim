import sys
import json
from pprint import pprint

data = json.load(sys.stdin)

cells = data["cells"]


temp = """\

```{{code-cell}} ipython3
{body}
```

"""

def join_indent(elems, indent=''):
    return ''.join(indent + (e if e.endswith('\n') else e + '\n') for e in elems)

for c in cells:
    if c["cell_type"] == "markdown":
        sys.stdout.write(join_indent(c["source"]) + '\n')
    elif c["cell_type"] == "code":
        body = join_indent(c["source"], indent='    ')
        if '!' not in body and len(c['outputs']) > 0 and 'text' in c['outputs'][0]:
            body = body + join_indent(c['outputs'][0]['text'], indent='    > ')
        sys.stdout.write(f'{body}\n')

sys.stdout.close()
