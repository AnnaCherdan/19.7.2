from api import CryptocompareAn
from settings import valid_fsym_1, valid_tsym_1, valid_tsym_2, valid_fsym_3, valid_tsym_3

cra = CryptocompareAn()


def test_get_price(fsym=valid_fsym_1, tsym=valid_tsym_1):
    status, result = cra.get_price(fsym, tsym)
    assert status == 200
    assert 'USD' in result


def test_get_invalid_currency(fsym=valid_fsym_1, tsym=valid_tsym_2):
    status, result = cra.get_invalid_currency(fsym, tsym)
    assert status == 200
    assert 'Cooldown' in result


def test_multiple_symbols_price(fsym=valid_fsym_3, tsym=valid_tsym_1):
    status, result = cra.get_multiple_symbols_price(fsym, tsym)
    assert status == 200
    assert 'USD' in result


# def test_get_invalid_price(fsym=valid_fsym_1, tsym=valid_tsym_2):
#     status, result = cra.get_price(fsym, tsym)
#     assert status == 200
#     assert 'Cooldown' in result

