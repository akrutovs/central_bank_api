from CB_API.central_bank import CbApi

c = CbApi()
usd = c.get_course_usd('17.09.2022')
print(usd)
eur = c.get_course('EUR')
print(eur)