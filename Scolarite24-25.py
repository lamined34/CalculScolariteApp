scolarite = {"Maternelle": 100000, "1": 90000,
             "2": 90000, "3": 95000, "4": 95000, 
             "5": 120000, "6": 160000, "7": 120000,
             "8": 120000, "9": 140000, "10": 170000,
             "11": 150000, "12": 150000}

inscription = {"Maternelle": 60000, "1": 60000,
             "2": 60000, "3": 60000, "4": 60000, 
             "5": 60000, "6": 60000, "7": 60000,
             "8": 60000, "9": 60000, "10": 60000,
             "11": 60000, '12': 60000} 

reinscription = {"Maternelle": 50000, "1": 50000,
             "2": 50000, "3": 50000, "4": 50000, 
             "5": 50000, "6": 50000, "7": 50000,
             "8": 50000, "9": 50000, "10": 50000,
             "11": 50000, "12": 50000} 

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

            #Gestion de l'affichage console

            #Entête Eleve, Eleve1, etc
            print("{:>15s} |".format(""), end=" ") #Libéllé Eleve
            i=0
            while i < len(students):
                print("{:>10s} |".format("Eleve "+str(i+1)), end=" ")
                i+=1

            print("{:>10s} |".format(""), end=" ")
            print("\n")

            #Afficher La classe de l'élève
            print("{:>15s} |".format("Classe"), end=" ") #Libéllé Classe
            for student in students:
                print("{:>10s} |".format(student["classe"] + 'e A'), end=" ")
            
            print("{:>10s} |".format("Total"), end=" ")
            print("\n")

            #Afficher Catégories (Ins ou Réins)
            print("{:>15s} |".format("Catégories"), end=" ") #Libéllé Catégories
            for student in students:
                if student["ins_reins"] == "1":
                    print("{:>10s} |".format("Ins"), end=" ")
                elif student["ins_reins"] == "2":
                    print("{:>10s} |".format("Réins"), end=" ")

            print("{:>10s} |".format(""), end=" ")
            print("\n")   
            
            #Scolarité
            print("{:>15s} |".format("Scolarité"), end=" ") #Libéllé Scolarité
            for student in students:
                print("{:>10d} |".format(mois(student["classe"], student["nb_mois"])), end=" ")  

            scolarite_sum = sum([mois(student["classe"], student["nb_mois"]) for student in students]) #Total Scolarité 
            print("{:>10d} |".format(scolarite_sum), end=" ")      
            print("\n")


            #Inscription/Reinscription
            print("{:>15s} |".format("Ins / Réins"), end=" ") #Libéllé Ins / Réins
            for student in students:
                if student["ins_reins"] == "1":
                    print("{:>10d} |".format(inscription[student["classe"]]), end=" ")
                elif student["ins_reins"] == "2":
                    print("{:>10d} |".format(reinscription[student["classe"]]), end=" ")

            ins_reins_sum = sum([inscription[student["classe"]] for student in students if student["ins_reins"]=="1"] +
                                [reinscription[student["classe"]] for student in students if student["ins_reins"]=="2"]) #Total Ins/Réins
            print("{:>10d} |".format(ins_reins_sum), end=" ")  
            print("\n")

                
            #Scolarité+Ins/Reins => Total
            print("{:>15s} |".format("Total"), end=" ") #Libéllé Total par colonne
            
            for student in students:
                if student["ins_reins"] == "1":
                    print("{:>10d} |".format(mois(student["classe"], student["nb_mois"])+
                                                    inscription[student["classe"]]), end=" ")
                elif student["ins_reins"] == "2":
                    print("{:>10d} |".format(mois(student["classe"], student["nb_mois"])+
                                                    reinscription[student["classe"]]), end=" ")
                    
            
            print("{:>10d} |".format(scolarite_sum+ins_reins_sum), end=" ")  
            print("\n")


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

        
            #Réduction plus de 4 ou payment annuelle
            #Determine le type de réduction
            typeReduction: str = ''
            
            typeNeufMois: bool = True
            for student in students:
                if student['nb_mois'] != 9:
                    typeNeufMois = False
                    break

            typePlusDeQuatre: bool = False
            typePlusDeQuatre = len(students) >= 5

            
            if typeNeufMois:
                typeReduction = 'neufMois'
            elif typePlusDeQuatre:
                typeReduction = 'plusDeQuatre'

            #Calcul de la reduction en fonction du type
            reduction: float = 0.
            if typePlusDeQuatre == True and typeNeufMois == True:
                print("\n\n")
                print("\t----------------------------------")
                print("\tRéduction des frais de scolarité\n")
                reduction = (scolarite_sum*5)/100
                print("Reduction 5% sur scolarité = {}".format(reduction))
                print("Nouvelle Scolarité = {}".format(scolarite_sum-reduction))
                print("Nouvelle Scolarité + Ins/Réins = {}".format((scolarite_sum+ins_reins_sum)-reduction))
            elif typeReduction == 'neufMois':
                print("\n\n")
                print("\t----------------------------------")
                print("\tRéduction dû au paiment annuelle\n")
                reduction = (scolarite_sum*5)/100
                print("Reduction 5% sur scolarité = {}".format(reduction))
                print("Nouvelle Scolarité = {}".format(scolarite_sum-reduction))
                print("Nouvelle Scolarité + Ins/Réins ={}".format((scolarite_sum+ins_reins_sum)-reduction))
            elif typeReduction == 'plusDeQuatre':
                print("\n\n")
                print("\t----------------------------------")
                print("\tRéduction dû au fait d'avoir plus de 4 enfants\n")
                sumScolMensuel: float = 0.
                for student in students:
                    sumScolMensuel += scolarite[student['classe']]
                reduction = ((sumScolMensuel*9)*5)/100
                
                print("Reduction 5% sur scolarité = {}".format(reduction))
                


