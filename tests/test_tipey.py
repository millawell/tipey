import unittest
from tipey.unit.temperature import Celsius, Fahrenheit
from tipey.unit.currency import (
    MYR,
    JPY,
    DKK,
    BRL,
    KRW,
    MXN,
    CAD,
    AUD,
    HRK,
    HKD,
    ISK,
    NZD,
    USD,
)

from tipey.unit.mass import Kilogram, Gram, Oz

from tipey.quantity import Temperature, Currency, Mass, I


class TestTipeyMethods(unittest.TestCase):

    def test_abstract_quantity(self):

        v1 = I(100) @ Gram

        self.assertEqual(
            v1.unit.d(), 'gram'
        )

    def test_temperature(self):

        v1 = Temperature(10, Celsius)

        v2 = v1 @ Fahrenheit @ Celsius @ Fahrenheit

        self.assertEqual(v2, 50)

    def test_currency(self):

        v1 = Currency(10, USD)
        v2 = (
            v1
            @ MYR
            @ JPY
            @ DKK
            @ BRL
            @ KRW
            @ MXN
            @ CAD
            @ AUD
            @ HRK
            @ HKD
            @ ISK
            @ NZD
            @ USD
        )

        self.assertAlmostEqual(v1.value, v2.value)

    def test_mass(self):

        v1 = Mass(1000, Gram)
        v2 = v1 @ Kilogram

        self.assertEqual(v2, 1)

        v1 = Mass(28.349523124999998, Gram)
        v2 = v1 @ Oz

        self.assertEqual(v2, 1)

    def test_arithmetic(self):

        v = I(1000) @ Gram + I(1) @ Kilogram

        self.assertEqual(
            v, 2000
        )

    def test_arithmetic(self):

        v1 = I(1001) @ Gram 
        v2 = I(1) @ Kilogram

        self.assertTrue(
            v1 > v2
        )

    def test_str(self):

        v1 = I(1000) @ Gram

        self.assertTrue(
            str(v1),
            '1000 Gram'
        )


if __name__ == "__main__":
    unittest.main()
