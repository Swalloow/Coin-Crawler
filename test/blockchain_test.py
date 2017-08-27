from rogers.blockchain.bithumb import ParserBithumb
from rogers.blockchain.coinone import ParserCoinone
from rogers.blockchain.korbit import ParserKorbit


def test_bithumb():
    parser = ParserBithumb()
    params = {"currency": parser.currency[0]}
    response = parser.get_response(params)
    assert response.status_code == 200


def test_coinone():
    parser = ParserCoinone()
    params = {"currency": parser.currency[0]}
    response = parser.get_response(params)
    assert response.status_code == 200


def test_korbit():
    parser = ParserKorbit()
    params = {"currecy_pair": parser.currency[0]}
    response = parser.get_response(params)
    assert response.status_code == 200
