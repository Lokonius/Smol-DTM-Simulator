from TuringMachine import TuringMachine
from Simulator import Simulator


def main():

    tm = TuringMachine([], {})

    tm.add_new_transition("q1", "a", "b", "R", "q1")
    tm.add_new_transition("q1", "b", "a", "R", "q2")

    tm.start_state = "q1"
    tm.end_states = ["q2"]

    tm.set_tape("aaaab")

    sim = Simulator(tm)

    sim.check()


if __name__ == "__main__":
    main()
