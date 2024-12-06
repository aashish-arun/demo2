class patientManager:
    def __init__(self):
        self.patients = [] 
        self.read_patients_file(self.patients) 
        


    def format_patient_info_for_file(self, patient):
        return f'{patient.pid}_{patient.name}_{patient.disease}_{patient.gender}_{patient.age}'

    def enter_patient_info(self):
        pid = int(input('Enter Patient ID: '))
        name = input('Enter Patient name: ')
        disease = input('Enter Patient disease: ')
        gender = input('Enter Patient gender: ')
        age = int(input('Enter Patient Age: '))

        patient_info = Patient(pid, name, disease, gender, age)
        return patient_info

    def read_patients_file(self, list):
       with open('patients.txt', 'r') as patients_file: 
        patients_data = patients_file.read() 
        patients_data = patients_data.split('\n') 

        for item in patients_data:
            patient_info = item.split('_')
            pid = int(patient_info[0])  
            age = int(patient_info[4])  
            patient_info = Patient(pid, patient_info[1], patient_info[2], patient_info[3], age)
            list.append(patient_info)

    def search_patient_by_id(self):
        pid = int(input('Enter Patient ID: \n')) 
        in_list = False
        
        for patient in self.patients:  
            if patient.pid == pid:  
                self.display_patient_info(patient)
                in_list = True

        if not in_list:
            print("Can't find the Patient with the same id on the system")

    
       
    def display_patient_info(self, patient): 
        print(f"{'ID':<10} {'Name':<20} {'Disease':<10} {'Gender':10} Age")
        print(f"{patient.pid:<10} {patient.name:<20} {patient.disease:<10} {patient.gender:10} {patient.age}")


    def edit_patient_info_by_id(self):
        pid = int(input('Please enter the id of the Patient that you want to edit their information: '))
        for patient in self.patients:
            if patient.pid == pid:
                patient.name = input('Enter new name: ')
                patient.disease = input('Enter new disease: ')
                patient.gender = input('Enter new gender: ')
                patient.age = int(input('Enter new age: '))
                print(f'Patient whose ID is {pid} has been edited')
        

    def display_patients_list(self):
        print(f"{'ID':<10} {'Name':<20} {'Disease':<10} {'Gender':10} Age")
        for patient in self.patients:
            print(f"{patient.pid:<10} {patient.name:<20} {patient.disease:<10} {patient.gender:10} {patient.age}")

        

    def write_list_of_patients_to_file(self):
        with open('patients.txt', 'w') as patients_file:
            for patient in self.patients:
                patients_file.write(self.format_patient_info_for_file(patient) + '\n')
        

    def add_patient_to_file(self):  
        new_patient = self.enter_patient_info() 
        self.patients.append(new_patient)  
        print(f'Patient whose ID is {new_patient.pid} has been added')