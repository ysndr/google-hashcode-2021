
#%%
class Library():
    def __init__(self, lid, n_books, books, signup, booksperday, book_scores, days):
        self.lid = lid
        self.n_books = int(n_books)
        self.books = books
        self.signup = int(signup)
        self.booksperday = int(booksperday)
        self.book_scores = book_scores
        self.book_score = sum(
            [book_scores[bid] for bid in self.books[:(days * self.booksperday)]])

    def delete_books(self, bids):
        self.books.remove(bids)
        self.book_score -= sum(self.book_scores[bid] for bid in bids if bid in self.books)

    def delete_book(self, bid):

        self.books.remove(bid)
        self.book_score -= self.book_scores[bid]
        self.n_books -= 1

    def update_score(self, days):
        self.book_score = sum(
            [self.book_scores[bid]
            for bid in self.books[:(days * self.booksperday)]])

    @property
    def score(self):
        return 1/(1+self.signup) * self.book_score


    def __hash__(self):
        return hash(self.lid)

#%%
def read_data(file):
    with open(file, 'r') as handle:
        lines = handle.readlines()

        return ()

#%%
