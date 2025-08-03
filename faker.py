import random
import os

def get_days_in_month(month, year):
    month_days = {
        1: 31, 2: 28, 3: 31, 4: 30,
        5: 31, 6: 30, 7: 31, 8: 31,
        9: 30, 10: 31, 11: 30, 12: 31
    }

    # Leap year check for February
    if month == 2 and ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
        return 29
    return month_days.get(month, 0)

gender = ""
name = ""
address = ""
age = 0
phone = 0
occupation = "Cook", "Neurobiologist", "Police Officer", "School Teacher", "Musician", "Medical Doctor", "Tech Support", "Unemployed", "Cashier", "Manager", "Waiter", "Author", "Construction Worker", "Artist", "Chiropractor", "Youtuber", "Beggar", "Geologist", "Marine Biologist", "Animator", "Programmer", "Web developer", "College Student", "Engineer", "Streamer", "Profesional Athlete", "Veterinarian", "Nurse", "Archeologist", "Coder", "Unemployed: Though applied", "Topologist", "Chemist", "Realtor", "Cartographer", "Fisherman", "Several jobs", "Several jobs", "Currently in prison", 
malenames = "Cole", "Chris", "Jacob", "Jack", "Jackson", "Tom", "Thomas", "Robert", "John", "Arthur", "Joe", "Oliver", "Charlie", "Charles", "Brady", "Brody", "Levi", "Noah", "Brooks", "Liam", "Ben", "Benjamin", "Max", "Gavin", "James", "Dave", "David", "Cameron", "Anthony", "Hunter", "Pedro", "Kyle", "Tyler", "Norman", "Elijah", "Lucas", "Theodore", "Will", "Leo", "Sebastion", "Daniel", "Richard", "Matthew", "Mark", "Donald", "Steven", "Andrew", "Paul", "Joshua", "Kenneth", "Kevin", "Brian", "George", "Jason", "Ryan", "Samuel", "Dennis", "Aaron", "Nathan", "Jim", "Eddie", "Jamal", "Miguel", "Aiden", "Garfield", "Nick", "Indigo", "Buddy", "Quin", "Deis", "Clifton", "Sean", "Wendell", "Brandon", "Casey", "Sully", 
femalenames = "Becka", "Rebecca", "Mary", "Allysa", "Brook", "Brookllyn", "Ava", "Emma", "Olivia", "Amy", "Bella", "Ashllyn", "Hannah", "Lily", "Fiona", "Gianna", "Avery", "Taylor", "Blake", "Jessica", "Kerry", "Linda", "Elizabeth", "Susan", "Karen", "Sarah", "Barbara", "Lisa", "Nancy", "Emily", "Carol", "Amanda", "Michelle", "Laura", "Angela", "Brenda", "Ana", "Katherine", "Debra", "Janet", "Maria", "Heather", "Helen", "Julie", "Ruth", "Evelyn", "Andria", "Abigail", "Sophia", "Grace", "Amber", "Alice", "Diana", "Elixis", "Kayla", "Lori", "Athena", "Skylar", "Marriah", "Harper", "Carlie", "Lucy", "Haidi", "Candice", "Alisha", "Emily", "Debbi", "Jade", "Ruby", "Josie", "Natalie", "Melody", "Janite", "Kaitlin", "Kit", "Holly", "Lila", "Lexi", "Rosalina", "Roxie", "Tia", "Dottie", "Kimberland", "Robin", "Audrie", 
surnames = "Miller", "Sanderson", "Arlow", "Pearl", "Benoit", "Mason", "Marrow", "Miles", "Oral", "Li", "Lee", "Eirra", "Streal", "Arkalyn", "Varey", "Smith", "Brown", "Williams", "Johnson", "Jackson", "Jones", "Wilson", "Harris", "Clark", "Davis", "Robinson", "Walker", "Young", "Scott", "Nelson", "Campbell", "Parker", "Cook", "Cooper", "Reed", "Kelly", "Watson", "Bennet", "Gray", "Myers", "Brian", "Drake", "Douglas", "Carson", "Enola", "Linton", "Webster", "Stinson", "Ericson", "Aldren", "Ross", "Geller", 
genders = "Male", "Female"
road = "Main St.", "Second St.", "Mountain Rd.", "California Rd.", "Master St.", "First St." "Ark Dr.", "Chicken St.", "Henry St.", "Hippopotamus St.", "Limb Rd.", "Snake Dr.", "Apricot Rd.", "Hawk Dr.", 
location = "Ohio", "Nigeria", "Uzbekistan", "Massachussets", "Ghana", "South Africa", "California", "Rhode Island", "Texas", "Colorado", "Utah", "Maine", "Spain", "New York", "Los Angelos", "Australia", "Oregon", "Mississipi", "Nashville", "Alabama", "New Zealand", "Michigan", "Malbourn", "San Fransisco", "Denmark", "Wisconsin", "Birkshire", "Ontario", "South Carolina", "Charleston", "Oklahoma", "Philadelphia", "Indiana", "Houston", "North Carolina", "Alberta, Canada", "Brazil", "Orlando", "Vietnam", "Korea", "China", "Ireland", "Singapore", "Senegal", "Chad", "Kenya", "Germany", "Luxemborg", "Poland", "Iceland", "Greenland", "Denver", "Boston", "Louisiana", "Hungary", "Croatia", "Czech Republic", "Austria", "Netheralnds", "Belgium", "Serbia", "North Macedonia", "South Macedonia", "Ukraine", "Latvia", "Sudan", "Madagascar", "Liberia", "West Sahara", "Portugal", 
causeofdeath = "Old age", "Murdered", "Suicide", "Hit by a car", "Old age", "Old age", "Accident", "Heart attack", "Unknown", "Cancer", "Old age", "Old age", "Old age", "Old age", "Cancer", "Cancer",
bloodtype = "A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-",
edubackground = "Masters", "Bachelors", "High School Diploma", "Doctorate", "Associates", "PHD", "Some college, no diploma"
major = "Computer Science", "Philosophy", "Psychology", "Environmental Science", "Socialogy", "Education", "Economics", "Law", "Civil Engineering", "Mechanical Engineering", "Electrical Engineering", "Programming", "History", "Nursing", "Business", "Mathematics",
interests = "Coding", "Art", "Writing", "Drawing", "Cooking", "Calligraphy", "Science", "Learning", "Law", "Engineering", "Talking to people", "Sports", "Hockey", "Basketball", "Football", "Soccer", "Gymnastics", "Baseball", "Reading", "Playing piano", "Playing guitar", "Singing", "Playing clarinet", "Playing saxaphone", "Playing oboe", "Playing tuba", "Playing trumpet", "History", "Mathematics", "Business", "Gardening", "Traveling", "Working", "Economics", "Philosophy", "Recording videos", 
bhabits = "Gambling", "Smoking", "None", "None", "None", "None", "None", "None", "None", "None", "Anger Issues", "Envy", "Betting", "Judging others", 
month = random.randint(1, 12)
year = random.randint(1970, 2005)
days_in_month = get_days_in_month(month, year)
day = random.randint(1, days_in_month)
birthdate = f"{year:04d}-{month:02d}-{day:02d}"
num1 = random.randint(1, 999)
pnum1 = f"{num1:03}"
num2 = random.randint(1, 999)
pnum2 = f"{num2:03}"
num3 = random.randint(1, 9999)
pnum3 = f"{num3:04}"

