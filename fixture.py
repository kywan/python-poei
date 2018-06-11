#!/usr/bin/env python


import mysql.connector
from faker import Faker

db = mysql.connector.connect(host="127.0.0.1", user="root", database="base_sql")
cursor = db.cursor()
i = 0

fake = Faker()
while i < 5000:
    user = (i, fake.first_name(), fake.last_name(), fake.email(), fake.date(pattern="%Y-%m-%d", end_datetime=None), fake.country(), fake.city(), fake.postcode())
    cursor.execute("""INSERT INTO `utilisateur`(`id`, `nom`, `prenom`, `email`, `date_naissance`, `pays`, `ville`, `code_postal`) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)""",user)
    i += 1

db.commit()
db.close()
