import requests
import re


class CbApi:
    def get_course_usd(self, date=''):
        request = 'https://www.cbr.ru/scripts/XML_daily.asp'
        if date != '':
            find_numbers = re.findall(r'[0-9]+', date)
            request += '?date_req=' + find_numbers[0] + '/' + find_numbers[1] + '/' + find_numbers[2]
        resp = requests.get(request)
        print(resp.content)
