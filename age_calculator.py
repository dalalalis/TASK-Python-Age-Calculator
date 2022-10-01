

import datetime 
def get_dob():
	birth_year= input("which year were you born?")
	birth_month=input("which month were you born ?")
	birth_day=input("in which day of the month were you bonrn?")
	dob=datetime.date(birth_year,birth_month,birth_day)
	print(dob)
	return (dob.year)

    # write code here
#get_dob()




def get_age(dob):
	import datetime
	today= datetime.date.today()
	age= today.year - get_dob
	
	print (age)

	
(get_age(get_dob))



# write code here
def main():
	import datetime
	dobyear=get_dob()
	age=get_age(dob) 
	date_year= datetime.date.year.today()
	if dobyear< date_year:
		return (age)
	else:
		print ("invalid date of birth")

	



if __name__ == '__main__':
    main()
