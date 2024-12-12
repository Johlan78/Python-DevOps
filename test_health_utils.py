import unittest
from health_utils import calculate_bmi

class TestHealthUtils(unittest.TestCase):
    def test_calculate_bmi(self):
        # Test normal BMI calculation
        self.assertAlmostEqual(calculate_bmi(70, 1.75), 22.86, places=2)  # Poids en kg, Taille en m

        # Test edge case for zero height
        with self.assertRaises(ValueError):
            calculate_bmi(70, 0)  # Valeur incorrecte de hauteur (0)

        # Test extreme cases
        self.assertAlmostEqual(calculate_bmi(100, 1.80), 30.86, places=2)
        self.assertAlmostEqual(calculate_bmi(45, 1.50), 20.00, places=2)

if __name__ == "__main__":
    unittest.main()