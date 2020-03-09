import os
import glob
from jinja2 import Template
import stringcase

template = Template(r"""
Usage
=====
{% for file_ in Examples.get_examples() %}
{{ Examples.get_name(file_) }}
{{ Examples.get_line(Examples.get_name(file_))}}
  .. literalinclude:: {{ Examples.convert_relative_path(file_) }}
{% endfor %}
    
""")


class Examples(object):
    def __init__(self, root):
        self._root = root

    def get_examples(self):
        return glob.glob(os.path.join(self._root, "*.py"))

    @staticmethod
    def convert_relative_path(file):
        path = file.split("examples")[1]
        return "../examples{}".format(path.replace("\\", "/"))

    @staticmethod
    def get_name(file):
        name = os.path.basename(file).split(".py")[0]
        return stringcase.titlecase(name)

    @staticmethod
    def get_line(name):
        return "-" * len(name)


if __name__ == '__main__':
    root = os.path.dirname(os.path.dirname(__file__))
    with open(os.path.join(root, "docs", "usage.rst"), "w") as f:
        f.write(template.render(
            Examples=Examples(os.path.join(root, "examples"))))
