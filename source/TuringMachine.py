class TuringMachine:

    # List of Chars
    tape: list[str]
    tape = []

    # dict[state, dict[read, (write, direction, next_state)]]
    states: dict[str, dict[str, (str, str, str)]]
    states: {}

    # start_state
    start_state: str
    start_state = ""

    # end_states
    end_states: [str]
    end_states = []

    def __init__(self, tape, states):

        self.tape = tape
        self.states = states

    def add_new_state(self, name: str, transitions: dict[str, (str, str, str)]):

        """
        adds a new state, with given transitions
        :param name: name of the state
        :param transitions: transitions of the new state
        :return:
        """

        if name is None:
            raise TypeError("name must not be None")

        self.states[name] = transitions
        return True

    def add_new_transition(self, state: str, read: str, write: str, direction: str, next_state: str):

        """
        adds a new transition the machine and add new states, if the states in the transition aren't already present
        :param state: start state
        :param read: char read form the tape
        :param write: char to write on the tape
        :param direction: direction to move the position
        :param next_state: state of after the transition
        :return:
        """

        if state is None:
            raise TypeError("state must not be None")

        if read is None:
            raise TypeError("read must not be None")

        if len(read) > 1:
            raise ValueError("read must be a single char")

        if write is None:
            raise TypeError("write must not be None")

        if len(write) > 1:
            raise ValueError("write must be a single char")

        if direction is None:
            raise TypeError("direction must not be None")

        if direction not in "LRN":
            raise ValueError("direction must be either of L, R, N")

        if next_state is None:
            raise TypeError("next_state must not be None")

        # adds the next_state to self.states if it does not exist
        if next_state not in self.states:

            self.states[next_state] = {}

        # if state in not in self.states a new state with the new transition ist created
        if state not in self.states:

            self.add_new_state(state, {read: (write, direction, next_state)})
            return True

        # if the state is in self.states add the new transition
        elif state in self.states:

            self.states[state][read] = (write, direction, next_state)
            return True

    def set_tape(self, new_tape: str):

        """
        takes a string and makes a list of characters out of it
        :param new_tape: the new content of the tape
        :return:
        """

        if new_tape is None:
            raise TypeError("new_tape must not be None")

        self.tape = []

        for x in new_tape:

            self.tape.append(x)

        return True
