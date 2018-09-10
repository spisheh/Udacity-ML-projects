
""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))


#f = open( "../final_project/poi_names.txt", "r" )
#count=0
"""for i in f.readlines():
	print(i[:3])
	if "(y)" in i:
		count+=1 
for i in enron_data.keys():
	if "JAMES" in i:
		print(i)"""

"""print(enron_data["Fastow Andrew S".upper()]["total_payments"])
print(enron_data["Lay Kenneth L".upper()]["total_payments"])
print(enron_data["Skilling Jeffrey K".upper()]["total_payments"])"""
e=0
s=0
for i in enron_data.values():
	if i["total_payments"]=="NaN" and i["poi"]:
		s+=1
	#if i["email_address"]!="NaN":
	e+=1
print(s,e)