def overtime():
  wage = pound 
  return wage


pound = int(input("Enter your wage: ")) 
print("Weekly hourly payment is: {}, Saturday overtime is: {}, Sunday overtime is: {}".format(pound, pound //2 + pound, pound*2))