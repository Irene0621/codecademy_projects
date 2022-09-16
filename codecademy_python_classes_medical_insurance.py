#!/usr/bin/env python
# coding: utf-8

# In this codecademy proyect we created a system to organize patient data using a class in python.
# This class call Patient takes patient parameters such as name, age, sex, bmi, num_of_children and if the patient smokes or not. We use methods like update_age and update_num_of_children to easily update patients parameters. This class orders the patient information in dictionaries using patient_profile method and gives information about the estimated insurance cost of a patient.

# In[1]:


class Patient:
    def __init__(self, name, age, sex, bmi, num_of_children, smoker):
        self.name = name
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.num_of_children = num_of_children
        self.smoker = smoker
    # This method calculate the estimated insurance cost
    def estimated_insurance_cost(self):
        estimated_cost = 250 * self.age - 128 * self.sex + 370 * self.bmi + 425 * self.num_of_children + 24000 * self.smoker - 12500
        print(self.name+ "'s estimated insurance costs is " + str(estimated_cost) + " dollars.")
    # This method help us update the age of our patient
    def update_age(self, new_age):
        self.age = new_age
        print(self.name + " is now " + str(self.age) + " years old.")
        self.estimated_insurance_cost()
    # This method help us update the number of children of our patient
    def update_num_of_children(self, new_num_children):
        self.num_of_children = new_num_children
        if self.num_of_children == 1:
            print(self.name + " has " + str(self.num_of_children) + " child.")
        else:
            print(self.name + " has " + str(self.num_of_children) + " children.")
    # This method help us organize patient information in dictionaries
    def patient_profile(self):
        patient_information = {}
        
        patient_information["Name"] = self.name
        patient_information["Age"] = self.age
        patient_information["Sex"] = self.sex
        patient_information["BMI"] = self.bmi
        patient_information["Number of Children"] = self.num_of_children
        patient_information["Smoker"] = self.smoker
        return patient_information
    
patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0)
patient1.update_age(50)
patient1.update_num_of_children(1)
patient1.estimated_insurance_cost()
patient1.patient_profile()

