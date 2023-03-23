<div align="center">
    <img src="{{cookiecutter.img}}" alt="logo" height="128">
</div>

# {{cookiecutter.name}}

![coding_style](https://img.shields.io/badge/code%20style-black-000000.svg)

{{cookiecutter.description}}

## Environment

{% set python_versions = cookiecutter.python.split('.') %}- Python {{ python_versions[0] }}.{{ python_versions[1] }}

## Getting Started

    python -m venv .venv
    {%- if cookiecutter.running_on_windows == "yes" %}
    .venv\Scripts\activate
    {%- else %}
    source .venv/bin/activate
    {%- endif %}
    python -m pip install -U pip
    pip install -r requirements.txt

> Use `pip install -r requirements-dev.txt` for development and docs.

{%- if cookiecutter.writing_docs == "yes" %}

## Docs

    mkdocs serve

{%- endif %}

## Credits
