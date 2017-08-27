from rogers.blockchain.bithumb import ParserBithumb
from rogers.blockchain.coinone import ParserCoinone
from rogers.blockchain.korbit import ParserKorbit
from rogers.model.database import Database
from utils.slack import send_message


def main():
    parser_class = {
        "bithumb": ParserBithumb,
        "coinone": ParserCoinone,
        "korbit": ParserKorbit
    }

    db = Database()
    for Parser in parser_class.values():
        parser = Parser()

        for currency in parser.currency:
            params = {"currency": currency}
            response = parser.get_response(params)
            model = parser.parse(response, currency)
            db.insert(model)

    send_message("#data-monitoring", "Save data finished!")

if __name__ == '__main__':
    main()
