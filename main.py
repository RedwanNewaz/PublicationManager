from OrganizeBib import batch_processing, sort_bib_data, filterBy
from DatabaseManger import make_sql_database
import os
from argparse import ArgumentParser
import logging
from glob import glob

def arg_recompile():
    bib_exists = False
    try:
        files = glob(temp_dir + "*.bib")
        bib_exists = len(files) > 0
    except:
        print("[Error]: no bib files in %s !" % temp_dir)
        raise FileNotFoundError
    finally:
        if (not bib_exists):
            print("[Error]: no bib files in %s !" % temp_dir)
            raise FileNotFoundError

def arg_filerBy():
    # output folder check
    os.makedirs("output", exist_ok=True)
    # create output file name
    name = arg.filterBy
    print(name)
    if (isinstance(name, list)):
        name = "_".join(name)
    output = "output/%s.bib" % name
    # run the filterBy function
    filterBy(input=input_file, output=output, name=arg.filterBy)
    # don't run other programs
    print("[INFO]: output written in (%s)" % output)
    exit(0)

def arg_sql(file):
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)
    output = "%s/%s.db" % (output_dir, file.split('.')[-2])
    make_sql_database(input=file, output=output)
    print("[INFO]: output written in (%s)"%output)
    exit(0)

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--file', type = str, required = True, help = "location of the bib file?")
    parser.add_argument('--filterBy',  default = "", nargs='+', help = "keep entries of author name?")
    parser.add_argument('--debug', action='store_true', default=False, help='show log in the console?')
    parser.add_argument('--recompile', action='store_true', default=False, help='recompiling existing bib files in output/splited_bib/ directory?')
    parser.add_argument('--sql', action='store_true', default=False, help='create sql database from the bib file?')

    arg = parser.parse_args()
    input_file = arg.file
    recompile = arg.recompile


    if(arg.debug):logging.basicConfig(level=logging.DEBUG)
    # check whether the file exists or not
    if(not recompile and not os.path.exists(input_file)):
        print("[Error]: %s does not exit !"%input_file)
        raise FileExistsError

    if(len(arg.filterBy)>0): arg_filerBy()
    temp_dir = 'output/splited_bib/'
    # if recompile then check are there any bib files in output/splited_bib/ directory?
    if recompile: arg_recompile()

    if(arg.sql):arg_sql(arg.file)



    output_dir = "output/splited_tex/"
    os.makedirs(temp_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)

    if(not recompile):sort_bib_data(input_file, temp_dir)
    batch_processing(temp_dir, output_dir)

    print("[INFO]: output written in (%s)"%output_dir)

    

