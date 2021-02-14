def overtime():
  hourly_rate = pound 
  return hourly_rate


pound = int(input("Enter your hourly rate: ")) 
print("Your weekly hourly rate is: {}, your Saturday's rate is: {}, your Sunday's rate is: {}".format(pound, pound //2 + pound, pound*2))
