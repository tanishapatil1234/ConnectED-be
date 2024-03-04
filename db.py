import sqlite3
from models.account_type import Account, Person, Member, Admin
from models.company import Company, JobPosting
from models.group_post import Group, Post, Message
from models.profile import Profile, Experience
from models.constants import Address

# Connect to SQLite database
conn = sqlite3.connect('volumes/sqlite.db')
cursor = conn.cursor()

# Create Account table
cursor.execute('''CREATE TABLE IF NOT EXISTS Account (
                    id TEXT PRIMARY KEY,
                    password TEXT,
                    status INTEGER
                )''')

# Create Person table
cursor.execute('''CREATE TABLE IF NOT EXISTS Person (
                    name TEXT,
                    address_street TEXT,
                    address_city TEXT,
                    address_state TEXT,
                    address_zip_code TEXT,
                    address_country TEXT,
                    email TEXT,
                    phone TEXT,
                    account_id TEXT,
                    FOREIGN KEY(account_id) REFERENCES Account(id)
                )''')

# Create Member table
cursor.execute('''CREATE TABLE IF NOT EXISTS Member (
                    date_of_membership TEXT,
                    headline TEXT,
                    profile_summary TEXT,
                    profile_experiences TEXT,
                    profile_educations TEXT,
                    profile_skills TEXT,
                    profile_accomplishments TEXT,
                    profile_recommendations TEXT,
                    account_id TEXT,
                    FOREIGN KEY(account_id) REFERENCES Account(id)
                )''')

# Create Admin table
cursor.execute('''CREATE TABLE IF NOT EXISTS Admin (
                    name TEXT,
                    address_street TEXT,
                    address_city TEXT,
                    address_state TEXT,
                    address_zip_code TEXT,
                    address_country TEXT,
                    email TEXT,
                    phone TEXT,
                    account_id TEXT,
                    FOREIGN KEY(account_id) REFERENCES Account(id)
                )''')

# Create Company table
cursor.execute('''CREATE TABLE IF NOT EXISTS Company (
                    name TEXT PRIMARY KEY,
                    description TEXT,
                    type TEXT,
                    company_size INTEGER
                )''')

# Create JobPosting table
cursor.execute('''CREATE TABLE IF NOT EXISTS JobPosting (
                    description TEXT,
                    employment_type TEXT,
                    location TEXT,
                    is_fulfilled INTEGER,
                    date_of_posting TEXT,
                    company_name TEXT,
                    FOREIGN KEY(company_name) REFERENCES Company(name)
                )''')

# Create Group table
cursor.execute('''CREATE TABLE IF NOT EXISTS `Group` (
                    name TEXT PRIMARY KEY,
                    description TEXT,
                    total_members INTEGER
                )''')

# Create Post table
cursor.execute('''CREATE TABLE IF NOT EXISTS Post (
                    text TEXT,
                    total_likes INTEGER,
                    total_shares INTEGER,
                    owner_name TEXT,
                    FOREIGN KEY(owner_name) REFERENCES Member(name)
                )''')

# Create Message table
cursor.execute('''CREATE TABLE IF NOT EXISTS Message (
                    sent_to TEXT,
                    message_body TEXT,
                    media BLOB
                )''')

# Create Profile table
cursor.execute('''CREATE TABLE IF NOT EXISTS Profile (
                    summary TEXT,
                    experiences TEXT,
                    educations TEXT,
                    skills TEXT,
                    accomplishments TEXT,
                    recommendations TEXT
                )''')

# Create Experience table
cursor.execute('''CREATE TABLE IF NOT EXISTS Experience (
                    title TEXT,
                    company TEXT,
                    location TEXT,
                    date_from TEXT,
                    date_to TEXT,
                    description TEXT,
                    profile_owner TEXT,
                    FOREIGN KEY(profile_owner) REFERENCES Member(name)
                )''')

# Create Address table
cursor.execute('''CREATE TABLE IF NOT EXISTS Address (
                    street TEXT,
                    city TEXT,
                    state TEXT,
                    zip_code TEXT,
                    country TEXT
                )''')

# Commit changes and close connection
conn.commit()
conn.close()
