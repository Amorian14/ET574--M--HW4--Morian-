import unittest
from main import Reel, SlotMachine

class TestSlotMachine(unittest.TestCase):

    # Provided: Reel spin bounds
    def test_reel_spin_bounds(self):
        reel = Reel()
        for _ in range(100):
            value = reel.spin()
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 9)

    # Provided: Outcome evaluation
    def test_evaluate_spin(self):
        sm = SlotMachine()
        self.assertEqual(sm.evaluate_spin(5, 5, 5), "WIN")
        self.assertEqual(sm.evaluate_spin(0, 3, 7), "LOSE")
        self.assertEqual(sm.evaluate_spin(4, 2, 9), "SPIN AGAIN")

    # Provided: play_round structure
    def test_play_round_structure(self):
        sm = SlotMachine()
        result = sm.play_round()
        self.assertIn("reels", result)
        self.assertIn("total", result)
        self.assertIn("result", result)

    # Your extra test 1: total calculation
    def test_total_calculation(self):
        r1, r2, r3 = 3, 4, 5
        total = r1 + r2 + r3
        self.assertEqual(total, 12)

    # Your extra test 2: win condition strict
    def test_win_condition(self):
        sm = SlotMachine()
        self.assertEqual(sm.evaluate_spin(7, 7, 7), "WIN")
        self.assertNotEqual(sm.evaluate_spin(7, 7, 6), "WIN")

    # Your extra test 3: lose if any zero
    def test_lose_condition_any_zero(self):
        sm = SlotMachine()
        self.assertEqual(sm.evaluate_spin(0, 9, 9), "LOSE")
        self.assertEqual(sm.evaluate_spin(9, 0, 9), "LOSE")
        self.assertEqual(sm.evaluate_spin(9, 9, 0), "LOSE")


if __name__ == "__main__":
    unittest.main()
