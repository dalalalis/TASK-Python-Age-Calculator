from datetime import date 

def get_dob(): 
	birth_year= int(input('enter your birth year:'))
	birth_month= int(input('enter your birth month:'))
	birth_day= int(input('enter birth day:'))
	import datetime as dt 
	date=dt.date(birth_year,birth_month,birth_day)
	print (date)
	return (birth_year)


    # write code here
#get_dob()




def get_age (dob):
	import datetime
	today= datetime.date.today()
	age= today.year - dob
	return (age)

	
#print (get_age(get_dob()))


# write code here
def main():
	import datetime
	age = get_age(get_dob())
	age1= int(age)
	if age1 >=1:
		return age
	else:
		return ("invalid date of birth")

print (main())


#if __name__ == '__main__':
    #main()
