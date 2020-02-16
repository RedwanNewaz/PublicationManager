# Y. Wang, S. Chaudhuri, and L.E. Kavraki, “Point-Based Policy Synthesis for POMDPs with Boolean and
# Quantitative Objectives,” IEEE Robotics and Automation Letters, 2019, 4(2): 1860-1867.
# name, "\textit{title}", \textbf{journal}, year, volume page

from pybtex.database.input import bibtex
from pathlib import Path
import logging
logger = logging.getLogger('[Bib2Tex]')

class TexEntry:
    template = '\item %s, ``\\textit{%s}", \\textbf{%s}, %s, %s'
    no_page_template = '\item %s, ``\\textit{%s}", \\textbf{%s}, %s'

    def get_name(self, person):
        authors = [ " ".join(p.first_names+ p.middle_names +p.last_names) for p in person]
        return ", ".join(authors)
    def __call__(self, *args, **kwargs):
        entry = args[0]
        self.author = self.get_name(args[1])
        self.title = entry.get('title', None)
        self.journal = entry.get('journal', None)

        if(not self.journal):
            self.journal = entry.get('publisher', None)
            self.isbn = entry.get('isbn',None)

        self.year = entry.get('Year', None)
        self.pages = entry.get('pages', None)




    def get_reference(self):
        fields = vars(self)

        # removing none fields
        header = list(filter(lambda x: fields[x], fields))
        # minimum 3 fields

        N = len(header) - 3
        template = '\item %s, ``\\textit{%s}", \\textbf{%s}'
        if (N>0):
            # add additional fields: page, book
            for _ in range(N):
                template += ", %s"

        values = list(fields[f] for f in fields if fields[f])
        # print(template, tuple(values))
        output = template%tuple(values)
        # print(output)

        return output
        # print(entry)
    def __str__(self):
        return self.__repr__()
    def __repr__(self):
        return self.get_reference()

template = '''
\\begin{enumerate}
%s
\end{enumerate}
'''

def make_list(data):
    body = template%(data)
    return body

def make_tex(input, output):

    parser = bibtex.Parser()
    bib_data = parser.parse_file(input)
    tex = TexEntry()
    try:
        data = []
        for e in bib_data.entries:
            tex(bib_data.entries[e].fields, bib_data.entries[e].persons['author'])
            data.append(str(tex))
        data = "\n".join(data)
        writableTxt = make_list(data)
        if('\\\\' in writableTxt):
            writableTxt = writableTxt.replace('\\\\', '\\')
        with open(output, 'w', encoding='utf-8') as file:
            file.write(writableTxt)
        logger.debug("[INFO] input = (%s) | output = (%s)" % (input, output))
    except:
        logger.error("[ERROR] (%s) could not process"%input)

    # print(writableTxt)

def batch_processing(dir_bib_files, output_dir):
    p = Path('.')
    bib_files = dir_bib_files + "/*.bib"
    output_file = output_dir + "{}.tex"
    inputs = p.glob(bib_files)
    for file in inputs:
        name = file.name.split('.')[0]
        make_tex(file, output_file.format(name))
