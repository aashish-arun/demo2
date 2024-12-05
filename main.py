class DoctorManager:
    def __init__(self):
        self.doctors= [] #empty list of doctors
        self.read_doctors_file()

    def format_dr_info(self, doctor):
        format_doctor= doctor.__str__() #Formats Doctor object similar to that of the doctors file
        return format_doctor
        

    def enter_dr_info(self):# Asks for the doctor_id, name, specialization and other parameters of the Doctor object to create
        doctor_id= int(input("Enter Doctor ID: ")) 
        name= input("Enter Doctor Name: ") 
        specialization= input("Enter specialization: ") 
        working_time= input("Enter Doctor working_time: ")
        qualification= input("Enter Doctor Qualification: ")
        room_number= input("Enter Doctor room_number: ")
        new_dr= Doctor(doctor_id, name, specialization, working_time, qualification, room_number)
        return new_dr
    
    def read_doctors_file(self): #opens the doctors file, reads it creates Doctor objects for each doctor and iterates it to the self.doctor list

        with open("doctors.txt", "r") as doctors_file: #opening the doctors file
            doctors_data= doctors_file.read()
            doctors_data= doctors_data.split("\n") #separating lines of the file to group data int doctor objects
            
            for data in doctors_data [1:]: 
                dr_info = data.split("_") #dividing each line furthermore to extract different paraneters for doctor object
                dr_id= int(dr_info[0])
                dr_room_number= int(dr_info[5])
                doctors= Doctor(dr_id, dr_info[1], dr_info[2], dr_info[3], dr_info[4], dr_room_number) # creating doctor object
                self.doctors.append(doctors) #adds doctor objects to the self.doctors list
    
    def search_dr_by_id(self): #looks for a doctor in the self.doctors list with a corresponding id and displays it
        dr_id= int(input("Enter Doctor ID: "))
        found =False
        
        for doctors in self.doctors:
            if doctors.doctor_id == dr_id: #moves through the list looking for doctor object with corresponding id      
                print(f"{'ID':<5} {'Name':<23} {'specialization':<16} {'working_time':<16} {'Qualification':<16}Room Number\n")
                print(self.diplay_doctor_info(doctors)) #outputs the doctor information if found
                found= True
        
        if not found:
            print ("Cannot find the doctor") #outputs message if not found and displays it

    def search_dr_by_name(self): #looks for a doctor in the self.doctors list with a corresponding name
        dr_name= input("Enter Doctor Name: ")
        found =False
        
        for doctors in self.doctors:
            if doctors.name == dr_name: #moves through the self.doctors list looking for doctor object with corresponding name
                print(f"{'ID':<5} {'Name':<23} {'specialization':<16} {'working_time':<16} {'Qualification':<16}Room Number\n")
                print(self.diplay_doctor_info(doctors)) #displays the doctor information with corresponding name if found
                found= True
       
        if not found:
            print ("Cannot find the doctor") #outputs this message if not found
    
    def diplay_doctor_info(self, doctor): #formats the doctor objectcontent in such a way that it is output in a tabular format
        return f"{doctor.doctor_id:<5} {doctor.name:<23} {doctor.specialization:<16} {doctor.working_time:<16} {doctor.qualification:<16}{doctor.room_number}"
    
    def edit_doctor_file(self): # looks for doctor object by ID in the self.doctors list edits the information and replaces it both in the list and the doctors file 
        id= int(input("Enter The Doctor ID: "))
        found= False
        
        for doctors in self.doctors: #loops through the list looking for a corresponding id and calls in setters of the doctor object to change the information
            if doctors.doctor_id == id:
                new_name= input("Enter Doctor's Name: ")
                new_specialization= input("Enter Doctor's specialization: ")
                new_time= input("Enter Doctor's working_time: ")
                new_qualification= input("Enter Doctor's Qualification: ")
                new_room= int(input("Enter Doctor's Room number: ")) 
                doctors.set_name(new_name)
                doctors.set_specialization(new_specialization)
                doctors.set_working_time(new_time)
                doctors.set_qualification(new_qualification)
                doctors.set_room_number(new_room)
                self.write_list_of_doctors_to_file() #rewrites the whole textfile with the new and editted doctors to keep it up to date
                print (f"Doctor whose id is {id} ha been edited") #outputs this message if the editing was successful
                found= True
                break
        if not found:
            print("Cannot find the doctor") #outputs this message if it fails

    def display_doctors_list(self): #formats all the information in the self.doctors list in a table format
        print(f"{'ID':<5} {'Name':<23} {'specialization':<16} {'working_time':<16} {'Qualification':<16}Room Number\n")
        for doctors in self.doctors:
            print(self.diplay_doctor_info(doctors)+"\n")

    def write_list_of_doctors_to_file(self): # Writes all the doctor objects in the doctors file in the format it was originally in but with the new data
        with open("doctors.txt", "w") as write_list:
            write_list.write(f"id_name_specilist_working_time_qualification_roomNb\n")
            for doctors in self.doctors:
                final_doctors=self.format_dr_info(doctors)
                write_list.write(f"{final_doctors}\n")
    
    def add_dr_to_file(self): # This appends a newly created Doctor object into both the list and the doctors file
        add_doctor= self.enter_dr_info()
        self.doctors.append(add_doctor) #appends info to the list
        with open("doctors.txt", "a") as dr_add:
            dr_add.write(f"\n{self.format_dr_info(add_doctor)}") #appends info to the doctors file