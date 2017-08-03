import sys
import os
import matplotlib.pyplot as plt

def nc(input_file, output_file, threshold):
    #Receives the names of input and output files. Runs Neighborhood Correlation with the specified files and threshold
    os.system("NC_standalone -f " + input_file + " --nc_thresh " + str(threshold) + " -o " + output_file)

def true_false_positives(input_file, family_dict):
    #Receives a dictionary "protein:family" and an input_file name.
    #The format of the input_file must be "protein1 protein2 nc_score".
    #For every protein pair in input_file, determines if the proteins in the pair belong to different families or the same family.
    #Pairs where both proteins don't belong to the curated benchmark are ignored.
    #Write to true_false_positives.txt the pairs with their NC-score and posterior classification in tp or fp.
    tp_count = 0
    fp_count = 0
    output_file = open("true_false_positives.txt", w)
    with open(input_file) as f:
        for line in f:
            line = line.split()
            if (line[0] in family_dict):
                if (line[1] in family_dict):
                    if (family_dict[line[0]] == family_dict[line[1]]):
                        tp_count+=1
                        output_file.write(line[0] + " " + line[1] + " " + line[2] + " " + "TP")
                    else:
                        fp_count+=1
                        output_file.write(line[0] + " " + line[1] + " " + line[2] + " " + "FP")
                else:
                    fp_count+=1
                    output_file.write(line[0] + " " + line[1] + " " + line[2] + " " + "FP")
            else if (line[1] in family_dict):
                if (line[0] in family_dict):
                    if (family_dict[line[0]] == family_dict[line[1]]):
                        tp_count+=1
                        output_file.write(line[0] + " " + line[1] + " " + line[2] + " " + "TP")
                    else:
                        fp_count+=1
                        output_file.write(line[0] + " " + line[1] + " " + line[2] + " " + "FP")
                else:
                    fp_count+=1
                    output_file.write(line[0] + " " + line[1] + " " + line[2] + " " + "FP")
    output_file.close()

def true_false_positives_counter(input_file):
    #Sorts input_file(outputed from the true_false_positives function) according to NC-score and counts number of tp and fp pair for each threshold.


#-------------------------------------------(BEGIN) Functions used only for plotting ROC curve------------------------------------
def true_negatives(fp_count, FO_count):
    #Receives the number of possible familyX-familyY pairs and the number of such pairs that appeared in a NC_standalone output.
    #Returns the difference, that is, the true negatives (number of familyX-familyY pairs that did NOT appear in the NC_standalone output).
    return FO_count - fp_count

def false_negatives(tp_count, FF_count):
    #Analogous to the true_negatives function
    return FF_count - tp_count

def sensitivity(tp_count, fn_count):
    #Receives the number of true positives and false negatives.
    #Returns the sensitivity.
    return tp_count/(tp_count + fn_count)

def specificity(tn_count, fp_count):
    #Receives the number of true negatives and false positives.
    #Returns the specificity.
    return tn_count/(tn_count + fp_count)
#-------------------------------------------(END) Functions used only for plotting ROC curve------------------------------------

def main():
    #Command line arguments:
        #input_file -> name of text file containing the BLAST bit-scores for the protein pairs
        #reference_file -> file containing all proteins followed by their families
        #FO_count -> number of familyX-familyY possible pairs
        #FF_count -> number of family-family possible pairs
        #min_threshold -> initial threshold value for executing NC_standalone
        #max_threshold -> maximum threshold value for executing NC_standalone
        #iterations -> number of times that the NC-standalone is executed
    #All NC_standalone outputs are named ROC100_nc_thresh.txt where thresh is the threshold number used in the execution

    input_file = sys.argv[1]
    reference_file = sys.argv[2]
    FO_count = float(sys.argv[3])
    FF_count = float(sys.argv[4])
    min_threshold = float(sys.argv[5])
    max_threshold = 1.0
    iterations = float(sys.argv[7])

    print("Creating dictionary with proteins and their families: \n")
    family_dict = {}
    with open(reference_file) as f:
        for line in f:
            (key, val) = line.split()
            family_dict[key] = val

    output_file_generic = "ROC100_nc_"
    step = (max_threshold - min_threshold)/iterations
    x_axis = []
    y_axis = []
    print("Running NC_standalone with multiple thresholds: \n")
    FF_observed = 0
    output_file = output_file_generic + str(threshold) + ".txt"
    nc(input_file, output_file, min_threshold)
    true_false_positives(output_file, family_dict)
    positives_file = open("true_false_positives.txt", r)
    true_false_positives_counter(positives_file)
    #DAQUI PRA BAIXO É CÓDIGO ANTIGO







    threshold = min_threshold
    while(threshold < max_threshold):
        output_file = output_file_generic + str(threshold) + ".txt"
        nc(input_file, output_file, threshold)
        tp_count, fp_count = true_false_positives(output_file, family_dict)
        FF_observed += tp_count
        threshold += step

        #Lines dedicated to calculate values for the ROC plot
        tn_count = true_negatives(fp_count, FO_count)
        fn_count = false_negatives(tp_count, FF_count)
        temp = 1.0 - specificity(tn_count, fp_count)
        x_axis.append(temp)
        y_axis.append(sensitivity(tp_count, fn_count))

    n = 100*FF_count
    ROC100K  = FF_observed/n*FF_count
    print("RESULT --> The ROC100k score is %f \n" % ROC100K)
    print("x_axis: ")
    print(x_axis)
    print("\n y_axis: ")
    print(y_axis)
    print("\n")
    print("ploting ROC curve: \n")
    #plt.axis([0.0, 1.0, 0.0, 1.0]) #comment this to let axis be free
    #ax = plt.gca() #comment this to let axis be free
    #ax.set_autoscale_on(False) #comment this to let axis be free
    plt.plot(x_axis, y_axis, '-ro')
    plt.show()


main()
