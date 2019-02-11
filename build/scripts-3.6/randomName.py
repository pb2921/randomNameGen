#!python

import csv

import random


class randomName:
 
  def __init__(self):
     print(f"Random Name-Record generator\n")
 
  def ranNameGenerator(self):

    records= int(input('Enter Number of Records :'))  

    #records=100

    print(f"Making  records\n" ,records)

 

 

    fieldnames=['id','name','last_name','age','city','mobile_number','salary','credit_points']

    writer = csv.DictWriter(open("people_Names_Details.csv", "w",newline="\n"), fieldnames=fieldnames)

 
    with open('1000Names.txt') as f:
        names = f.read().splitlines()
     
    with open('100lastNames.txt') as f1:
        last_names = f1.read().splitlines()
    
    
    cities=['New Delhi', 'Sydney', 'Melbourne', 'London', 'Shanghai', 'New York', 'Singapore','Tokyo', 'Taipei','Sao Palo','Bangalore'

            ,'Shenzhen','Kyoto','Seol','Johannesburg','Toronto','Denver','Hartford', 'Texas']

 

    writer.writerow(dict(zip(fieldnames, fieldnames)))

    for i in range(0, records):

     writer.writerow(dict([

        ('id', i+1000),

        ('name', random.choice(names)),
        ('last_name', random.choice(last_names)),

        ('age', str(random.randint(24,34))),

        ('city', random.choice(cities)),

        ('mobile_number', str(random.randint(9000000000,9999999999))),

        ('salary', str(random.randint(50000,700000))),

        ('credit_points',random.randint(1, 9))  

          ]))

randomName1 = randomName()
randomName1.ranNameGenerator()
