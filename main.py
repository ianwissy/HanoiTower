import time

class Hanoi:

    def __init__(self, number_of_discs):
        self.discs = number_of_discs
        self.stack_1 = list(range(self.discs))
        self.stack_2 = []
        self.stack_3 = []
        self.stack_array = [self.stack_1, self.stack_2, self.stack_3]
        self.solve()

    def move_disc(self, start_stack, end_stack):
        end_stack[:0] = [start_stack[0]]
        start_stack[0:1] = []

    def move_choice(self, parity):
        top_dict = {}
        for n in range(3):
            try:
                top_dict[self.stack_array[n][0]] = n
            except IndexError:
                top_dict[self.discs] = None
        if parity == 1:
            del top_dict[max(top_dict)]
            disc_to_move = max(top_dict)
        else:
            disc_to_move = min(top_dict)
        if (self.discs - disc_to_move) % 2 == 1:
            self.move_disc(self.stack_array[top_dict[disc_to_move]], self.stack_array[(top_dict[disc_to_move] + 2) % 3])
        else:
            self.move_disc(self.stack_array[top_dict[disc_to_move]], self.stack_array[(top_dict[disc_to_move] + 1) % 3])
        #print(self.stack_array) #Remove first # to print all of the steps (It is pretty neat!)

    def solve(self):
        move_count = 0
        while self.stack_3 != list(range(self.discs)):
            self.move_choice(move_count % 2)
            move_count += 1
            #if move_count > 2 ** self.discs:
            #    break


class RecursiveHanoi:

    def __init__(self, number_of_discs):
        self.number_of_discs = number_of_discs
        self.disc_dict = {}
        self.disc_array = [[], [], []]
        for n in range(number_of_discs):
            self.disc_dict[n] = 0
            self.disc_array[0].append(n)
        self.recur(number_of_discs - 1)

    def recur(self, disc_number):
        if disc_number != 0:
            self.recur(disc_number - 1)
        self.disc_array[self.disc_dict[disc_number]][0:1] = []
        self.disc_dict[disc_number] = \
            (self.disc_dict[disc_number] + (-1) ** ((self.number_of_discs - disc_number) % 2)) % 3
        self.disc_array[self.disc_dict[disc_number]][:0] = [disc_number]
        #print(self.disc_array)   #Remove first # to print all of the steps (It is pretty neat!)
        if disc_number != 0:
            self.recur(disc_number - 1)


start = time.perf_counter()
H = Hanoi(10)
end = time.perf_counter()
print(end - start)

r_start = time.perf_counter()
HR = RecursiveHanoi(10)
r_end = time.perf_counter()
print(r_end - r_start)

