"""Plugin for generate API docs."""

# Import built-in modules
import os
from pathlib import Path

# Import third-party modules
from jinja2 import Template
import mkdocs_gen_files
import stringcase


template = Template(
    r"""
Examples
========
{% for file_ in Examples.get_examples() %}
{{ Examples.get_name(file_) }}
{{ Examples.get_line(Examples.get_name(file_))}}
```python
{{ Examples.get_content(file_) }}
```
{% endfor %}

"""
)


class Examples(object):
    def __init__(self, root: Path):
        self._root = root

    def get_examples(self):
        files = [file_ for file_ in self._root.glob("*.py") if "_psd_files.py" not in file_.as_posix()]
        return files

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

    @staticmethod
    def get_content(file_):
        with open(file_, "r") as f:
            return "".join(f.readlines())


def main():
    root = Path(__file__).parent.parent
    with mkdocs_gen_files.open("examples.md", "w") as nav_file:
        examples_data = Examples(root.joinpath("examples"))
        nav_file.write(template.render(Examples=examples_data))


if __name__ == "<run_path>":
    main()
