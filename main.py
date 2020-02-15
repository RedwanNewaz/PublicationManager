from OrganizeBib import batch_processing, sort_bib_data
import os
from argparse import ArgumentParser
import logging

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--file', type = str, required = True, help = "location of the bib file?")
    parser.add_argument('--debug', action='store_true', default=False, help=' show log in the console?')

    arg = parser.parse_args()
    input_file = arg.file

    if(arg.debug):logging.basicConfig(level=logging.DEBUG)

    temp_dir = 'output/splited_bib/'
    output_dir = "output/splited_tex/"
    os.makedirs(temp_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)

    sort_bib_data(input_file, temp_dir)
    batch_processing(temp_dir, output_dir)

    print("[INFO]: output written in (%s)"%output_dir)

    

