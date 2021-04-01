#!/usr/bin/env python3
from datetime import datetime
import os
from pathlib import Path
import time
from typing import List, Tuple


ROOT_DIR = Path(__file__).parent.parent


def make_docs_dir(file_dir: Path, sitename: str) -> str:
    file_name = f"{file_dir.name}"
    file_name = file_name.replace(".py", ".md")
    md_dir = ROOT_DIR / "docs/algorithm" / sitename / file_name
    print(file_dir, "------>", md_dir)
    md_dir.parent.mkdir(exist_ok=True, parents=True)
    return md_dir


def make_docs(
    file_dir: Path, header: list, context: list, code: list, sitename: str
) -> None:
    md_dir = make_docs_dir(file_dir, sitename)
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


def split_context(
    file_dir: Path, sitename: str
) -> Tuple[List[str], List[str], List[str]]:
    # created = time.ctime(os.path.getctime(file_dir))
    # created = datetime.strptime(created, "%a %b %d %H:%M:%S %Y").strftime("%Y-%m-%d")
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
                    header = [
f"""---
{line.strip()}
"""
                    ]
                elif line.startswith("date"):
                    header += [
f"""{line.strip()}
categories: [algorithm]
tags: [{sitename}]
toc: true
author: Jongseob Jeon
---\n
"""
                    ]
                elif is_context:
                    context += [line]
                else:
                    code += [line]
    return header, context, code


def main():
    src_dir = ROOT_DIR / "src"
    for sitename in ["acmicpc", "leetcode"]:
        site_dir = src_dir / sitename
        if sitename not in os.listdir(src_dir):
            continue
        dirs = [site_dir / d for d in os.listdir(site_dir)]
        print(dirs)
        while dirs:
            dir_name = dirs.pop()
            if os.path.isdir(dir_name):
                sub_dirs = [dir_name / d for d in os.listdir(dir_name)]
                dirs.extend(sub_dirs)
            else:
                header, context, code = split_context(dir_name, sitename)
                if len(context) > 0:
                    make_docs(dir_name, header, context, code, sitename)


if __name__ == "__main__":
    main()
