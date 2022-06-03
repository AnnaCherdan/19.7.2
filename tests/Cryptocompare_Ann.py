from api import CryptocompareAn
from settings import valid_fsym_1, valid_tsym_1, valid_tsym_2, valid_fsym_3, valid_tsym_3, valid_exchange

cra = CryptocompareAn()


class TestCrypAn:
    def setup(self):
        self.cra = CryptocompareAn

    def test_get_price(self, fsym=valid_fsym_1, tsym=valid_tsym_1):
        status, result = cra.get_price(fsym, tsym)
        assert status == 200
        assert 'USD' in result

    def test_get_invalid_currency(self, fsym=valid_fsym_1, tsym=valid_tsym_2):
        status, result = cra.get_invalid_currency(fsym, tsym)
        assert status == 200
        assert 'Cooldown' in result

    def test_multiple_symbols_price(self, fsym=valid_fsym_3, tsym=valid_tsym_3):
        status, result = cra.get_multiple_symbols_price(fsym, tsym)
        assert status == 200
        assert 'BTC' in result
        assert 'ETH' in result

    def test_multiple_symbols_full_data(self, fsym=valid_fsym_1, tsym=valid_tsym_3):
        status, result = cra.get_multiple_symbols_full_data(fsym, tsym)
        assert status == 200
        assert 'RAW' in result

    def test_generate_custom_average(self, fsym=valid_fsym_1, tsym=valid_tsym_1, e=valid_exchange):
        status, result = cra.get_generate_custom_average(fsym, tsym, e)
        assert status == 200
        assert 'RAW' in result

    def test_mapping_from_symbol(self, fsym=valid_fsym_1):
        status, result = cra.get_mapping_from_symbol(fsym)
        assert status == 200
        assert 'RAW' in result






