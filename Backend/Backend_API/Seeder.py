from faker import Faker
from Users.models import User
from Users.models import Roles
from Users.models import User_Roles
from Users.models import Patient_User
from Users.models import Psychologist_User
from Users.models import Diagnosis
from Activities.models import *
from ActivitySeeder import get_activity
from MoodsSeeder import get_mood
from Moods.models import *
import hashlib


fake = Faker() 

def seed_db(num_entries=10, overwrite=True):
    deleteAllData()

    seed_roles()

    pkAdmin = Roles.objects.filter(role_name="ADMIN").get()
    pkPsyc = Roles.objects.filter(role_name="PSYCHOLOGIST").get()
    pkPatient = Roles.objects.filter(role_name="PATIENT").get()
    
    seed_user(num_entries, overwrite, pkAdmin, pkPsyc, pkPatient)
    seed_activities() 
    seed_moods()

def deleteAllData():
    Proof_Activities_Type.objects.all().delete()
    Activity_Types.objects.all().delete()

    Generic_Moods.objects.all().delete()
    Patient_Mood.objects.all().delete()

    User_Roles.objects.all().delete()
    Roles.objects.all().delete()
    
    Psychologist_User.objects.all().delete()
    Patient_User.objects.all().delete()
    Diagnosis.objects.all().delete()

    User.objects.all().delete()


    
def seed_roles():
    print("Overwriting Roles")
    Roles.objects.all().delete()
    r = Roles(role_name = "ADMIN")
    r.save()
    r = Roles(role_name = "PSYCHOLOGIST")
    r.save()
    r = Roles(role_name = "PATIENT")
    r.save()
    print("Done writing roles")

def seed_user(num_entries, overwrite, pkAdmin, pkPsyc, pkPatient):
    if overwrite:
        print("Overwriting users")
        User.objects.all().delete()
        count = 0 

        # Used to store the most recent psychologist that has been read so that 
        # the users before a new psychologist can be assigned to this psychologist
        currentPsychologist = None

        for _ in range(num_entries):
            # Create data for user
            usrname = fake.first_name() if count != 0 else 'a'
            print(usrname)
            email = fake.email()
            pssw = fake.password(length=15) if count != 0 else 'a'
            encrpyted_pass = hashlib.sha256((pssw).encode()).hexdigest() 
            title = fake.prefix()
            first_name= fake.first_name()
            surname = fake.last_name()
            cell = fake.phone_number()
            Da_OB = fake.date_of_birth() 
            gender = 'M' if count % 2 == 1 else 'F'
            prim_adress = fake.address()
            city = fake.city()
            postal_code = fake.postcode()
            country = fake.country()
            citizenship = fake.country()
            is_inactive = fake.boolean(chance_of_getting_true=50)
            created_at = fake.date()
            updated_at = created_at

            if count == 0:
                user_pass = open("all_users.txt","w+")
            else:
                user_pass = open("all_users.txt","a")

            # for _ in range(num_entries):
            user_pass.write("username " + usrname + " pass " + pssw+ " " + "\n")
            user_pass.close()

            u = User(
                username = usrname,
                email_address = email,
                password = encrpyted_pass,
                title = title,
                first_name = first_name,
                surname = surname,
                cell_number = cell,
                date_of_birth =  Da_OB,
                gender = gender,
                primary_address =  prim_adress,
                city = city,
                postal_code =  postal_code,
                country =  country,
                citizenship = citizenship,
                is_inactive = is_inactive,
                created_at = created_at,
                updated_at =  updated_at
            )  # Create new User
            # used to calculate progress
            count += 1 
            percent_complete = count / num_entries * 100
            print("Adding {} new Users: {:.2f}%".format(num_entries, percent_complete))
            print()
            u.save()

            # set first user to an admin
            if(count==0):
                ur = User_Roles(
                        user = u,
                        role = pkAdmin
                    )
                ur.save()
            else:
                print(pkAdmin) 
                # random number 
                rndNum = fake.random_digit()
                if rndNum >= 0 and rndNum <= 3 and currentPsychologist != None: # rand number between 0 and 3
                    # create patient user role
                    ur = User_Roles(
                        user = u,
                        role = pkPatient
                    )
                    ur.save()

                    # create a diagnosis for the patient
                    diagnosis = Diagnosis(
                        name = fake.first_name(),
                        description = fake.last_name()
                    )
                    diagnosis.save()

                    # create patient user
                    patientUser = Patient_User(
                        user = u,
                        psychologist = currentPsychologist,
                        diagnosis = diagnosis
                    )
                    patientUser.save()

                elif rndNum >= 4 and rndNum <= 6 and currentPsychologist != None: # rand number between 4 and 6
                    # create admin user role
                    ur = User_Roles(
                        user = u,
                        role = pkAdmin
                    )
                    ur.save()
                elif rndNum >= 7 and rndNum <= 9 or currentPsychologist == None: # rand number between 7 and 9
                    # create psychologist user role
                    ur = User_Roles(
                        user = u,
                        role = pkPsyc
                    )
                    ur.save()

                    # create a psychologist user
                    psychologistUser = Psychologist_User(
                        user = u,
                        practitioners_id = fake.random_digit(),
                        practice_address = fake.address(),
                        practice_work_number = fake.phone_number(),
                        practice_email = fake.email()
                    )
                    psychologistUser.save()
                    
                    # set the current psychologist to the user that has just been added
                    currentPsychologist = psychologistUser
            print("Serializing Data")
        print()