while True:
    selection = input("Press enter to start! ")
    if selection == "":
        os.system('clear')
        month = random.randint(1, 12)
        year = random.randint(1970, 2005)
        days_in_month = get_days_in_month(month, year)
        day = random.randint(1, days_in_month)
        birthdate = f"{year:04d}-{month:02d}-{day:02d}"
        num1 = random.randint(1, 999)
        pnum1 = f"{num1:03}"
        num2 = random.randint(1, 999)
        pnum2 = f"{num2:03}"
        num3 = random.randint(1, 9999)
        pnum3 = f"{num3:04}"
        gender = (random.choice(genders))
        occupationvar = random.choice(occupation)
        print("Gender:", gender)
        if gender == "Male":
            name = print("Name:", random.choice(malenames), random.choice(surnames))
        else:
            name = print("Name:", random.choice(femalenames), random.choice(surnames))
        print("Location:", random.choice(location), random.randint(1000, 5000), random.choice(road), )
        print("Phone Number:", pnum1 + "-" + pnum2 + "-" + pnum3)
        print("Occupation:", occupationvar)
        print("Birthdate:", birthdate)
        print("Cause of Death:", random.choice(causeofdeath))
        print("Blood Type:", random.choice(bloodtype))
        if occupationvar == "College Student":
            print("Educational Background: In progress")
        else:
            print("Educational Background:", random.choice(edubackground))
        print("Major:", random.choice(major))
        print("Family Members:", random.randint(3, 5))
        print("Interests:", random.choice(interests) + ",", random.choice(interests) + ",", random.choice(interests) + ",")
        print("Bad Habits:", random.choice(bhabits))
    elif selection == "gender":
        print(gender)
    elif selection == "clear":
        os.system('clear')
    elif selection == "exit":
        break
    
