import requests
import re
from halper.Halper import Check


class CbApi:
    def get_course_usd(self, date=''):
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
            print(resp.content)
        except:
            print('Ошибка. Проверьте дату')
