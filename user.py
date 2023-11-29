class User:
    def __init__(self):
        self.name = None
        self.confirm = False
        self.movie = None
        self.visitDate = None
        self.visitTime = None
        self.payMethod = None
        self.pay = None

    def set_name(self,name):
        self.name = name
    def target_movie(self,movie):
        self.movie = movie
    def visit_at(self,date):
        self.visitDate = date
    def pay_by(self,method):
        self.payMethod = method
