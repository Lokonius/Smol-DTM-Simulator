import unittest
from source.TuringMachine import TuringMachine


class TMTestCase(unittest.TestCase):

    def setUp(self):

        self.tm = TuringMachine([], {})

    def test_init(self):

        self.assertEqual(self.tm.tape, [])
        self.assertEqual(self.tm.states, {})

    def test_add_new_state(self):

        self.tm.add_new_state("q1", {})

        self.assertEqual(self.tm.states, {"q1": {}})
        self.assertRaises(TypeError, self.tm.add_new_state, name=None, transitions={})
        self.assertRaises(TypeError, self.tm.add_new_state, name="q1", transitions=None)

    def test_add_new_transition(self):

        self.tm.add_new_transition("q1", "a", "b", "R", "q2")

        self.assertTrue("q1" in self.tm.states.keys())
        self.assertTrue("q2" in self.tm.states.keys())
        self.assertTrue("a" in self.tm.states["q1"].keys())
        self.assertEqual(self.tm.states["q1"]["a"][0], "b")
        self.assertEqual(self.tm.states["q1"]["a"][1], "R")
        self.assertEqual(self.tm.states["q1"]["a"][2], "q2")

    def test_add_new_transition_values(self):

        self.assertRaises(TypeError, self.tm.add_new_transition, state=None, read="a", write="b", direction="R",
                          next_state="q2")
        self.assertRaises(TypeError, self.tm.add_new_transition, state="q1", read=None, write="b", direction="R",
                          next_state="q2")
        self.assertRaises(TypeError, self.tm.add_new_transition, state="q1", read="a", write=None, direction="R",
                          next_state="q2")
        self.assertRaises(TypeError, self.tm.add_new_transition, state="q1", read="a", write="b", direction=None,
                          next_state="q2")
        self.assertRaises(TypeError, self.tm.add_new_transition, state="q1", read="a", write="b", direction="R",
                          next_state=None)
        self.assertRaises(ValueError, self.tm.add_new_transition, state="q1", read="ab", write="b", direction="R",
                          next_state="q2")
        self.assertRaises(ValueError, self.tm.add_new_transition, state="q1", read="a", write="asdb", direction="R",
                          next_state="q2")

    def test_overwrite_transition(self):

        self.tm.add_new_transition("q1", "a", "b", "R", "q2")
        self.tm.add_new_transition("q1", "a", "c", "L", "q3")

        self.assertTrue("q1" in self.tm.states.keys())
        self.assertTrue("q3" in self.tm.states.keys())
        self.assertTrue("a" in self.tm.states["q1"].keys())
        self.assertEqual(self.tm.states["q1"]["a"][0], "c")
        self.assertEqual(self.tm.states["q1"]["a"][1], "L")
        self.assertEqual(self.tm.states["q1"]["a"][2], "q3")

    def test_set_tape(self):

        self.tm.set_tape("quark")
        self.assertEqual(self.tm.tape, ["q","u","a","r","k"])

    def test_set_tape_values(self):

        self.assertRaises(TypeError, self.tm.set_tape, new_tape=None)


if __name__ == "__main__":
    unittest.main()

