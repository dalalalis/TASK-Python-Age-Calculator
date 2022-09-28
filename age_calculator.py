from datetime import date


def get_dob():
	birth_year= int(input('enter your birth year:'))
	birth_month= int(input('enter your birth month:'))
	birth_day= int(input('enter birth day:'))
	import datetime as dt 
	date=dt.date(birth_year,birth_month,birth_day)
	return date

    # write code here
	
print (get_dob())


def get_age(dob):
    # write code here
	...


def main():
	# write code here
	...


if __name__ == '__main__':
    main()
