def add_new_state(name: str, states: dict):

    states[name] = [None]

    return states


def add_new_transition(state: str, read: str, write: str, direction: str, next_state: str,
                       states: dict[(str, list[(str, str, str, str)])]):

    transitions: list[(str, str, str, str)]

    if states[state][0] is None:
        states[state] = [(read, write, direction, next_state)]

    else:
        transitions = states[state]
        transitions.append((read, write, direction, next_state))

    return states
