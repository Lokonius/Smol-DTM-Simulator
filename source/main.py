from turing_machine import TuringMachine
from simulator import Simulator


def main():

    # code for a test machine, which accepts every word which starts with a number of 'a's and ends with a 'b'

    tm = TuringMachine([], {})

    tm.add_new_transition("q1", "a", "a", "R", "q1")
    tm.add_new_transition("q1", "b", "b", "R", "q2")
    tm.add_new_transition("q2", "_", "_", "N", "q3")

    tm.start_state = "q1"
    tm.end_states = ["q3"]

    tm.set_tape("aaaab")

    sim = Simulator(tm)

    sim.check()


if __name__ == "__main__":
    main()
