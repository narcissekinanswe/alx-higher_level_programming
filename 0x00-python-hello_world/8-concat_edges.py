#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
print(str[str.find("object-oriented programming"):].split()[0] + " " + str[str.find("object-oriented programming"):].split()[1] + " " + str[str.find("object-oriented programming"):].split()[2] + " " + str[str.find("object-oriented programming"):].split()[3] + " " + str[str.find("object-oriented programming"):].split()[4] + " " + str[str.find("object-oriented programming"):].split()[5] + ",")

