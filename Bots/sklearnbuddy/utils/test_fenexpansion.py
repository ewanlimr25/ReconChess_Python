import unittest
import fenexpansion as fe

class TestFenexpansion(unittest.TestCase):

    def test_fenexpansion(self):
        fen = "r1b1kbnr/ppp1p1pp/n7/3P1P1Q/3PP3/1BN2P2/PP2N1PP/R1BQK2R"\
            " b KQkq - 0 5"
        expanded_board = fe.fenexpansion(fen)
        self.assertEqual(expanded_board, "r@b@kbnr/ppp@p@pp/n@@@@@@@/"\
            "@@@P@P@Q/@@@PP@@@/@BN@@P@@/PP@@N@PP/R@BQK@@R")

# __name__ is a special variable assigned by python to the 'main' file being
# run. __name__ is __main__ when the .py file is run directly as opposed to
# being imported by another file.
if __name__ == '__main__':
    unittest.main()

