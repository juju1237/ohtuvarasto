import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_konstruktori_nollaa_nollan_tilavuuden(self):
        varasto = Varasto(0)

        self.assertEqual(varasto.tilavuus, 0)
        self.assertEqual(varasto.saldo, 0)

    def test_konstruktori_nollaa_negatiivisen_alkusaldon(self):
        varasto = Varasto(10, -1)

        self.assertEqual(varasto.saldo, 0)

    def test_konstruktori_rajoittaa_alkusaldon_tilavuuteen(self):
        varasto = Varasto(10, 12)

        self.assertEqual(varasto.saldo, 10)

    def test_lisays_ohittaa_negatiivisen_maaran(self):
        self.varasto.lisaa_varastoon(-1)

        self.assertEqual(self.varasto.saldo, 0)

    def test_lisays_tayttaa_varaston_yli_menevalla_maaralla(self):
        self.varasto.lisaa_varastoon(11)

        self.assertEqual(self.varasto.saldo, 10)

    def test_ottaminen_ohittaa_negatiivisen_maaran(self):
        self.varasto.lisaa_varastoon(5)

        saatu_maara = self.varasto.ota_varastosta(-1)

        self.assertEqual(saatu_maara, 0)
        self.assertEqual(self.varasto.saldo, 5)

    def test_ottaminen_palauttaa_koko_saldon_jos_pyynto_yli_saldon(self):
        self.varasto.lisaa_varastoon(5)

        saatu_maara = self.varasto.ota_varastosta(6)

        self.assertEqual(saatu_maara, 5)
        self.assertEqual(self.varasto.saldo, 0)

    def test_merkkijonoesityksessa_naytetaan_saldo_ja_vapaa_tila(self):
        self.varasto.lisaa_varastoon(4)

        self.assertEqual(str(self.varasto), "saldo = 4, vielä tilaa 6")
