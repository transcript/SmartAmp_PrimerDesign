#!/usr/bin/python
# imports:
import operator
import sys

# This lets raw_input do tab completion:
import readline
readline.parse_and_bind("tab: complete")

# SmartAmp primer generator v1
# Initially created 07-08-2014
# Sam Westreich
# OVERALL GOAL: Be able to select a raw sequence, and generate viable SmartAmp primers - no thought required!
###############################

# Part 1: input and checks

print (" ")
print ("This is the primer generator for Smart Amplification, version 1.")
print ("At any time, press CTRL + C to cancel this script.")
print (" ")

print ("The input file must be only the raw bases.  Including flanking sequences, it must be at least 120 bases long to allow for primers to be generated.")
print (" ")

input_file_name = raw_input("Type in the name of the raw text document containing the target sequence and flanking sequences: ")

with open (input_file_name, "r") as myfile:
	raw_seq = myfile.read().replace("\n","")

if raw_seq.strip("GATC"):
	print ("\n File contains characters other than raw bases.")
	sys.exit()
else:
	print ("\n Sequence composition acceptable.\n")

if len(raw_seq) < 120:
	print ("Input sequence needs to be at least 120 characters in length.")
	sys.exit()
elif len(raw_seq) > 2000:
	print ("Your input sequence is greater than 2k bases; this may be too long for SmartAmp PCR.")
	sys.exit()
else:
	print ("Sequence length accepted.\n")
	
# Part 2: gathering all the parts of primers

OP1 = raw_seq[0:14]
print (OP1 + "\n")