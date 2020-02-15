from pybtex.database.input import bibtex
from pybtex.database import BibliographyData, Entry
from pprint import pprint, pformat
from collections import defaultdict
from .Bib2Tex import logger
def write_result(name, new_data):
    """:param new_data is the dictionary of entries"""
    write_bib = BibliographyData(new_data)
    need_modification = write_bib.to_string('bibtex')
    with open("%s" % name, 'w', encoding='utf-8') as file:
        file.write(need_modification)

def findBibType(data):
    output = defaultdict(list)
    for entry in data.entries:
        output[data.entries[entry].type].append(entry)
    return output

def sort_bib_data(input, output):
    parser = bibtex.Parser()
    bib_data = parser.parse_file(input)
    sorted_data = findBibType(bib_data)
    output_file = output + "/{}.bib"
    for key in sorted_data:
        name = output_file.format(key)
        entries = sorted_data[key]
        data = {bib : bib_data.entries[bib] for bib in entries}
        write_result(name, data)
    logger.debug(pformat(sorted_data))

if __name__ == '__main__':
    input_file = 'InputFile/kavrakilab.bib'
    output_dir = 'OrganizeBib'
    sort_bib_data(input_file, output_dir)


