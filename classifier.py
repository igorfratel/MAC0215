import sys

def protein_pair_classifier(input_file, family_dict):
    #Receives a dictionary "protein:family" and an input_file.
    #The format of the input_file must be "protein1 protein2 nc_score".
    #For every protein pair in input_file, determines if the proteins in the pair belong to different families or the same family.
    #Pairs where both proteins don't belong to the curated benchmark are ignored.
    #Write to true_false_positives.txt the pairs with their NC-score and posterior classification in tp or fp.
    tp_count = 0
    fp_count = 0
    output_file = open("nc_results_classified.txt", 'w')
    with open(input_file, 'r') as f:
        for line in f:
            line = line.split()
            if (line[0] in family_dict):
                if (line[1] in family_dict):
                    if (family_dict[line[0]] == family_dict[line[1]]):
                        tp_count+=1
                        output_file.write(line[0] + " " + line[1] + " " + line[2] + " " + "TP" + "\n")
                    else:
                        fp_count+=1
                        output_file.write(line[0] + " " + line[1] + " " + line[2] + " " + "FP" + "\n")
                else:
                    fp_count+=1
                    output_file.write(line[0] + " " + line[1] + " " + line[2] + " " + "FP" + "\n")
            elif (line[1] in family_dict):
                fp_count+=1
                output_file.write(line[0] + " " + line[1] + " " + line[2] + " " + "FP" + "\n")
            #E se nenhuma delas estiver no dicionario? Eu estou ignorando esses casos
    output_file.close()

def main():
    print("Creating dictionary with proteins and their families: \n")
    family_dict = {}
    with open("curated_set.dat", 'r') as f:
        for line in f:
            (key, val) = line.split()
            family_dict[key] = val
    print("Classifying proteins: \n")
    protein_pair_classifier("nc_results.txt",family_dict)
main()