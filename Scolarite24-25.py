scolarite = {"Maternelle": 100000, "1": 90000,
             "2": 90000, "3": 95000, "4": 95000, 
             "5": 120000, "6": 160000, "7": 120000,
             "8": 120000, "9": 140000, "10": 170000,
             "11": 150000}

inscription = {"Maternelle": 60000, "1": 60000,
             "2": 60000, "3": 60000, "4": 60000, 
             "5": 60000, "6": 60000, "7": 60000,
             "8": 60000, "9": 60000, "10": 60000,
             "11": 60000} 

reinscription = {"Maternelle": 50000, "1": 50000,
             "2": 50000, "3": 50000, "4": 50000, 
             "5": 50000, "6": 50000, "7": 50000,
             "8": 50000, "9": 50000, "10": 50000,
             "11": 50000} 

def mensuel(classe):
    return scolarite[classe]

def trimestriel(classe):
    return scolarite[classe] * 3

def annuel(classe):
    return scolarite[classe] * 9

"""
Scolarite d'une classe pour un nombre de mois
"""
def mois(classe, nbMois=1):
    return scolarite[classe] * nbMois
    
    
    
if __name__ == "__main__":
    choix = ""
    menu = """\tMenu 
    1-Scolarite mensuel
    2-Scolarite trimestriel
    3-Scolarite annuel
    4-Scolarite par nombre de mois
    5-Total Scolarité
    """
    while(choix != "O"):
        print("\n\n***************************************************")
        print(menu)
        
        choix = input("Choix: ").upper()
        if choix == "1":
            classe = input("\nClasse: ")
            print("\nScolarité ==> {}".format(mensuel(classe)))
            print("Scolarité + inscription ==> {}".format(mensuel(classe)+inscription[classe]))
        elif choix =="2":
            classe = input("\nClasse: ")
            print("\nScolarité ==> {}".format(trimestriel(classe)))
            print("Scolarité + inscription ==> {}".format(trimestriel(classe)+inscription[classe]))
        elif choix == "3":
            classe = input("\nClasse: ")
            print("\nScolarité ==> {}".format(annuel(classe)))
            print("Scolarité + inscription ==> {}".format(annuel(classe)+inscription[classe]))
        elif choix == "4":
            classe = input("\nClasse: ")
            nbmois = int(input("Nombre de mois: "))
            print("\nScolarité ==> {}".format(mois(classe, nbmois)))
            print("Scolarité + inscription ==> {}".format(mois(classe, nbmois)+inscription[classe]))
        elif choix == "5":
            students = list()
            studens_number = int(input("Nombre d'élèves: "))

            print("\n")
            i=0
            while i < studens_number:
                classe = input("Classe eleve "+str(i+1)+": ")
                if classe.upper() == "M":
                    classe = "Maternelle"
                
                ins_reins = input("Inscription(1)/Reinscription(2): ")
                nb_mois = int(input("Nombre de mois: "))

                students.append({"classe":classe, "ins_reins":ins_reins, "nb_mois":nb_mois})
                i+=1
            
            print("\n")
            print(students)
            print("\n")

            i=0
            while i < len(students):
                print("{:>8s} |".format("Eleve "+str(i+1)), end=" ")
                i+=1
            
            #Afficher Ins ou Réins
            print("\n")
            for student in students:
                if student["ins_reins"] == "1":
                    print("{:>8s} |".format("Ins"), end=" ")
                elif student["ins_reins"] == "2":
                    print("{:>8s} |".format("Réins"), end=" ")
                
            
            #Scolarité
            print("\n")
            for student in students:
                print("{:>8d} |".format(mois(student["classe"], student["nb_mois"])), end=" ")

            #Inscription/Reinscription
            print("\n")
            for student in students:
                if student["ins_reins"] == "1":
                    print("{:>8d} |".format(inscription[student["classe"]]), end=" ")
                elif student["ins_reins"] == "2":
                    print("{:>8d} |".format(reinscription[student["classe"]]), end=" ")
                
            #Scolarité+Ins/Reins
            print("\n")
            for student in students:
                if student["ins_reins"] == "1":
                    print("{:>8d} |".format(mois(student["classe"], student["nb_mois"])+
                                                    inscription[student["classe"]]), end=" ")
                elif student["ins_reins"] == "2":
                    print("{:>8d} |".format(mois(student["classe"], student["nb_mois"])+
                                                    reinscription[student["classe"]]), end=" ")


            #Total Scolarite   
            print("\n")
            scolarite_sum = sum([mois(student["classe"], student["nb_mois"]) for student in students])
            print("Total Scolarité ==> {}".format(scolarite_sum))

            #Total Inscription   
            print("\n")
            ins_reins_sum = sum([inscription[student["classe"]] for student in students if student["ins_reins"]=="1"] +
                                [reinscription[student["classe"]] for student in students if student["ins_reins"]=="2"])
            print("Total Ins/Réins ==> {}".format(ins_reins_sum))

            #Total Scolarite   
            print("\n")
            print("Scolarité + Ins/Réins==> {}".format(scolarite_sum+ins_reins_sum))

            #Réduction de 5% sur les frais annuels (9 mois)
            test = True
            for student in students:
                if student["nb_mois"] != 9:
                    test = False
                    break
            
            if test == True:
                print("\n\n")
                print("\t----------------------------------")
                reduction = (scolarite_sum*5)/100
                print("Reduction 5% sur scolarité == {}".format(reduction))
                print("Nouvelle Scolarité + Ins/Réins == {}".format((scolarite_sum+ins_reins_sum)-reduction))