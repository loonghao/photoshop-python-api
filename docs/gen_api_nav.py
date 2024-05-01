"""Plugin for generate API docs."""
# Import built-in modules
from pathlib import Path

import mkdocs_gen_files
# Import third-party modules


def main():
    nav = mkdocs_gen_files.Nav()
    root = Path(__file__).parent.parent
    api_root = root.joinpath("photoshop")
    for path in sorted(Path(api_root).glob("**/*.py")):
        module_path = path.relative_to(root).with_suffix("")
        doc_path = path.relative_to(root).with_suffix(".md")
        full_doc_path = Path("reference", doc_path)
        parts = list(module_path.parts)
        if parts[-1] == "__init__":
            continue
        elif parts[-1] == "__main__":
            continue
        elif parts[-1] == "__version__":
            continue
        nav_parts = list(parts)
        if nav_parts[-1].startswith("_"):
            nav_parts[-1] = nav_parts[-1][1:]
        nav[nav_parts] = doc_path.as_posix().replace("\\", "/")
        full_doc_path = full_doc_path.as_posix().replace("\\", "/")
        with mkdocs_gen_files.open(full_doc_path, "w") as fd:
            ident = ".".join(parts)
            print(f"::: " + ident, file=fd)

        mkdocs_gen_files.set_edit_path(full_doc_path, path.as_posix().replace("\\", "/"))

    with mkdocs_gen_files.open("reference/SUMMARY.md", "w") as nav_file:
        nav_file.writelines(nav.build_literate_nav())


if __name__ == "<run_path>":
    main()
