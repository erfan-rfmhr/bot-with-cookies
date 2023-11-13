# Cookie Python Bot

Structure your python bot project with cookie! [Cookiecutter](https://github.com/cookiecutter) is a python package that helps you structure and
organize your project easy and fast. Check it out on the official [documentation](https://cookiecutter.readthedocs.io/en/stable/).

---

## Tree

This will be your project folder after you run cookie:

    ├───config
    ├───database
    ├───docs
    ├───logs
    ├───repo
    │   └───interface
    ├───services
    ├───tests
    │   └───units
    └───{{cookiecutter.project_slug}}
        ├───commands
        │   ├───admin
        │   └───core
        ├───errors
        └───handlers
            ├───admin
            └───core

---

## How to use?

First install cookiecutter:

- `pip install cookiecutter`

Then run cookie on this repo:

- `cookiecutter https://github.com/erfan-rfmhr/bot-with-cookies.git`
