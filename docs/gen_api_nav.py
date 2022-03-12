"""Plugin for generate API docs."""

# Import built-in modules
from pathlib import Path

# Import third-party modules
import mkdocs_gen_files


def main():
    nav = mkdocs_gen_files.Nav()
    root = Path(__file__).parent.parent
    api_root = root.joinpath("photoshop")
    print(api_root)
    for path in sorted(Path(api_root).glob("**/*.py")):
        module_path = path.relative_to(root).with_suffix("")
        doc_path = path.relative_to(root).with_suffix(".md")
        full_doc_path = Path(doc_path)
        parts = list(module_path.parts)
        if parts[-1] == "__init__":
            parts = parts[:-1]
            doc_path = doc_path.with_name("index.md")
            full_doc_path = full_doc_path.with_name("index.md")
        elif parts[-1] == "__main__":
            continue
        nav_parts = list(parts)
        nav[nav_parts] = doc_path
        with mkdocs_gen_files.open(full_doc_path, "w") as fd:
            ident = ".".join(parts)
            print(f"::: " + ident, file=fd)

        mkdocs_gen_files.set_edit_path(full_doc_path, path)

    with mkdocs_gen_files.open("api.md", "w") as nav_file:
        nav_file.writelines(nav.build_literate_nav())


if __name__ == "<run_path>":
    main()
