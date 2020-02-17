
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

### Pro tip
You can use the following command to learn more about the supported arguments 
```
python main.py --help
```
