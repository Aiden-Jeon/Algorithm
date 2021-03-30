#!/usr/bin/env python3
from datetime import datetime
import os
from pathlib import Path
import time


ROOT_DIR = Path(__file__).parent.parent


def make_docs_dir(file_dir: Path):
    last_modified = time.ctime(os.path.getmtime(file_dir))
    last_modified = datetime.strptime(last_modified, "%a %b %d %H:%M:%S %Y").strftime(
        "%Y-%m-%d"
    )
    file_name = f"{last_modified}-{file_dir.name}"
    file_name = file_name.replace(".py", ".md")
    md_dir = ROOT_DIR / "docs/algorithm" / file_name
    print(file_dir, "------>", md_dir)
    md_dir.parent.mkdir(exist_ok=True, parents=True)
    return md_dir


def make_docs(file_dir: Path, header: list, context: list, code: list):
    md_dir = make_docs_dir(file_dir)
    with open(md_dir, "w") as f:
        header = "".join(header)
        context = "".join(context)
        code = "".join(code)
        f.write(header)
        f.write("\n")
        f.write(context)
        f.write("\n## source code \n")
        f.write("```python\n")
        f.write(code)
        f.write("```\n")


def split_context(file_dir: Path):
    header = []
    context = []
    code = []
    with open(file_dir, "r") as f:
        line = f.readline()
        if line.startswith('"""'):
            is_context = True
            while line:
                line = f.readline()
                if line.startswith('"""'):
                    is_context = False
                elif line.startswith("title"):
                    header += ["---\n"]
                    header += [line]
                    header += ["categories: [algorithm]\n"]
                    header += ["toc: true\n"]
                    header += ["toc_sticky: true\n"]
                    header += ["---\n"]
                elif is_context:
                    context += [line]
                else:
                    code += [line]
    return header, context, code


def main():
    src_dir = ROOT_DIR / "src"
    dirs = [src_dir / d for d in os.listdir(src_dir)]
    while dirs:
        dir_name = dirs.pop()
        if os.path.isdir(dir_name):
            sub_dirs = [dir_name / d for d in os.listdir(dir_name)]
            dirs.extend(sub_dirs)
        else:
            header, context, code = split_context(dir_name)
            if len(context) > 0:
                make_docs(dir_name, header, context, code)


if __name__ == "__main__":
    main()
