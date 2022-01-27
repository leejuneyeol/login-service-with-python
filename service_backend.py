import sqlite3
import hashlib
import re

def hash(text):
    data = text.encode()
    hash_object = hashlib.sha1()
    hash_object.update(data)
    hex_dig = hash_object.hexdigest()
    return hex_dig

p = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
conn = sqlite3.connect("user.db", isolation_level=None)
# 커서 획득
c = conn.cursor()
# 테이블 생성 (데이터 타입은 TEST, NUMERIC, INTEGER, REAL, BLOB 등)
c.execute("CREATE TABLE IF NOT EXISTS information \
    (dlwnsdufcjswo, id, password, name, phone, email)")

already_id = []
password_hash = []
c.execute("SELECT * FROM information")
for row in c.fetchall():
    already_id.append(row[1])
    password_hash.append(row[2])

def sign_up():
    while True:
        id = input("Enter ID: ")
        if id.encode().isalnum() != True:
            print("Error")
        elif id in already_id:
            print('already exist')
        else:
            break
    while True:
        password = input("Enter password: ")
        def passwordCheck(pwd):
            if len(pwd) < 8 or len(pwd) > 21 and not re.findall('[0-9]+', pwd) and not \
            re.findall('[a-z]', pwd):
                print("Error")
            elif not re.findall('[`~!@#$%^&*(),<.>/?]+', pwd):
                print("Error")
            else:
                return True
        if passwordCheck(password) == True:
            password = hash(password)
            break
    while True:
        name = input("Enter name: ")
        if name.isalnum() != True:
            print("Error")
        else:
            break
    phone_number = input("Enter phone_number: ")
    try:
        phone_number = phone_number.replace('-', '')
    except:
        pass
    while True:
        email = input("Enter email: ")
        if p.match(email) == None:
            print("Error")
        else:
            break

    c.execute(f"INSERT INTO information \
        VALUES(1, '{id}', '{password}', '{name}', '{phone_number}', '{email}')")

def auto_sign_up(id, password, name, phone_number, email):
    if id.encode().isalnum() != True:
        raise ValueError("Invalid ID")
    def passwordCheck(pwd):
        if len(pwd) < 8 or len(pwd) > 21 and not re.findall('[0-9]+', pwd) and not \
        re.findall('[a-z]', pwd):
            raise ValueError("Invalid password")
        elif not re.findall('[`~!@#$%^&*(),<.>/?]+', pwd):
            raise ValueError("Invalid password")
        else:
            return True
    if passwordCheck(password) == True:
        password = hash(password)
    if name.isalnum() != True:
        raise ValueError("Invalid name")
    try:
        phone_number = phone_number.replace('-', '')
    except:
        pass
    if p.match(email) == None:
        raise ValueError("Invalid error")

    c.execute(f"INSERT INTO information \
        VALUES(1, '{id}', '{password}', '{name}', '{phone_number}', '{email}')")
    
def sign_in():
    id = input("Enter ID: ")
    password = hash(input("Enter Password: "))
    try:
        index_id = already_id.index(id)
        index_password = password_hash[index_id]
        if index_password == password:
            print('Login!')
        else:
            print('Error')
    except:
        print("Unknown ID")
        
def unhash_sign_in(id, password_hash_data):
    try:
        index_id = already_id.index(id)
        index_password = password_hash[index_id]
        if index_password == password_hash_data:
            print('Login!')
        else:
            print('Error')
    except:
        print("Unknown ID")