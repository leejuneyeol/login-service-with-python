from service_backend import auto_sign_up as au
from service_backend import unhash_sign_in as us
from faker import Faker
import sqlite3

conn = sqlite3.connect("user.db", isolation_level=None)
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS information \
    (dlwnsdufcjswo, id, password, name, phone, email)")

ids = []
pwds = []
c.execute("SELECT * FROM information")
for row in c.fetchall():
    ids.append(row[1])
    pwds.append(row[2])

def dummygenerator():
    fake = Faker("Ko-KR")  
    for i in range(10):
        dic = {}
        id = fake.user_name()
        password = fake.password()
        name = fake.name()
        phone_number = fake.phone_number()
        email = fake.email()
        dic['id'] = id
        dic['password'] = password
        print(dic)
        try:
            au(id, password, name, phone_number,email)
        except:
            print('Error')
            pass
        
for i in range(10):
    us(ids[i], pwds[i])