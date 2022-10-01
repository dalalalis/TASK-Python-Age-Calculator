

import datetime 
def get_dob():
	birth_year= input("which year were you born?")
	birth_month=input("which month were you born ?")
	birth_day=input("in which day of the month were you bonrn?")
	dob=datetime.date(birth_year,birth_month,birth_day)
	print(dob)
	dob=dob.year
	return (dob)

    # write code here
#get_dob()




def get_age (dob):
	dob-int(dob)
	import datetime
	today= datetime.date.today()
	age= today.year - dob
	print (age)

	



# write code here
def main():
	import datetime
	dob=get_dob()
	age=get_age(dob) 
	date_year= datetime.date.year.today()
	if dob< date_year:
		return (age)
	else:
		print ("invalid date of birth")

	
print (main())


#if __name__ == '__main__':
    #main()
