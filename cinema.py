class Start_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)

class Hall:
    def __init__(self, rows, cols, hall_no):
        self.str_cinema = Start_Cinema()
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

        self.str_cinema.entry_hall(self)

    def entry_show(self, show_id, movie_name, time):
        newShow = (show_id, movie_name, time)
        self.show_list.append(newShow)

        self.seats[show_id] = []
        for r in range (self.rows):
            row = [0] * self.cols
            self.seats[show_id].append(row)

    def view_show_list(self):
        print(' ')
        for show in self.show_list:
            print(f'\t->Show name: {show[1]}, Show id: {show[0]}, Show time: {show[2]}')
        print(' ')

    def book_seat(self, show_id, row, col):
        show_exists = False
        for show in self.show_list:
            if show[0] == show_id:
                show_exists = True
        
        if show_exists:
            if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
                print(f"\n\t->Seat ({row}, {col}) is invalid.\n")
                return False
            
            if self.seats[show_id][row][col] == 1:
                print(f'\n\t->Seat ({row},{col}) is already booked\n')
                return False
            
            else:
                self.seats[show_id][row][col] = 1
                print(f'\n\t->Seat ({row},{col}) booked!\n')
                return True
        
        else:
            print('\n\t->No such show\n')

    def view_available_seats(self,show_id):
        print('Available Seats: ')
        for row in range (self.rows):
            for col in range (self.cols):
                if self.seats[show_id][row][col] == 0:
                    print(f'Seat ({row},{col})')
        
        print(' ')
    

hall1 = Hall(5, 10, 1)
hall1.entry_show(1, 'Jawan', '2.00AM')
hall1.entry_show(2, 'Pathan', '2.00AM')

while True:
    print('[1] View all Show')
    print('[2] Book ticket')
    print('[3] View available seats')
    print('[4] Exit')

    op = int(input('\nEnter your choice: '))

    if op == 1:
        hall1.view_show_list()
        
    if op == 2:
        show_id = int(input('\nEnter show id: '))
        n = int(input('Number of ticket?'))
        for i in range (0,n):
            row = int(input('Row: '))
            col = int(input('Col: '))
            res = hall1.book_seat(show_id, row, col)
            
    if op == 3:
        show_id = int(input('Enter show id: '))
        hall1.view_available_seats(show_id)
    if op == 4:
        break






    