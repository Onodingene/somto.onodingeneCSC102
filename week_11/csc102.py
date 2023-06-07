
class pau_sis:
    def questions(self):
        global name
        name = input("Enter your full name: ").upper()
        global age
        age = int(input("Enter your age: "))
        if age > 14 and age < 18:
            school.the_pirates()
        elif age > 18 and age < 22:
            school.the_yankees()
        elif age > 22:
            school.the_bulls()
        else:
            print("THIS INFORMATION DOES NOT EXIST IN OUR DATABASE!")

    def the_pirates(self):
        import pandas as pd
        file = pd.read_csv('pirates.csv')
        print(file)

    def the_yankees(self):
        import pandas as pd
        file = pd.read_csv('yankees.csv')
        print(file)

    def the_bulls(self):
        import pandas as pd
        file = pd.read_csv('bulls.csv')
        print(file)

school = pau_sis()
school.questions()
