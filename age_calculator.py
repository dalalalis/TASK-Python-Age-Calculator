

import datetime as dt 
def get_dob():
	birth_year= int(input('enter your birth year:'))
	birth_month= int(input('enter your birth month:'))
	birth_day= int(input('enter birth day:')) 
	dob=dt.date(birth_year,birth_month,birth_day)
	print(dob)
	return (dob.year)

    # write code here
#get_dob()




def get_age(dob):
	import datetime
	today= datetime.date.today()
	age= today.year -dob.year
	
	return (age)

	
#(get_age(get_dob()))



# write code here
def main():
	import datetime
	date_year= datetime.date.today().year
	dob=get_dob()
	age= get_age(dob)
	if get_dob.year < date_year:
		return (age)
	else:
		print ("invalid date of birth")

	



if __name__ == '__main__':
    main()
