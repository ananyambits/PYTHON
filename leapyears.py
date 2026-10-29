StartYear= int(input("Enter the Start year:"))
end_year= int(input("Enter the end year:"))
print("List of loop years:")
for year in range(StartYear,end_year):
	if((year%4==0)and(year%100!=0))or(year%400==0):
		print(year) 
