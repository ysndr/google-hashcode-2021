#%%
from importdata import Library

class Submission():
    def __init__(self, lid, books):
        pass



def export_data(file, submissions, book_scores):
    with open(file, 'w+') as handle:
        handle.write(f"{len(submissions)}\n")
