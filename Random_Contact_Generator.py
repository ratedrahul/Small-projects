import random

first_name=['Aaradhya','Akansha','Aditi','Priya','Aishwarya','Anamika','Anjali','Ambika','Aarohi','Avni','Babita','Bhawna','Chanchal','Aarav','Abhishek','Arjun','Vihaan','Aditya','Sai','Riyansh','Krishna','Ishan','Dhruv','Ryan','Kabir','Shaurya','Aayuhman','Ayush','Ankit','Akhilesh','Aanand','Parth','Raghav','Jai','Dev','Ansh','Shiva','Shivansh','Manish','Neel','Om','Anirudh','Dev','Yash','Sarthak','Rohan','Rohit','Ranu','Pranav','Samarth','Sahil','Ajay','Sandeep','Sanjay']
#print((first_name))


last_name=['Gupta','Ahirwar','Sharma','Jayaswal','Jain','Verma','Gome','Khandelwal','Kuwal','Gehlod','Sani','Khurana','Kapoor','Vashistha','Manjhi','Das','Dohe','Ghosh','Patra','Modi','Solanki','Kumawat','Dongre','Roshan','Mali','Saini','Pahadiya','Singh','Jodha','ShriVastav','Pancholi','Choudhary','Parmar','Borasi','Pandey','Chawla','Rai','Tapadiya','Yadav','Dhawan','Kumar','Tandan','Chopra','Malya','Ayyar','Morya','Kashyap','Athawale','Thakkad']
#print(last_name)

address_place=['Vijay nagar','Gori nagar','Ambedkar Nagar','Gandhi Nagar','M.G.Road','Indira Gandhi Marg','Patel Marg','Gulmohar Township','Silvar Township','Residency Colony','Sadar Bazar','corporate society','Sector A','Sector B','Sector C','Sector D','Shiv Nagar','Mahavir Nagar','Bangali Colony','Shastri Nagar','Industrial Area','Ring Road','Lakshmi Nagar','Sudama nagar','Rajendra nagar','Nehru nagar','Vidya Vihar','VidyaVihar Society','Bhim nagar','Ambedkar Chowk','Usha nagar','Subhash nagar','Hyper city','Sai Colony','Transport colony','Radio colony','Aazad nagar','Saket Nagar','Sarafa','Nayapura','Maratha Nagar']
nearby=['Big Bazar','Central Park','Zoo Road','Nehru square','Kotwali ','Radhakishan Temple','Shiva Temple','Satya Sai School','Medical college','City Center','Cloth Market','Ganesh Mandir','St.Josheph Church','Apollo Hospital','Electronic Complex','Iskon Temple','PNB','SBI','petrol pump','Dashahara Maidan','Green Garden','Bus Stand','Riksha Stand','Railway station','Gopal kirana','KFC','Pizza hut','Mcdonolds','Government School','Pani ki tanki','Police station','Kendriya Vidhyalaya','Book store','Book market','Sabji market','Fish market','Rajiv Gandhi Square','Tower Choraha','Bherav Temple','Krishna mandir','Press complex','Inox','HDFC Bank','HDFC ATM','SBI ATM','Hanuman mandir','ICICI BANK','Swastik Garden','Om Sweets','Jain Mithai Bhandar','Bherav Mandir', 'Axis Bank','Canara Bank','Girls Hostel','Sai Temple','Rajiv Gandhi College','Rajiv Chok']

cityn=['Mumbai','New Delhi','Culcutta','Bangluru','Hyderabad','Jaipur','Indore','Ahemdabad','Surat','Nagpur','Kanpur','Bhopal','Pune','Vadodara','Noida','Jodhpur','Patna','Ranchi','Goa','Raipur']

starting_number=[62,63,70,72,73,74,75,75,76,77,78,78,79,81,83,87,88,90,90,90,91,91,92,93,93,93,94,94,94,95,95,96,96,97,97,98,98,98,99,99,75]

ginti = int(input("Enter number How many fake contacts you want  "))

for num in range(ginti):
    first=random.choice(first_name)
    last=random.choice(last_name)

    phone = f'+91{random.choice(starting_number)}{random.randint(100,999)}-{random.randint(10000,99999)}'

    street_num=random.randint(10,999)
    street=random.choice(address_place)
    near='Near '+random.choice(nearby)
    city=random.choice(cityn)

    address=f'{street_num},{street},\n{near},\n{city}'
    #print(num+1,'--')
    print(num+1)

    print(f'{first} {last}\n{address}\n{phone}')
    print('\n\n\n')

input("Press Enter to exit")
