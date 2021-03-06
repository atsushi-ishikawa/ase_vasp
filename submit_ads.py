import os,sys

# pure metals
# note: no need to do separate calculation for pure metals when making alloy-including database,
#       just set "First=True" flag in alloy part

alloy = True
env = "hokudai" # or "hokudai"

dict = {
  "0"  : {"element" : "Rh" , "lattice" : "fcc" },
  "1"  : {"element" : "Pd" , "lattice" : "fcc" }, 
  "2"  : {"element" : "Ir" , "lattice" : "fcc" }, 
  "3"  : {"element" : "Pt" , "lattice" : "fcc" }, 
  "4"  : {"element" : "Cu" , "lattice" : "fcc" }, 
  "5"  : {"element" : "Ag" , "lattice" : "fcc" }, 
  "6"  : {"element" : "Au" , "lattice" : "fcc" }
}

first = True
# alloy
if alloy:
	for i in range(0,len(dict)):
		element1 = dict[str(i)]["element"]
		for j in range(i+1,len(dict)):
			element2 = dict[str(j)]["element"]

			# --- change by 50% --> gives 21 systems w.o. pure metals
			#for comp1 in range(50,100,50): # start, end, diff

			# --- change by 25% --> gives 63 systems w.o. pure metals
			#for comp1 in range(25,100,25): # start, end, diff

			# --- change by 10%
			#first = False
			#for comp1 in range(10,50,10):  # start, end, diff # part1
			#for comp1 in range(50,100,10): # start, end, diff # part2

			# --- change by 5%
			first = True
			for comp1 in range(5,25,5):   # start, end, diff # part1
			#for comp1 in range(25,50,5):  # start, end, diff # part2
			#for comp1 in range(50,75,5):  # start, end, diff # part3
			#for comp1 in range(75,100,5): # start, end, diff # part4

				if env=="ito":
					command = "pjsub -x \"INP1={0}\" -x \"INP2={1}\" -x \"INP3={2}\" run_kyushu.sh".format(element1,element2,comp1) # PBS
				elif env=="hokudai":
					command = "pjsub -x \"INP1={0}\" -x \"INP2={1}\" -x \"INP3={2}\" run_vasp.sh".format(element1,element2,comp1) # PBS
				os.system(command)

# do pure metal if the loop is first
if first:
	for i in range(0,len(dict)):
		element = dict[str(i)]["element"]
		if env=="ito":
			command = "pjsub -x \"INP1={0}\" run_kyushu.sh".format(element)
		elif env=="hokudai":
			command = "pjsub -x \"INP1={0}\" run_vasp.sh".format(element)
		os.system(command)

