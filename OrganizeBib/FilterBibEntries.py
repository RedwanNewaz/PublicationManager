from pip._vendor.pyparsing import unicode
from pybtex.database.input import bibtex
from pybtex.database import BibliographyData, Entry
import re
from .Bib2Tex import logger

def read_bibfile(file):
    parser = bibtex.Parser()
    bib_data = parser.parse_file(file)
    return bib_data.entries

def author_items(name, data):
    count = 0
    for i, d in enumerate(data):
        author = data[d].persons.get('author', None)
        if(author):
            names = [unicode(person) for person in author]
            all_names = " ".join(names)
            if(isinstance(name, list)):
                findName = any([re.search(n, all_names, re.IGNORECASE) for n in name])
            else:
                findName = re.search(name, all_names, re.IGNORECASE)
            if( findName):
                yield d
                count += 1
    logger.debug("[INFO] Total entries of author %s: %s" %(name, count))


def write_result(output, filter_data, data):
    write_bib = BibliographyData({key:data[key] for key in filter_data})
    need_modification = write_bib.to_string('bibtex')
    with open(output, 'w', encoding='utf-8') as file:
        file.write(need_modification)

def filterBy(input, output, name):
    data = read_bibfile(input)
    filter_data = author_items(name, data)
    write_result(output=output, filter_data = filter_data, data=data)









