# Cookie Python Bot
Structure your python bot project with cookie! <a href="https://github.com/cookiecutter">Cookiecutter<a> is a python package that helps you structure and
organize your project easy and fast. Check it out on the official <a href="https://cookiecutter.readthedocs.io/en/stable/">documentation<a>.
<hr>

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
<hr>

## How to use?
First install cookiecutter:<br>
- `pip install cookiecutter`<br>

Then run cookie on this repo:<br>
- `cookiecutter https://github.com/erfan-rfmhr/bot-with-cookies.git`