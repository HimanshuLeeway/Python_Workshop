guests = {}

num_guests = int(
  input("How many guests would you like to invite to the party? "))

for i in range(num_guests):
  name = input("Enter the name of guest {}: ".format(i + 1))
  favorite_food = input("Enter {}'s favorite food: ".format(name))

  guest_info = [name, favorite_food]

  guests[name] = guest_info

print("Guest List:")
for name, guest_info in guests.items():
  print("- {} likes to eat {}".format(name, guest_info[1]))
