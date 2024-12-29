"""Plugin for generate API docs."""

# Import built-in modules
from __future__ import annotations

from pathlib import Path
import re
import shutil

# Import third-party modules
import mkdocs_gen_files
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
    """Class for handling example files generation."""

    def __init__(self, root: Path) -> None:
        """Initialize Examples class.
        
        Args:
            root: Root directory path.
        """
        self._root = root

    def get_examples(self) -> list[Path]:
        """Get list of example files.
        
        Returns:
            List of example file paths.
        """
        return sorted([file_ for file_ in self._root.glob("*.py") if "_psd_files.py" not in file_.as_posix()])

    @staticmethod
    def convert_relative_path(file: str) -> str:
        """Convert file path to relative path.
        
        Args:
            file: File path to convert.
            
        Returns:
            Relative path string.
        """
        # Use raw string for regex pattern
        return re.sub(r"\W+", "", str(file))

    @staticmethod
    def get_name(file: str) -> str:
        """Get example name from file path.
        
        Args:
            file: File path.
            
        Returns:
            Example name in title case.
        """
        name = Path(file).stem
        return name.replace("_", " ").title()

    @staticmethod
    def get_line(name: str) -> str:
        """Generate underline for example name.
        
        Args:
            name: Example name.
            
        Returns:
            String of dashes matching name length.
        """
        return "-" * len(name)

    @staticmethod
    def get_content(file_: str) -> str:
        """Get content of example file.
        
        Args:
            file_: File path.
            
        Returns:
            File content as string.
        """
        with Path(file_).open(encoding='utf-8') as f:
            return "".join(f.readlines())


def main() -> None:
    """Generate examples documentation."""
    root = Path(__file__).parent.parent
    examples_dir = root / "examples"
    
    # 生成 examples.md 文件
    examples_data = Examples(examples_dir)
    content = template.render(Examples=examples_data)
    
    # 使用 mkdocs_gen_files 生成文件到正确的位置
    with mkdocs_gen_files.open("examples.md", "w", encoding='utf-8') as f:
        f.write(content)
        print("Generated examples.md")
    
    # 确保文件被写入到正确的位置
    mkdocs_gen_files.set_edit_path("examples.md", "docs/gen_examples.py")

    # 同时写入到 docs 目录
    docs_dir = root / "docs"
    docs_dir.mkdir(exist_ok=True)
    examples_file = docs_dir / "examples.md"
    
    # 如果文件已存在，先删除它
    if examples_file.exists():
        try:
            examples_file.unlink()
        except PermissionError:
            pass

    # 写入新文件
    examples_file.write_text(content, encoding='utf-8')
    print(f"Generated {examples_file}")


if __name__ == "__main__":
    main()
