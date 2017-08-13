import sys
import matplotlib.pyplot as plt
import numpy as np

def roc_generator(input_file, step, positive_examples, negative_examples):
    threshold = 1.0
    tp_count, fp_count, tn_count, fn_count = 0, 0, 0, 0
    x_axis = []
    y_axis = []
    with open(input_file, 'r') as f:
        for line in f:
            line = line.split()
            if (float(line[2]) >= threshold):
                if (line[3] == "TP"):
                    tp_count += 1
                else:
                    fp_count += 1
            else:
                tn_count = negative_examples - fp_count
                fn_count = positive_examples - tp_count
                sensitivity = tp_count/(tp_count + fn_count)
                specificity = tn_count/(tn_count + fp_count)
                x_axis.append(1 - specificity)
                y_axis.append(sensitivity)
                threshold -= step
    return x_axis, y_axis

def main():
    step = 0.0005
    x_axis = []
    y_axis = []
    positive_examples = 853465
    negative_examples = 40459204
    print("Counting number of true and false positives for each threshold: \n")
    x_axis, y_axis = roc_generator("nc_results_classified_sorted_cut.txt", step, positive_examples, negative_examples)
    print("x_axis: ")
    print(x_axis)
    print("\n y_axis: ")
    print(y_axis)
    print("\n")
    print("ploting ROC curve: \n")
    plt.ylim([0.0, 1.0])
    auc = np.trapz(y_axis,x_axis)
    print(auc)
    plt.plot(x_axis, y_axis)
    plt.show()


main()