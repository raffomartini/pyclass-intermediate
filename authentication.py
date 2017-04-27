'''
authentication -- who you are 
authorization -- what you are permitted 
'''

passwords = {}

### Pain text :( #########################

# def store_password(username, password):
#     passwords[username] = password
#
# def check_password(username, password):
#     return passwords[username] == password

### Two way encryption ###################

# def store_password(username, password):
#     passwords[username] = password.encode('rot-13')
#
# def check_password(username, password):
#     return passwords[username].decode('rot-13') == password

### One way encryption ###################

# def store_password(username, password):
#     passwords[username] = hash(password)
#
# def check_password(username, password):
#     return passwords[username] == hash(password)

### Cryptohash #################################

# import md5
#
# def store_password(username, password):
#     passwords[username] = md5.new(password).hexdigest()
#
# def check_password(username, password):
#     return passwords[username] == md5.new(password).hexdigest()

### Modern Cryptohash #################################

import hashlib

def store_password(username, password):
    passwords[username] = hashlib.sha512(password).hexdigest()

def check_password(username, password):
    return passwords[username] == hashlib.sha512(password).hexdigest()

### Rainbow Table #####################################

rainbow = {}

with open('data/common_passwords.txt') as f:
    for line in f:
        password = line.split(', ')[0]
        hashcode = hashlib.sha512(password).hexdigest()
        rainbow[hashcode] = password

### Add some salt ######################################
# salt is per-user
# pepper is per-application

import string
import random

alphabeth = string.ascii_letters + string.digits + string.punctuation

def good_password(n=20):
    return ''.join(random.choice(alphabeth) for i in range(n))

def slowhash(password, salt, repeats = int(5e5)):
    hashcode = hashlib.sha512(password + salt).hexdigest()
    for i in xrange(repeats):
        hashcode = hashlib.sha512(hashcode).hexdigest()

def store_password(username, password):
    salt = good_password()
    hashcode = slowhash(password, salt)
    passwords[username] = hashcode, salt

def check_password(username, password):
    hashcode, salt = passwords[username]
    return hashcode == slowhash(password, salt)

if __name__ == '__main__':
    store_password('admin', 'cisco123')
    print check_password('admin', 'cisco123')
    print check_password('admin', 'cisco124')
    print passwords

    # Test Acccounts

    crummy_passwords = '''\
    admin root superman password cisco snoopy password1 Password password.
    password! !password (password)'''.split()
    for i, password in enumerate(crummy_passwords):
        username = 'User{:03d}'.format(i)
        store_password(username, password)


    # Rainbow Attack
    fmt = 'Gotcha! {user} {password}'
    # for username, hashcode in sorted(password.item()):
    #     if hashcode in rainbow:
    #         print 'haha'
