import statistics
import csv

GENDER = 0
HEIGHT = 1
WEIGHT = 2

def readnumbertxt(n_file):
	file = open(n_file, 'r')
	numbers = []
	for x in file:
		numbers.append(int(x))
		file.close()
	return numbers

def variance(numbers):
	mean = statistics.mean(numbers)
	total = 0
	for y in numbers:
		total+=((y-mean)**2)
	return total/len(numbers)

def standard_deviation(var):
	return var ** 0.5

def weightheight(wh_file):
	with open(wh_file,'r') as f:
		reader = csv.reader(f)
		next(reader)
		wh = []
		for x in reader:
			wh.append(x)
	return wh

def get_gwh(data):
	gender = []
	height = []
	weight = []
	for d in data:
		height.append(float(d[HEIGHT]))
		weight.append(float(d[WEIGHT]))
		gender.append(d[GENDER])

	return gender, height, weight


data = weightheight("weight-height.csv")

g, h, w  = get_gwh(data)

mean_h = statistics.mean(h)
mean_w = statistics.mean(w)
std_h = standard_deviation(variance(h))
std_w = standard_deviation(variance(w))

counter = 0

def report(counter, stats):
	if anoms[0] == None:
		print("ANOMALY! (%s) > weight: %f" % (','.join(data[counter]),anoms[1]))
	elif anoms[1] == None:
		print("ANOMALY! (%s) > height: %f" % (','.join(data[counter]),anoms[0]))
	else:
		print("ANOMALY! (%s) > height: %f, weight: %f" % (','.join(data[counter]),anoms[1],anoms[0]))

for d in data:
	weight = float(d[WEIGHT])
	height = float(d[HEIGHT])
	anoms = [None,None]

	if  weight > mean_w + (2.5 * std_w) or weight < mean_w - (2.5 * std_w):
		anoms[1]=weight

	if  height > mean_h + (2.5 * std_h) or height < mean_h - (2.5 * std_h):
		anoms[0]=height

	if anoms[0] or anoms[1]:
		report(counter,anoms)

		counter = counter + 1



# ANOMALY! (MALE, 76.4, 122.3) > height: 122.3
# ANOMALY! (MALE, 76.4, 122.3) > weight: 76.4,
# ANOMALY! (MALE, 76.4, 122.3) > weight: 76.4, height: 122.3