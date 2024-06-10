head_zone_A = (0, 2, 6, 8, 12, 14, 16, 18, 20, 24, 26)
succ_zone_A = ("B", "J", "A", "C", "D", "I", "B", "D", "B", "C", "E", "I", "D", "F", "E", "G", "F", "H", "G", "I", "B", "D", "H", "J", "A", "I")

head_7_ponts =  (0, 3, 8, 11, 14)
succ_7_ponts =  (2, 2, 3, 1, 1, 3, 4, 4, 1, 2, 4, 2, 2, 3)

def degreSommetGraphe(head, succ, sommet):
    degre = head[sommet] - head[sommet -1]
    return degre

def voisinsSommetGraphe(head, succ, sommet):
    liste_voisins = succ[head[sommet - 1]:head[sommet]]
    return liste_voisins

print("### Degré des sommets du graphe des 7 ponts de Königsberg ###")
for sommet in range(1, len(head_7_ponts)):
    print("sommet", str(sommet), ":", str(degreSommetGraphe(head_7_ponts, succ_7_ponts, sommet)))
    
print("\n### Voisins des sommets du graphe des 7 ponts de Königsberg ###")
for sommet in range(1, len(head_7_ponts)):
    print("sommet", str(sommet), ":", str(voisinsSommetGraphe(head_7_ponts, succ_7_ponts, sommet)))

print("\n### Degré des sommets du graphe de la Zone A ###")
for sommet in range(1, len(head_zone_A)):
    print("sommet", str(sommet), ":", str(degreSommetGraphe(head_zone_A, succ_zone_A, sommet)))

print("\n### Voisins des sommets du graphe de la Zone A ###")
for sommet in range(1, len(head_zone_A)):
    print("sommet", str(sommet), ":", str(voisinsSommetGraphe(head_zone_A, succ_zone_A, sommet)))

# Dictionnaire
liste_zone_A = {"A": ["B", "J"], 
                "B": ["A", "C", "D", "I"],
                "C": ["B", "D"], 
                "D": ["B", "C", "E", "I"], 
                "E": ["D", "F"], 
                "F": ["E", "G"], 
                "G": ["F", "H"], 
                "H": ["G", "I"], 
                "I": ["B", "D", "H", "J"], 
                "J": ["A", "I"]}

def degreSommetGraphe2(liste, sommet):
    degre = len(liste[sommet])
    return degre

print("### Degré des sommets du graphe de la Zone A ###")
for sommet in liste_zone_A:
    print("sommet", str(sommet), ":", str(degreSommetGraphe2(liste_zone_A, sommet)))

matrix_zone_A = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 1, 1, 0, 0, 0, 0, 1, 0],
                 [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 1, 1, 0, 1, 0, 0, 0, 1, 0],
                 [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                 [0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
]

def voisinsSommetGrapheMatrice(matrice, sommet):
    liste = matrice[sommet]
    voisins = [i for i in range(len(liste)) if liste[i] != 0]
    return voisins

def degreSommetGrapheMatrice(matrice, sommet):
    degre = sum(matrice[sommet])
    return degre

print("### Degré des sommets du graphe de la Zone A ###")
for sommet in range(len(matrix_zone_A)):
    print("sommet", str(sommet+1), ":", str(degreSommetGrapheMatrice(matrix_zone_A, sommet)))

print("\n### Voisins des sommets du graphe de la Zone A ###")
for sommet in range(len(matrix_zone_A)):
    voisins = voisinsSommetGrapheMatrice(matrix_zone_A, sommet)      # on procède en deux temps, car
    print("sommet", str(sommet+1), ":", str([v+1 for v in voisins])) # les indices commencent à 0

def existeCycleEulerien(matrice):                                     
    for sommet in range(len(matrice)):
        
  
if (existeCycleEulerien(matrix_zone_A)):
    print ("Le graphe de la Zone A est eulérien")
else:
    print ("Le graphe de la Zone A n'est pas eulérien")