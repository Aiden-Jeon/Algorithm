#!/usr/bin/env python3
import os
from pathlib import Path


ROOT_DIR = Path(__file__).parent.parent


def make_docs_dir(filename: str):
    md_name = str(filename).replace(".py", ".md").replace("src", "docs")
    md_dir = ROOT_DIR / md_name
    print(filename, "------>", md_dir)
    md_dir.parent.mkdir(exist_ok=True, parents=True)
    return md_dir


def make_docs(filename: str, context: list, code: list):
    md_dir = make_docs_dir(filename)
    with open(md_dir, "w") as f:
        context = "".join(context)
        code = "".join(code)
        f.write(context)
        f.write("\nsource code: \n")
        f.write("```python\n")
        f.write(code)
        f.write("```\n")


def split_context(filename: str):
    context = []
    code = []
    with open(filename, "r") as f:
        line = f.readline()
        if line.startswith('"""'):
            is_context = True
            while line:
                line = f.readline()
                if line.startswith('"""'):
                    is_context = False
                elif is_context:
                    context += [line]
                else:
                    code += [line]
    return context, code


def main():
    src_dir = ROOT_DIR / "src"
    dirs = [src_dir / d for d in os.listdir(src_dir)]
    while dirs:
        dir_name = dirs.pop()
        if os.path.isdir(dir_name):
            sub_dirs = [dir_name / d for d in os.listdir(dir_name)]
            dirs.extend(sub_dirs)
        else:
            context, code = split_context(dir_name)
            if len(context) > 0:
                make_docs(dir_name, context, code)


if __name__ == "__main__":
    main()
