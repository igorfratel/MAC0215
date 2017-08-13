def fp_pairs_counter(input_file, k):
	fp_count = 0
	with open(input_file, 'r') as f:
		for line in f:
			line = line.split()
			if (line[3] == "FP"):
				fp_count += 1
				if (fp_count == 100*k):
					return line[0] + " " +line[1]+ " " + line[2]


def main():
	result = fp_pairs_counter("nc_results_classified_sorted.txt", 1577)
	print(result)

main()

	
