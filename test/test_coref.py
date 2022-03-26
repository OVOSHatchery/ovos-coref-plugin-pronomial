import unittest

from ovos_coref_plugin_pronomial import PronomialCoreferenceSolver


class TestPronomial(unittest.TestCase):

    def test_coref(self):
        solver = PronomialCoreferenceSolver()
        self.assertEqual(solver.solve_corefs(
            "My neighbors have a cat. It has a bushy tail"),
            "My neighbors have a cat. cat has a bushy tail")
        self.assertEqual(solver.solve_corefs(
            "Here is the book now take it"),
            "Here is the book now take book")
        self.assertEqual(solver.solve_corefs(
            "The sign was too far away for the boy to read it"),
            "The sign was too far away for the boy to read sign")
        self.assertEqual(solver.solve_corefs(
            "Dog is man's best friend. It is always loyal"),
            "Dog is man's best friend. Dog is always loyal")
        self.assertEqual(solver.solve_corefs(
            "The girl said she would take the trash out"),
            "The girl said girl would take the trash out")
        self.assertEqual(solver.solve_corefs(
            "I voted for Bob because he is clear about his values. His ideas represent a majority of the nation. He is better than Alice"),
            "I voted for Bob because Bob is clear about Bob values. Bob ideas represent a majority of the nation. Bob is better than Alice")
        self.assertEqual(solver.solve_corefs(
            "Jack von Doom is one of the top candidates in the elections. His ideas are unique compared to Bob's"),
            "Jack von Doom is one of the top candidates in the elections. Doom ideas are unique compared to Bob's")
        self.assertEqual(solver.solve_corefs(
            "Members voted for John because they see him as a good leader"),
            "Members voted for John because Members see John as a good leader")
        self.assertEqual(solver.solve_corefs(
            "Leaders around the world say they stand for peace"),
            "Leaders around the world say Leaders stand for peace")
        self.assertEqual(solver.solve_corefs(
            "My neighbours just adopted a puppy. They care for it like a baby"),
            "My neighbours just adopted a puppy. neighbours care for puppy like a baby")
        self.assertEqual(solver.solve_corefs(
            "I have many friends. They are an important part of my life"),
            "I have many friends. friends are an important part of my life")