def seed_activities():
    # Proof of activities 
  
    PA = Proof_Activities_Type(name = "IMAGE")
    PA.save() 
    PA = Proof_Activities_Type(name = "DOCUMENT")
    PA.save() 
    PA = Proof_Activities_Type(name = "PHONE")
    PA.save() 

    # Get different types of proofs 
    pkImg = Proof_Activities_Type.objects.filter(name="IMAGE").get()
    pkDoc = Proof_Activities_Type.objects.filter(name="DOCUMENT").get()
    pkPhone = Proof_Activities_Type.objects.filter(name="PHONE").get()
    
    # Activity types

    AT  = Activity_Types(name= "PHYSICAL")
    AT.save() 
    AT  = Activity_Types(name= "MENTAL")
    AT.save() 
    AT  = Activity_Types(name= "SELF_IMPROVEMENT")
    AT.save()

    #Get different Activity Types 
    pkPhys = Activity_Types.objects.filter(name="PHYSICAL").get()
    pkMental = Activity_Types.objects.filter(name="MENTAL").get()
    pkSImp = Activity_Types.objects.filter(name="SELF_IMPROVEMENT").get()
        

    role = Roles.objects.filter(role_name = 'PATIENT').values() 
    # roleid = role.values('role_id') 
    roleid = role.values('role_id').get()
    roleid = roleid.get('role_id')
    pu = User_Roles.objects.filter(role_id = roleid).values('user_id')  # Return a list of only userid's
    # for i in pu : print(i.get('userid_id'))  

    dict = [] 
    for i in pu :
        dict.append(i.get('user_id')) 
    print(dict)
    patients= open("patient_id.txt","w+")
     
    for uid in dict:
        patients.write(str(uid) + "\n")
        usr = User.objects.get(user_id = uid)
        patientUsr = Patient_User.objects.get(user = usr)
        # PT = Proof_Activities_Type.objects
        # Get Random activity 
        rndNum = fake.random_digit()
        if rndNum >= 0 and rndNum <= 3 :
            A = Activities(
                activity_name = get_activity(), 
                activity_description = 'You are tasked to perform the following blah blah ',
                proof_type = pkImg,
                activity_type = pkPhys,
            )
            A.save()
            AA = Assigned_Activities(
                activity = A,
                patient = patientUsr,
                due_date = fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None),
                description = 'You are tasked to perform the following blah blah ',
                isCompleted = fake.random_int(0,1)
            )
            AA.save()
            PrA = Proof_Activities(
                filename = fake.file_name(category=None, extension=None),
                pathname = fake.file_path(depth=1, category=None, extension=None)
            )
            PrA.save()
            CA = Completed_Activities(
                completed_activities = AA, 
                completion_date = fake.date_time_this_year(before_now=False, after_now=False, tzinfo=None),
                proof = PrA
            )
            CA.save() 
        elif rndNum >= 4 and rndNum <= 6 :
            A = Activities(
                activity_name = get_activity(), 
                activity_description = 'You are tasked to perform the following blah blah ',
                proof_type = pkDoc,
                activity_type = pkMental,
            )
            A.save()
            AA = Assigned_Activities(
                activity = A,
                patient = patientUsr,
                due_date = fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None),
                description = 'You are tasked to perform the following blah blah ',
                isCompleted = fake.random_int(0,1)
            )
            AA.save()
            PrA = Proof_Activities(
                filename = fake.file_name(category=None, extension=None),
                pathname = fake.file_path(depth=1, category=None, extension=None),
            )
            PrA.save()
            CA = Completed_Activities(
                completed_activities = AA, 
                completion_date = fake.date_time_this_year(before_now=False, after_now=False, tzinfo=None),
                proof = PrA
            )
            CA.save()
        elif rndNum >= 7 and rndNum <= 9:
            A = Activities(
                activity_name = get_activity(), 
                activity_description = 'You are tasked to perform the following blah blah ',
                proof_type = pkPhone,
                activity_type = pkSImp,
            )
            A.save()
            AA = Assigned_Activities(
                activity = A,
                patient = patientUsr,
                due_date = fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None),
                description = 'You are tasked to perform the following blah blah ',
                isCompleted = fake.random_int(0,1)
            )
            AA.save()
            PrA = Proof_Activities(
                filename = fake.file_name(category=None, extension=None),
                pathname = fake.file_path(depth=1, category=None, extension=None)
            )
            PrA.save()
            CA = Completed_Activities(
                completed_activities = AA, 
                completion_date = fake.date_time_this_year(before_now=False, after_now=False, tzinfo=None),
                proof = PrA
            )
            CA.save()

    print("Serializing Data")
    patients.close()


