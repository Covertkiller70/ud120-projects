#!/usr/bin/python

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

def findPOI(name, feature):
    for person in enron_data:
        search = name.upper()
        if person.find(search) != -1:
            print(person + ' ' + str(enron_data[person][feature]))

def hasEmailSalary():
    ecount = 0
    scount = 0
    utpcount = 0
    poi_utpcount = 0
    poi_count = 0

    for person in enron_data:
        if enron_data[person]['salary'] != 'NaN':
            scount += 1
        if enron_data[person]['email_address'] != 'NaN':
            ecount += 1
        if enron_data[person]['total_payments'] == 'NaN':
            utpcount += 1
        if enron_data[person]['total_payments'] == 'NaN' and enron_data[person]['poi'] == True:
            poi_utpcount += 1
        if enron_data[person]['poi'] == True:
            poi_count += 1
    print('Known Emails: ' + str(ecount))
    print('Known Salaries: ' + str(scount))
    print('Unkown Total payments: '+ str(utpcount))
    print('Total POI that did not get paid: ' + str(poi_utpcount))
    print('Total Dataset: ' + str(len(enron_data)))
    print('Total POIs: ' + str(poi_count))
    return utpcount

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))
hasEmailSalary()
print(hasEmailSalary() / len(enron_data) * 100)
#findPOI('skilling','total_payments')
#findPOI('lay','total_payments')
#findPOI('fastow','total_payments')