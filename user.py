class User:
    def __init__(self):
        self.name = None
        self.confirm = False
        self.movie = None
        self.visitDate = None
        self.visitTime = None
        self.payMethod = None


    def set_name(self,name):
        self.name = name
    def target_movie(self,movie):
        self.movie = movie
    def visit_at(self,date):
        self.visitDate = date
    def visit_time(self,time):
        self.visitTime = time
    def pay_by(self,method):
        self.payMethod = method
    def reset_all_booking_details(self):
        self.confirm = False
        self.movie = None
        self.visitDate = None
        self.visitTime = None
        self.payMethod = None        
    def reset_visitDate(self):
        self.visitDate = None
    def reset_visitTime(self):
        self.visitTime = None