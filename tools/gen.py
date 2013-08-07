import os
import sys

number, project, title = sys.argv[1:]

template = open("template.md").read()
setup = open("tools/setup.py").read()

solution = "%s.%s" % (number, project)
fname = "%s.md" % solution

if not os.path.exists("solutions/" + solution):
    os.mkdir("solutions/" + solution)

with open("problems/" + fname, 'w') as f:
    problem_out = template.replace('Title', title.strip())
    f.write(problem_out)

with open("solutions/" + solution + "/setup.py", 'w') as f:
    project_out = setup.replace('NAME', project.strip())
    f.write(project_out)

os.mkdir("solutions/" + solution + "/" + project)
open("solutions/" + solution + "/" + project + "/__init__.py", "w").close()

