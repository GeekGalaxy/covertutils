
from covertutils.crypto.algorithms import *

algo_dict = {
		'null' : NullCyclingAlgorithm,
		'std' : StandardCyclingAlgorithm,
		'crc' : Crc32CyclingAlgorithm,
	}

import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("algorithm", help = 'The algorithm name for use', choices = algo_dict.keys(), type = str, default = 'std' )
parser.add_argument("message", help = "The message to be digested", type = str)
parser.add_argument("--cycles", '-c', help = "The cycles that the algorithm will perform", default = 20, type = int)
parser.add_argument("--length", '-l', help = "The length of the output generated by the algorithm (if it has variable output support)", default = 32, type = int)
# print 'a'
args = parser.parse_args()
# print args
algo = algo_dict[args.algorithm]



res = algo(args.message, args.length, args.cycles).hexdigest()
print( res )
