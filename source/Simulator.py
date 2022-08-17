import TuringMachine
from time import sleep


class Simulator:

    machine: TuringMachine
    machine = None

    def __init__(self, machine: TuringMachine):

        if machine is None:
            raise TypeError("machine must not be None")

        self.machine = machine

    def check(self):

        current_state = self.machine.start_state
        position = 0

        while True:

            if len(self.machine.tape) == position:
                self.machine.tape.append("_")

            print(current_state)
            print(position)
            print(self.machine.tape)
            print()

            sleep(1)

            if current_state in self.machine.end_states:
                break

            if current_state not in self.machine.states:
                print(f"state {current_state} does not exist")
                return False

            if self.machine.tape[position] not in self.machine.states[current_state]:
                print(f"no transition for {self.machine.tape[position]}")
                return

            write, move, next_state = self.machine.states[current_state][self.machine.tape[position]]

            self.machine.tape[position] = write

            if move == "R":
                position += 1

            elif move == "L":
                position -= 1

            current_state = next_state





