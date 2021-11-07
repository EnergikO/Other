from urllib.request import urlopen
from translate import translate


def get_data_from_url(url: str) -> str:
	data = urlopen(url).read().decode('ASCII')
	return translate(data)


def fact_about_number(randomly: bool=False) -> str:
	if randomly:
		from random import randint, choice
		number = randint(0, 9999)
		type_of_fact = choice(['trivia', 'math'])

	else:
		number = int(input('Input number='))
		type_of_fact = input('Input type of fact\n(it may be only "trivia" or "math")')

	if type_of_fact == '' or (type_of_fact != 'trivia' and type_of_fact != 'math'):
		type_of_fact = 'trivia'

	return get_data_from_url(f'http://numbersapi.com/{number}/{type_of_fact}')


def fact_about_date(randomly: bool=False) -> str:
	if randomly:
		from random import randint
		day = randint(1, 31)
		month = randint(1, 12)

	else:
		day = int(input('Input day='))
		month = int(input('Input month='))

	return get_data_from_url(f'http://numbersapi.com/{month}/{day}/date')


def fact_about_year(randomly: bool=False) -> str:
	if randomly:
		from random import randint
		year = randint(0, 9999)

	else:
		year = int(input('Input year='))

	return get_data_from_url(f'http://numbersapi.com/{year}/year')


def main():
	print(fact_about_number(True))
	print(fact_about_date(True))
	print(fact_about_year(True))


if __name__ == '__main__':
	main()
