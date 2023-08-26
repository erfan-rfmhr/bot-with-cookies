# Cookie Python Bot
Structure your python bot project with cookie! <a href="https://github.com/cookiecutter">Cookiecutter<a> is a python package that helps you structure and
organize your project easy and fast. Check it out in the official <a href="https://cookiecutter.readthedocs.io/en/stable/">documentation<a>.
<hr>

## Tree
This will be your project folder after you run cookie:

    ├───database
    ├───docs
    ├───logs
    ├───services
    ├───tests
    │   └───units
    └───{{cookiecutter.project_slug}}
        ├───commands
        │   └───admin
        ├───errors
        └───handlers
            └───admin
<hr>

## How to use?
First install cookiecutter:<br>
- `pip install cookiecutter`<br>

Then run cookie on this repo:<br>
- `cookie <url>`