def seed_moods():
    General_Mood = ['Happy', 'Sad', 'Excellent','Meh', 'Angry']
    for mood in General_Mood:
        GM = Generic_Moods(name = mood)
        GM.save()


    role = Roles.objects.filter(role_name = 'PATIENT').values() 
    # roleid = role.values('role_id') 
    roleid = role.values('role_id').get()
    roleid = roleid.get('role_id')
    pu = User_Roles.objects.filter(role_id = roleid).values('user_id')  # Return a list of only userid's
    # for i in pu : print(i.get('userid_id'))  

    dict = [] 
    for i in pu :
        dict.append(i.get('user_id')) 
    print(dict)
    for uid in dict:
        usr = User.objects.get(user_id = uid)
        patientUsr = Patient_User.objects.get(user = usr)
        # PT = Proof_Activities_Type.objects
        # Get Random activity 
        rndNum = fake.random_digit()
        GM = Generic_Moods.objects.filter(name = General_Mood[fake.random_int(0, len(General_Mood)-1)]).get()
        if rndNum >= 0 and rndNum <= 3 :
            PM = Patient_Mood(
                generic_mood = GM, 
                patient = patientUsr,
                logged_time = fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None),
                description = "{} because I did blah blah blah during this day ".format(GM.name)
            )
            PM.save()
        elif rndNum >= 4 and rndNum <= 6 :
           
            
            PM = Patient_Mood(
                generic_mood = GM, 
                patient = patientUsr,
                logged_time = fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None),
                description = "{} because I did blah blah blah during this day ".format(GM.name)
            )
            PM.save()
        elif rndNum >= 7 and rndNum <= 9:
        
            PM = Patient_Mood(
                generic_mood = GM, 
                patient = patientUsr,
                logged_time = fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None),
                description = "{} because I did blah blah blah during this day ".format(GM.name)
            )
            PM.save()
         

