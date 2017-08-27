class Config:
    APP_NAME = 'rogers'
    DATABASE_URI = 'mysql+pymysql://USER:PROJECT@IP_ADDRESS:PORT/DB_NAME'
    SLACK_TOKEN = 'Add slack token'


class Source:
    BITHUMB_URI = 'https://api.bithumb.com/public/ticker/'
    COINONE_URI = 'https://api.coinone.co.kr/ticker/'
    KORBIT_URI = 'https://api.korbit.co.kr/v1/ticker/detailed'
