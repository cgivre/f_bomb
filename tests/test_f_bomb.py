import contextlib
import io
import unittest
from f_bomb import F_Bomb
from f_bomb.f_bomb import FUCK


class test_f_bomb(unittest.TestCase):
    def test_f_bomb(self):
        the_bomb = F_Bomb()
        self.assertEqual(str(the_bomb), "FUCK!")

    def test_language(self):
        the_bomb = F_Bomb()
        self.assertEqual(the_bomb.drop(), "FUCK!")
        self.assertEqual(the_bomb.drop("FR"), "PUTAIN!")
        self.assertEqual(the_bomb.drop("de"), "SCHEISSE!")

    def test_carpet_bomb(self):
        self.assertEqual(F_Bomb().carpet_bomb(3), "FUCK!\nFUCK!\nFUCK!")
        self.assertEqual(F_Bomb().carpet_bomb(2, "fr"), "PUTAIN!\nPUTAIN!")

    def test_defuse(self):
        self.assertEqual(F_Bomb().defuse(), "F**K!")
        self.assertEqual(F_Bomb().defuse("sv"), "F*N!")
        self.assertEqual(F_Bomb().defuse("he"), "ז*ן!")

    def test_dud(self):
        self.assertEqual(F_Bomb().dud(), "fudge.")

    def test_countdown(self):
        self.assertEqual(F_Bomb().countdown(), "3... 2... 1... FUCK!")
        self.assertEqual(F_Bomb().countdown(1, "it"), "1... CAZZO!")

    def test_grawlix(self):
        cuss = F_Bomb().grawlix(4)
        self.assertEqual(len(cuss), 5)
        self.assertTrue(cuss.endswith("!"))
        self.assertTrue(set(cuss[:-1]) <= set("#@$%&*"))

    def test_roulette(self):
        self.assertIn(F_Bomb().roulette(), [F_Bomb().drop(lang) for lang in FUCK])

    def test_cluster_bomb(self):
        lines = F_Bomb().cluster_bomb(5).split("\n")
        self.assertEqual(len(lines), 5)

    def test_nuke(self):
        self.assertEqual(len(F_Bomb().nuke().split("\n")), len(FUCK))

    def test_on_error(self):
        @F_Bomb.on_error
        def boom():
            raise ValueError("oops")

        @F_Bomb.on_error
        def fine():
            return 42

        self.assertEqual(fine(), 42)
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr), self.assertRaises(ValueError):
            boom()
        self.assertEqual(stderr.getvalue(), "FUCK!\n")


if __name__ == '__main__':
    unittest.main()
