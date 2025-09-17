customers = ["Sunil", "Rajat", "Sahil", "Inderjot", "Madan"]
bills = [12,23,45,56,7,8]

for customer, bill in zip(customers, bills): # retusn tuple that is unpacked 
    print(f"{customer} paid ${bill}")