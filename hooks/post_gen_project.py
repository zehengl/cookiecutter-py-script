import os
import shutil
import subprocess

folder = os.getcwd()

if not "{{cookiecutter.using_pyenv}}" == "yes":
    with open(os.path.join(folder, ".python-version"), "w") as f:
        f.write("{{cookiecutter.python}}\n")

if not "{{cookiecutter.writing_docs}}" == "yes":
    shutil.rmtree(os.path.join(folder, "docs"))
    os.remove(os.path.join(folder, "mkdocs.yml"))

message = "initial commit from gh:zehengl/cookiecutter-py-script"

subprocess.call(["git", "init"])
subprocess.call(["git", "add", "*"])
subprocess.call(["git", "commit", "-m", message])
