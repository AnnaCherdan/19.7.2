from api import CryptocompareAn
from settings import valid_fsym_1, valid_tsym_1, valid_tsym_2, valid_fsym_3, valid_tsym_3, valid_exchange
from settings import valid_exchangeFsym, valid_language

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
        assert 'RateLimit' in result

    def test_mapping_exchange(self, e=valid_exchange):
        status, result = cra.get_mapping_from_symbol(e)
        assert status == 200
        assert 'Data' in result

    def test_mapping_exchange_from_symbol(self, fsym=valid_exchangeFsym):
        status, result = cra.get_mapping_exchange_from_symbol(fsym)
        assert status == 200
        assert 'Data' in result

    def test_latest_news_articles(self, lang = valid_language):
        status, result = cra.get_latest_news_articles(lang)
        assert status == 200
        assert 'Data' in result

    def test_all_the_exchanges_and_trading_pairs(self):
        status, result = cra.get_all_the_exchanges_and_trading_pairs()
        assert status == 200
        assert 'Data' in result

    def test_rate_limit(self):
        status, result = cra.get_rate_limit()
        assert status == 200
        assert 'Data' in result


