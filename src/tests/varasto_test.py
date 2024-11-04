import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
      #  self.varasto = Varasto(10)
        self.taysi_varasto = Varasto(0)
        self.negatiivinen_alkusaldo = Varasto(10,-3)
        self.varasto2 = Varasto(10,13)

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

    def test_negatiivisen_lisaaminen_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(-3)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_lisays_tayttaa_varaston(self):
        self.varasto.lisaa_varastoon(10)

        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_ota_negatiivinen_antaa_nollan(self):
        nosto = self.varasto.ota_varastosta(-4)

        self.assertAlmostEqual(nosto, 0.0)

    def test_ota_yli_saldon_asettaa_saldon_nollaksi(self):
        self.varasto.lisaa_varastoon(2)

        nosto = self.varasto.ota_varastosta(3)
        self.assertAlmostEqual(self.varasto.saldo, 0.0)


    def test_ota_yli_saldon_anna_kaikki_mita_voi(self):
        self.varasto.lisaa_varastoon(2)

        nosto = self.varasto.ota_varastosta(3)
        self.assertAlmostEqual(nosto, 2)

    def test_merkkijono_toimii(self):
        self.varasto.lisaa_varastoon(4)

        tulos = str(self.varasto)

        self.assertAlmostEqual(tulos, "saldo = 4, vielä tilaa 6")

    def test_lisays_yli_tilavuuden_muuttaa_saldon_tayteen(self):
        self.varasto.lisaa_varastoon(11)

        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_konstruktori_luo_tayden_varaston(self):
        self.assertAlmostEqual(self.taysi_varasto.tilavuus, 0)

    def test_negatiivinen_alkusaldo_nollaksi(self):
        self.assertAlmostEqual(self.negatiivinen_alkusaldo.saldo, 0.0)

    def test_liian_suuri_alkusaldo_tayttaa_varaston(self):
        self.assertAlmostEqual(self.varasto2.saldo, self.varasto2.tilavuus)
