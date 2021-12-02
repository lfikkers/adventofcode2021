class Submarine:
    def __init__(self, name: str = "yellow"):
        self.pos_x = 0
        self.pos_y = 0
        self.name = name
    
    def forward(self, x: int = 0) -> None:
        if x < 0:
            print(f'The value of x should be negative, but it is {x}.')
        elif x == 0:
            print(f'The value of x is 0, no steps are made.')
        else:
            prev_pos_x = self.pos_x
            self.pos_x += x

            print (f'Moved {x} steps forward, from {prev_pos_x} to {self.pos_x}.')
    
    def down(self, x: int = 0) -> None:
        if x < 0:
            print(f'The value of x should be negative, but it is {x}.')
            print('Use up() instead.')
        elif x == 0:
            print('The value of x is 0, no steps are made.')
        else:
            prev_pos_y = self.pos_y
            self.pos_y += x

            print (f'Moved {x} steps down, from {prev_pos_y} to {self.pos_y}.')
    
    def up(self, x: int = 0) -> None:
        if x < 0:
            print(f'The value of x should be negative, but it is {x}.')
            print('Use down() instead.')
        elif x == 0:
            print('The value of x is 0, no steps are made.')
        else:
            prev_pos_y = self.pos_y
            self.pos_y -= x

            print (f'Moved {x} steps up, from {prev_pos_y} to {self.pos_y}.')
    
    def print_position(self) -> None:
        print(f'The position of the {self.name} submarine is:')
        print(f'X = {self.pos_x}, depth = {self.pos_y}.')

    def calculate_answer(self) -> None:
        answer = self.pos_x * self.pos_y
        print(f'The answer is {answer}.')


sub = Submarine()

with open(f'.\\code\\2dec\\input.txt') as file:
    contents = file.readlines()

for line in contents:
    command, step = line.split(" ")
    step = int(step)
    if command == "down":
        sub.down(step)
    elif command == "up":
        sub.up(step)
    elif command == "forward":
        sub.forward(step)
    else:
        print (f'command not understoond: {command}, {step}.')
    
sub.print_position()
sub.calculate_answer()