import sys

from importdata import Library, read_data
from exportdata import Submission, export_data




def compute(libraries, book_lookup, book_scores, days):
    #MAIN LOOP
    libs_sorted = sorted(libraries, key=lambda l: l.score)

    output = []

    count = len(libs_sorted)


    while count:
        best = libs_sorted.pop()
        output.append(best)

        days -= best.signup

        changed_libs = set()
        for b in best.books:
            libs = book_lookup[b]
            changed_libs |= libs
            for lid in libs:
                if lid == best.lid: continue
                libraries[lid].delete_book(b)




        for lib in libs_sorted:
            lib.update_score(days)

        libs_sorted = sorted(libs_sorted, key=lambda l: l.score)

        count -= 1





    submissions = [Submission.from_library(lib) for lib in output if lib.n_books]



    return submissions


def resort(lib, libs_sorted):
    i = libs_sorted.index(lib)
    old = i
    while libs_sorted[i].score > lib.score:
        i -= 1
    del(libs_sorted[old])
    libs_sorted.insert(i, lib)


if __name__ == '__main__':
    for datafile in sys.argv[1:]:

        book_scores, book_lookup, libraries, days = read_data(datafile)

        submissions = compute(libraries, book_lookup, book_scores, days)

        export_data(f"submission-{datafile}", submissions, book_scores)
        print(f'-> exported to submission-{datafile}')

    print('done.')
