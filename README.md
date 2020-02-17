
# How to use
To use this either you can use docker platform or python virtual environment. 
For docker platform, please visit [this](https://hub.docker.com/repository/docker/redwan06me/publicationmanager/general) link.

## How to build

### Build python virtual environment
```
python venv -m ./venv
```
Please use the python and pip from the venv folder. 
### Install dependencies 
```
pip install -r requirements.txt 
```

## Supported arguments 
* --file : a single bib file that contains all the information  
* --debug: show debugging information in the console 
* -- filterBy:  filter a bib file based on the author surname
* --recompile: recompiling existing splited bib files

By default, this program will categorize your single bib file into multiple bib files. 
Then it will create corresponding tex files based on those bib files so that you can input them (tex files) in your latex resume.
If there are some entries in your bib file where you are not a co-author, you can filter those entries by using filterBy argument. 
You may find the recompile argument is useful if you want to modify a splited bib file and create a new tex file based on your modification.

### Pro tip
You can use the following command to learn more about the supported arguments 
```
python main.py --help
```
