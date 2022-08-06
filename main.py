from time import sleep

import build

Tape = ["a","a","a"]

states: dict[(str, list[(str, str, str, str)])]
states = {}

start_state: str
start_state = "q1"

end_states: [str]
end_states = ["q3"]


def main():

    build.add_new_state("q1", states)
    build.add_new_transition("q1", "a", "á", "R", "q2", states)

    build.add_new_state("q2", states)
    build.add_new_transition("q2", "a", "a", "R", "q2", states)
    build.add_new_transition("q2", "_", "à", "L", "q3", states)
    build.add_new_transition("q2", "à", "à", "R", "q2", states)

    build.add_new_state("q3", states)
    build.add_new_transition("q3", "à", "à", "L", "q3", states)
    build.add_new_transition("q3", "a", "a", "L", "q4", states)

    build.add_new_state("q4", states)
    build.add_new_transition("q4", "a", "a", "L", "q4", states)
    build.add_new_transition("q4", "á", "á", "R", "q1", states)

    current_state = start_state
    position = 0

    while True:

        transitions: list[(str, str, str, str)]
        transitions = states[current_state]

        print(Tape)

        found_transition = False

        print(position)
        for x in transitions:
            if x[0] == Tape[position]:
                Tape[position] = x[1]
                if x[2] == "R":
                    position += 1
                    if position == len(Tape):
                        Tape.append("_")
                elif x[2] == "L":
                    position -= 1
                current_state = x[3]
                print("transition to " + x[3])
                found_transition = True
                break
        if found_transition is False:
            if current_state in end_states:
                print("Accepted")
                break
            else:
                print("Input discarded")
                break
        sleep(2)

if __name__ == "__main__":
    main()
