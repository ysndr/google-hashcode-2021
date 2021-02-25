import sys

from importdata import Library, read_data
from exportdata import Submission, export_data




def compute(__):
    #MAIN LOOP
    pass




if __name__ == '__main__':
    for datafile in sys.argv[1:]:

        __ = read_data(datafile)

        submissions = compute(__)

        export_data(f"submission-{datafile}", submissions)
        print(f'-> exported to submission-{datafile}')

    print('done.')
