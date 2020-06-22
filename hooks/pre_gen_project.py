import re
import os
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

module_name = '{{ cookiecutter.project_slug}}'

if not re.match(MODULE_REGEX, module_name):
    print('ERROR: The project slug (%s) is not a valid Python module name. Please do not use a - and use _ instead' % module_name)

    #Exit to cancel project
    sys.exit(1)

REMOVE_PATHS = [
    '{% if cookiecutter.packaging != "pip" %} requirements.txt {% endif %}',
    '{% if cookiecutter.packaging != "conda" %} environment.yml {% endif %}',
    '{% if cookiecutter.image_recognition != "y" %} resources/test {% endif %}',
    '{% if cookiecutter.image_recognition != "y" %} resources/train {% endif %}',
    '{% if cookiecutter.manual_Docker_containers != "y" %} Dockerfile {% endif %}',
    '{% if cookiecutter.manual_Docker_containers != "y" %} entrypoint.sh {% endif %}'
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            os.rmdir(path)
        else:
            os.unlink(path)
