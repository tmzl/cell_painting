# Cell Painting Script
First landing for the in-house cell painting script - work in progress.

## Setting up the Python
Setting up the Python on the system via pyenv (https://github.com/pyenv-win/pyenv-win)

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

## Data structure

When saving data, to use our renaming.py, the data needs to be in the following structure.

CHEMICAL/data/biorep_X/day_X/channel

Be mindful not to use excess number of _ since we will use a regular expression in the CellProfiler based on the number of _ and folder structure.

## Running the pipeline

### Renaming the files

First step is to correctly rename all of the files for each chemical. Use the path to the CHEMICAL:

`python renaming.py --root-path=</path/to/txt/CHEMICAL>`

### CellProfiler feature extraction

After file renaming, we import the whole CHEMICAL folder into the CellProfiler.

Use this regex expression to correctly parse the file names:

`^(?P<Chemical>.*?_.*?)_(?P<Biorep>.*?_.*?)_(?P<Day>.*?_.*?)_(?P<Channel>.*?_.*?)_(?P<Well>[^_]*)_s(?P<Site>[^.]*)\.png$`

?? WHICH FILES TO COLLECT ??
Only MitoDay5Image.txt ?

?? 
Collect all relevant CellPainter into a specified folder.

### Pooling the CellProfiler data

Prepare the meta_table.txt according to the desired pooling option (sum / mean) for each column data type.

Run the script to pool all the data according to the meta_table.txt in a specified folder:

`python pooling_profiler.py --txt-dir=</path/to/txt/files>`