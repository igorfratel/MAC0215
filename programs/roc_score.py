import sys

def score_generator(input_file):
    T = 853465
    n = 100*1577
    tp_count = 0
    tp_count_temp = 0
    with open(input_file, 'r') as f:
        for line in f:
            line = line.split()
            if (line[3] == "TP"):
                tp_count_temp += 1
            else:
                tp_count += tp_count_temp
    ROC100K = tp_count/n*T
    return ROC100K

def main():
    ROC100K = score_generator("nc_results_classified_sorted_cut.txt")
    print(ROC100K)
    
main()