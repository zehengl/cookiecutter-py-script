<div align="center">
    <img src="https://cdn4.iconfinder.com/data/icons/cookie-flat-color-2/512/1-512.png" alt="logo" height="196">
</div>

# cookiecutter-py-script

A cookiecutter template for python scripts

## Prerequisites

- Git

## Usage

    pip install cookiecutter
    cookiecutter gh:zehengl/cookiecutter-py-script

## Develop

Use virtual environment and set up development dependencies.

    python -m venv .venv
    .\.venv\Scripts\activate
    pip install -r requirements-dev.txt

Run the follow command periodically to update template's dependencies.

    pcu ".\{{cookiecutter.name}}\requirements-dev.txt" -u

## Credits

- [Logo][1] by [Andika .][2]

[1]: https://www.iconfinder.com/icons/5241573/bakery_christmas_cookie_cupcake_pastry_winter_icon
[2]: https://www.iconfinder.com/Sinkandika
