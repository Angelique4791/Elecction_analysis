from pkgutil import walk_packages


print("Hello World!")
print("Hello to you, too, Atom!")
name = "Brian Johnson"
country = "United States"
age = 34
hourly_wage = 12
daily_wage = hourly_wage * 8
satisfied = True
print(f'Hello {name}')
print(f'{name} is from {country}')
print(f'{name} is {age} years old')
print(f'{name} earned ${daily_wage} today')
print (f'{name} is satisfied? {satisfied}')

counties =["Arapahoe","Denver","Jefferson"]
counties.append("El Paso")

counties_tuple = ("Arapahoe","Denver","Jefferson","El Paso")

counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict ["Denver"] = 463353
counties_dict ["Jefferson"] = 432438
counties_dict ["El Paso"] = 461149

voting_data = []

voting_data.append({"county":"Arapahoe","registered_voters":422829})
voting_data.append({"county":"Denver","registered_voters":463353})
voting_data.append({"county":"Jefferson","registered_voters":432829})
voting_data.append({"county":"El Paso","registered_voters":461149})

#Input statements
#How many votes did you get?
my_votes = int(input("How many votes did you get in the election?"))
#Total votes in election
total_votes = int(input("What is the total number of votes in the election?"))
#Calculate percentage of votes you received
percentage_votes = (my_votes/total_votes)*100
print("I received " + str(percentage_votes) + "% of the total votes.")

#If statements
if counties[1] == "Denver":
    print(counties[1])

if counties[3] != 'Jefferson':
    print (counties[2])

temperature = int(input("What is the temperature outside?"))

if temperature >80:
    print("Turn on AC.")
else:
    print("Open the window")

#What is the grade?
score = int(input("What is your test score?"))

#Determine grade
if score >= 90:
    print("Your grade is an A.")
else:
    if score >= 80:
        print("Your grade is a B.")
    else:
        if score >= 70:
            print("Your grade is a C.")
        else:
            if score >= 60:
                print("Your grade is a D.")
            else:
                print("Your grade is an F.")

#What is the grade?
score = int(input("Provide your score to receive your grade."))
#Determine the grade
if score >= 90:
    print("Your grade is an A.")
elif score >= 80:
    print("Your grade is a B.")
elif score >= 70:
    print("Your grade is a C.")
elif score >= 60:
    print("Your grde is a D.")
else:
    print("Your grade is an F.")

# Membership function
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")

#Logical and Membership coumpound function
if"Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")
if"Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

#Loops!!!
x=5
while x<=10:
    print(x)

    x=x+1

for county in counties:
    print(county)
numbers = [0,1,2,3,4]
for nm in numbers:
    print(nm)  
for nm in range(5):
    print(nm)
print("first")
for i in range(len(counties)):
    print(counties[i])
print("second")
for i in range(len(counties_tuple)):
    print(counties_tuple[i])
print("third")        
for county in counties_dict:
    print(county)
print("fourth")
for county in counties_dict.keys():
    print(county)
for voters in counties_dict.values():
    print(voters)
    print("second")
for county in counties_dict:
    print(counties_dict[county])
print("third")
for county in counties_dict:
    print(counties_dict.get(county))
    
#INCORRECT OUTPUT-----------------------------------------------------------------

    #---------------------------------------------------------------------------------
for county_dict in voting_data:
    print(county_dict)
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
# F-string comparison
for county,voters in counties_dict.items():
    print(county + " county has " + str(voters)+ "registered voters.")

for county,voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

#Candidate results
candidate_votes = int(input("How many votes did the candidate get in the election?"))
total_votes = int(input("What is the total number of votes in the election?"))
message_to_candidate = (
    f"You received {candidate_votes} number of votes."
    f"The total number of votes in the election was {total_votes}."
    f"You received {candidate_votes/total_votes*100}% of the total votes.")
print(message_to_candidate)

#Import the datetime class from the datetime module.
import datetime
#Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
#Print the present time.
print("The present time is ",now)
print("NOW'S THE TIME!!!")

for x in range(2,7):
    print(x)
    