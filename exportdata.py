#%%
from importdata import Library

class Submission():
    def __init__(self, lid, books):
        self.lid = lid
        self.books = books


    @classmethod
    def from_library(cls, library: Library):
        return Submission(library.lid, list(library.books))

    def get_nbooks(self):
        return len(self.books)

    def get_bids(self, book_scores):
        return sorted(self.books, key=lambda bid: -book_scores[bid])


def export_data(file, submissions, book_scores):
    with open(file, 'w+') as handle:
        handle.write(f"{len(submissions)}\n")
        for submission in submissions:
            if submission.get_nbooks == 0: continue
            handle.write(f"{submission.lid} {submission.get_nbooks()}\n")
            handle.write(f"{' '.join([str(book) for book in submission.get_bids(book_scores)])}\n")
