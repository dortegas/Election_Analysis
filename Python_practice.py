# print("Hello World!")
#print(5 + 2*3)
#print(8//5-3)
#print(8 + 22 *2 -4)
#print(16 - 3/2 + 7 - 1)
#print(3**3%5)
#print(5+9*3/2-4)
#print(3 % 5)
#print(3 ** (3 % 5))

#counties = ["Arapahoe","Denver","Jefferson"]
#counties.append("El Paso")
#counties.insert(2,"El Paso")

#print(counties)

#counties.remove("El Paso")
#print(counties)

#counties.pop()
#print(counties)
#print(len(counties))

#counties = ["Arapahoe","Denver","Jefferson"]
#counties.insert(1,"El Paso")
#counties.remove("Arapahoe")
#counties[2] = "Denver"
#counties[1] = "Jefferson"
#counties.append("Arapahoe")
#print(counties)

#counties = {}
#counties = dict()
#counties["Arapahoe"] = 422829
#counties["Denver"] = 463353
#counties["Jefferson"] = 432438

#print(counties) 
#print(counties.items())
#print(counties['Arapahoe'])

# voting_data = []
# voting_data.append({"county":"Arapahoe","registered_voters":422829})
# voting_data.append({"county":"Denver","registered_voters":463353})
# voting_data.append({"county":"Jefferson","registered_voters":432438})

# #print(voting_data)

# voting_data.insert(1,{"county":"El Paso","registered_voters":461149})
# voting_data.pop(0)
# voting_data[2] = {"county":"Denver","registered_voters":463353}
# voting_data[1] = {"county":"Jefferson","registered_voters":432438}
# voting_data.append({"county":"Arapahoe","registered_voters":422829})

# print(voting_data)

# counties = ["Arapahoe","Denver","Jefferson"]
# if counties[1] == 'Denver':
#     print(counties[1])


# temperature = int(input("What is the temperature outside? "))

# if temperature > 80:
#     print("Turn on the AC.")
# else:
#     print("Open the windows.")

# x = 0
# while x <= 5:
#     print(x)
#     x = x + 1

# for num in range(5):
#     print(num)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# for county in counties_dict:
#     print(county)

#for county in counties_dict.keys():
 #   print(county)

#print(counties_dict.keys()) 

# print(counties_dict.values()) 

# print(counties_dict['Denver'])

# for county in counties_dict:
#     print(counties_dict[county])

# for key, value in counties_dict.items():
#     print(key, value)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

# for county_dict in voting_data:
#     print(county_dict)

# for county_dict in range(len(voting_data)):
#     print(voting_data[county_dict])

# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)

# for county_dict in voting_data:  
#      print(county_dict.values())

# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters} registered voters.")

# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
#     f'You received {candidate_votes:,} number of votes. '
#     f'The total number of votes in the election was {total_votes:,}. '
#     f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

# print(message_to_candidate)

# counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
# for county, voters in counties_dict.items():
#   print(county + " county has " + str(voters) + " registered voters.")

# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters:,} registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

for county in voting_data:
    print(f"{county['county']} county has {county['registered_voters']:,} registered voters.")