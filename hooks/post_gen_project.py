import os
import shutil
import subprocess


if not "{{cookiecutter.writing_docs}}" == "yes":
    folder = os.getcwd()
    shutil.rmtree(os.path.join(folder, "docs"))
    os.remove(os.path.join(folder, "mkdocs.yml"))

message = "initial commit from gh:zehengl/cookiecutter-py-script"

subprocess.call(["git", "init"])
subprocess.call(["git", "add", "*"])
subprocess.call(["git", "commit", "-m", message])
