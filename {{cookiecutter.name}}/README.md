<div align="center">
    <img src="{{cookiecutter.img}}" alt="logo" height="196">
</div>

# {{cookiecutter.name}}

![coding_style](https://img.shields.io/badge/code%20style-black-000000.svg)

{{cookiecutter.description}}

## Install

    python -m venv venv
    {%- if cookiecutter.running_on_windows == "yes" %}
    .\venv\Scripts\activate
    {%- else %}
    source venv/bin/activate
    {%- endif %}
    python -m pip install -U pip
    pip install -r requirements.txt

Use `pip install -r requirements-dev.txt` for development.
It will install `pylint` and `black` to enable linting and auto-formatting.
{%- if cookiecutter.enable_jupyterlab == "yes" %}
It will also install `jupyterlab` for notebook experience.
{%- endif %}

## Usage

## Credits
