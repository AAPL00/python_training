list_of_subjects = []
while True:
    print("Do you wat to add a subject? Type Yes or No")
    interrogation = input()
    if  interrogation == "Yes":
        list_of_subjects.append(input("Introduce the subject\n"))
    elif interrogation == "No":
        break
    else:
        print("What do you mean?")
for subject in list_of_subjects:
    score = int(input("Introduce your score in " + subject + "\n"))
    if score > 2:
        print("Estuve aqui")
        list_of_subjects.remove(subject)
reprobed_subjects = "You reprobed"
for subject in list_of_subjects:
    reprobed_subjects += (" " + subject)
print(reprobed_subjects)    
    
    
