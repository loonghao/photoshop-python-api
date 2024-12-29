"""Plugin for generate API docs."""

# Import built-in modules
from __future__ import annotations

import os
from pathlib import Path

import mkdocs_gen_files
import stringcase

# Import third-party modules
from jinja2 import Template

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

""",
)


class Examples:
    def __init__(self, root: Path) -> None:
        self._root = root

    def get_examples(self) -> list[Path]:
        return [file_ for file_ in self._root.glob("*.py") if "_psd_files.py" not in file_.as_posix()]

    @staticmethod
    def convert_relative_path(file: str) -> str:
        path = file.split("examples")[1]
        return "../examples{}".format(path.replace("\\", "/"))

    @staticmethod
    def get_name(file: str) -> str:
        name = Path(file).name.split(".py")[0]
        return stringcase.titlecase(name)

    @staticmethod
    def get_line(name: str) -> str:
        return "-" * len(name)

    @staticmethod
    def get_content(file_: str) -> str:
        with Path(file_).open() as f:
            return "".join(f.readlines())


def main() -> None:
    root = Path(__file__).parent.parent
    with mkdocs_gen_files.open("examples.md", "w") as nav_file:
        examples_data = Examples(root.joinpath("examples"))
        nav_file.write(template.render(Examples=examples_data))


if __name__ == "__main__":
    main()
