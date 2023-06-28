# Cell Painting Script
First landing for the in-house cell painting script - work in progress.

## Setting up the python
Setting up the python on the system via pyenv (https://github.com/pyenv-win/pyenv-win)

Open powershell (terminal VIA MS store) + run:

`&"${env:PYENV_HOME}\install-pyenv-win.ps1"`

`pyenv update`

`pyenv install -l`

Check out which versions of Python are available:

`pyenv versions`

Set global python for the computer:

`pyenv global 3.11.4`

## Setting up the enviroment and requirements

On GitHub --> Code --> Download ZIP

Deploy the download locally and use the terminal to establish Python environment using the following steps:

Move the working directory in terminal to selected local deployment. 
Set up local Python version for the chosen folder:

`pyenv local 3.11.4`

Setting up local working environment:

`python -m venv .venv`

Activate the environment:

`.\.venv\Scripts\activate`

Upgrade pip for installing dependencies:

`python -m pip install --upgrade pip`

Install the dependancies:

`pip install -r .\requirements.txt`

