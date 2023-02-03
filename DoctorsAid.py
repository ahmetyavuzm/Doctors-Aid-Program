# Ahmet Yavuz Mutlu 2210356014

def create():
    """This function add a new patient in all patients 
    list and writes some feedback in output file"""
    global patient_list, patient_data
    if patient_data not in patient_list:
        patient_list.append(patient_data)
        output_function(f"Patient {patient_data[0]} is recorded. \n")
    else:
        output_function(f"Patient {patient_data[0]} cannot be recorded due to duplication. \n")     

def remove():
    """This function remove the patient that users want in all
     patients list and writes some feedbacks in output file"""
    global patient_list, patient_data
    for i in range(len(patient_list)): 
        if patient_data[0] == patient_list[i][0]:
            patient_list.pop(i)
            output_function(f"Patient {patient_data[0]} is removed. \n")
            break
        elif i == (len(patient_list)-1):
            output_function(f"Patient {patient_data[0]} cannot be removed due to absence. \n")

def list():
    """This function, writes all patients datas 
    as a table form in a output file"""
    global patient_list, patient_data
    output_function("Patient\tDiagnosis\tDisease\t\t\tDisease\t\tTreatment\t\tTreatment\n"+
                            "Name\tAccuracy\tName\t\t\tIncidence\tName\t\t\tRisk\n"+"-"*73+"\n")
    total_char = [8,12,16,12,16,0]
    for i in range(len(patient_list)):
        for j in range(6):
            tab_num = (total_char[j] -len(patient_list[i][j]))//4 + 1 
            if (total_char[j] -len(patient_list[i][j]))%4 == 0 : tab_num += -1
            if j == 1:
                # In the bottom three lines if the decimal part has one number after the roundation operation, we add "0", if it is not we don't add anything.
                if len(str(round(float(patient_list[i][j])*100,2))) <5 : zero ="0"
                else : zero =""
                text = f"{round(float(patient_list[i][j])*100,2)}{zero}%"
            elif j == 5: text = f"{round(float(patient_list[i][j])*100)}%"
            else: text = patient_list[i][j]
            output_function((text+"\t"*tab_num))
        output_function("\n")

def patient_probability_function():
    """This function calculates the probability that 
    the patient has cancer based on the test results."""
    global patient_list, patient_data
    for i in range(len(patient_list)):
        if patient_data[0] in patient_list[i]:
            diagnosis_accuracy = float(patient_list[i][1])
            diev = patient_list[i][3].split("/") # diev : disease incedence elements values
            diev[0], diev[1] = int(diev[0]), int(diev[1])
            # With using Bayer's Theorem, function calculates patient's probability
            probability_value =(diev[0]*diagnosis_accuracy) / ((diagnosis_accuracy*diev[0])+(diev[1]-diev[0])*(1-diagnosis_accuracy))
            cancer_type = patient_list[i][2] 
            return probability_value , cancer_type

def probability(patient_data_values):
    """This function, writes the result of the patients
    probability of being cancer in a output file"""
    global patient_data
    if patient_data_values != None:
        if round(patient_data_values[0]*10000)%100 == 0 : probability_persentage = round(patient_data_values[0]*100)
        else : probability_persentage = round(patient_data_values[0]*100,2) 
        output_function(f"Patient {patient_data[0]} has a probability of {probability_persentage}% of having {patient_data_values[1].lower()}.\n")
    else: output_function(f"Probability for {patient_data[0]} cannot be calculated due to absence. \n")

def recommendation(patient_probability):
    """This function gives a recommendation on whether
    the desired patient should be treated or not."""
    global patient_data, patient_list
    for i in range(len(patient_list)):
        if patient_data[0] in patient_list[i]:
            patient_treatmet_risk = float(patient_list[i][5])
            if patient_treatmet_risk > patient_probability[0]:
                output_function(f"System suggests {patient_data[0]} NOT to have the treatment. \n")
                break
            else:
                output_function(f"System suggests {patient_data[0]} to have the treatment. \n") 
                break   
        elif i == (len(patient_list)-1):
            output_function(f"Recommendation for {patient_data[0]} cannot be calculated due to absence \n")

def output_function(a_text):
    outputs_text_file.write(a_text)

def input_function(input_file_name):
    """This function reads the text file containing the inputs, parses the entered data,
    performs the operations requested by the user, and prints the outputs to a text file."""
    global patient_data, all_inputs
    all_inputs = open(input_file_name, "r")
    all_inputs = all_inputs.readlines()
    for line in all_inputs:
        try:
            first_space_chracter = line.index(" ")
            function_name = line[:first_space_chracter]
            patient_data = line[first_space_chracter+1:].rstrip("\n").split(", ")
        except:
            function_name = line.rstrip("\n")
        if function_name == "create" : create()
        elif function_name == "remove" : remove()
        elif function_name == "list" : list()
        elif function_name == "probability" : probability(patient_probability_function())
        elif function_name == "recommendation" : recommendation(patient_probability_function())

patient_list , patient_data = [], []
outputs_text_file = open("doctors_aid_outputs.txt", "w")
input_function("doctors_aid_inputs.txt")
outputs_text_file.close()