from turing_machine import TuringMachine
from time import sleep


class Simulator:

    """
    a class for simulating a TuringMachine

    """
    machine: TuringMachine  # the machine which is going to be simulated
    machine = None

    def __init__(self, machine: TuringMachine):

        if machine is None:
            raise TypeError("machine must not be None")

        self.machine = machine

    def check(self, input_tape=None):

        """
        checks whether the machine accepts the given input or not
        :param input_tape: new input_tape for the machine
        if not None, changes the tape to the new value, else it just works with the current tape of the machine
        :return:
        """

        if input_tape is not None:
            self.machine.set_tape(input_tape)

        current_state = self.machine.start_state
        position = 0

        while True:

            # add new space at the end of the tape to ensure the position doesn't move out of range
            if len(self.machine.tape) == position:
                self.machine.tape.append("_")

            # some prints to follow what the machine ist doing
            print(current_state)
            print(position)
            print(self.machine.tape)
            print()

            sleep(1)

            # break if end state reached
            if current_state in self.machine.end_states:
                break

            # abort if the state does not exist
            if current_state not in self.machine.states:
                print(f"state {current_state} does not exist")
                return False

            # abort if no transition for the current char exists
            if self.machine.tape[position] not in self.machine.states[current_state]:
                print(f"no transition for {self.machine.tape[position]}")
                return False

            write, move, next_state = self.machine.states[current_state][self.machine.tape[position]]

            # write the new char on the tape
            self.machine.tape[position] = write

            # move position according to instructions
            if move == "R":
                position += 1

            elif move == "L":
                position -= 1

            # swap to next state
            current_state = next_state

        return True





