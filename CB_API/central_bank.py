import requests
import re
from helper.Helper import Check
from bs4 import BeautifulSoup


class CbApi:
    def get_xml(self, date=''):
        request = 'https://www.cbr.ru/scripts/XML_daily.asp'
        if date != '':
            find_numbers = re.findall(r'[0-9]+', date)
            d = find_numbers[0]
            m = find_numbers[1]
            y = find_numbers[2]
            if Check.check_values(d, 1, 31) and Check.check_values(m, 1, 12) and Check.check_values(y, 2000, 2022):
                request += f'?date_req={d}/{m}/{y}'
            else:
                return 0
        try:
            resp = requests.get(request)
            return BeautifulSoup(resp.content, 'xml')
        except:
            print('Ошибка. Проверьте дату')

    def get_course_usd(self, date=''):
        soup = self.get_xml(date=date)
        return float(soup.find(ID="R01235").Value.string.replace(',', '.'))

    def get_course_euro(self, date=''):
        soup = self.get_xml(date=date)
        return float(soup.find(ID="R01239").Value.string.replace(',', '.'))

    def get_course(self, char_code: str, date='') -> float:
        """support AUD, AZN, GBP, AMD, BYN, BGN, BRL, HUF, HKD, DKK, USD, EUR, INR, KZT, CAD, KGS, CNY, MDL, NOK,
        PLN, RON, XDR, SGD, TJS, TRY, TMT, UZS, UAH, CZK, SEK, CHF, ZAR, KRW, JPY"""
        soup = self.get_xml(date=date)
        char_code = char_code.upper()
        try:
            nominal = int(soup.find('CharCode', text=char_code).find_next_sibling('Nominal').string)
            value = soup.find('CharCode', text=char_code).find_next_sibling('Value').string
            value = value.replace(',', '.')
            return float(value) / nominal
        except:
            if char_code == 'RUB':
                return 1
            else:
                print('Ошибка.Проверьте код валюты')

    def convert(self, amount, cur_from, cur_to, date=''):
        try:
            cur_to = cur_to.upper()
            cur_from = cur_from.upper()
            cur_1 = self.get_course(cur_from, date)
            cur_2 = self.get_course(cur_to, date)
            return (amount*cur_1)/cur_2
        except:
            print('Ошибка.Проверьте код валюты')


