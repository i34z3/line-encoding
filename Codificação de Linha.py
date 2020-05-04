import numpy as np
import matplotlib.pyplot as plt


def nrz(vetor):
	for i in range(0,len(vetor)):
		plt.plot([i,i+1], [vetor[i],vetor[i]], 'yo-', color='k')
		if i != 0:
			if vetor[i-1] != vetor[i]:
				plt.plot([i,i], [0,1], 'yo-', color='k')


def nrzl(vetor):
	y = [1 if yn == 0 else -1 for yn in vetor]

	for i in range(0,len(y)):
		plt.plot([i,i+1], [y[i],y[i]], 'yo-', color='k')
		if i != 0:
			if y[i-1] != y[i]:
				plt.plot([i,i], [-1,1], 'yo-', color='k')


def nrzi(vetor):
	pos = 1

	for i in range(0,len(vetor)):
		if vetor[i] == 1:
			plt.plot([i,i], [-1,1], 'yo-', color='k')
			pos = (-1 if pos == 1 else 1)
		plt.plot([i,i+1], [pos,pos], 'yo-', color='k')


def rz(vetor):
	vetor = [1 if yn == 1 else -1 for yn in vetor]
	for i in range(0,len(vetor)):
		if i != 0:
			plt.plot([i,i], [0,vetor[i]], 'yo-', color='k')
		plt.plot([i,i+0.5], [vetor[i],vetor[i]], 'yo-', color='k')
		plt.plot([i+0.5,i+0.5], [vetor[i],0], 'yo-', color='k')
		plt.plot([i+0.5,i+1], [0,0], 'yo-', color='k')
	   

def manchester(vetor):
	for i in range(0,len(vetor)):
		if i != 0 and vetor[i] == vetor[i-1]:
			plt.plot([i,i], [1,-1], 'yo-', color='k')
		if vetor[i] == 0:
			plt.plot([i,i+0.5], [1,1], 'yo-', color='k')
			plt.plot([i+0.5,i+0.5], [1,-1], 'yo-', color='k')
			plt.plot([i+0.5,i+1], [-1,-1], 'yo-', color='k')
		else:
			plt.plot([i,i+0.5], [-1,-1], 'yo-', color='k')
			plt.plot([i+0.5,i+0.5], [1,-1], 'yo-', color='k')
			plt.plot([i+0.5,i+1], [1,1], 'yo-', color='k')
			

def manchester_differential(vetor):
	pos = -1
	for i in range(0,len(vetor)):
		if vetor[i] == 1:
			pos = (-1 if pos == 1 else 1)
		else:
			plt.plot([i,i], [1,-1], 'yo-', color='k')
		if pos == 1:
			if i != 0:
				plt.plot([i,i+0.5], [1,1], 'yo-', color='k')
			plt.plot([i+0.5,i+0.5], [1,-1], 'yo-', color='k')
			plt.plot([i+0.5,i+1], [-1,-1], 'yo-', color='k')
		else:
			if i != 0:
				plt.plot([i,i+0.5], [-1,-1], 'yo-', color='k')
			plt.plot([i+0.5,i+0.5], [1,-1], 'yo-', color='k')
			plt.plot([i+0.5,i+1], [1,1], 'yo-', color='k')
	plt.plot([0,0.5], [-1,-1], color='k')


def ami(vetor):
	pos = 0
	for i in range(0,len(vetor)):
		if vetor[i] == 0:
			plt.plot([i,i+1], [0,0], 'yo-', color='k')
		else:
			if pos == 0:
				plt.plot([i,i], [0,1], 'yo-', color='k')
				plt.plot([i,i+1], [1,1], 'yo-', color='k')
				plt.plot([i+1,i+1], [0,1], 'yo-', color='k')
			else:
				plt.plot([i,i], [0,-1], 'yo-', color='k')
				plt.plot([i,i+1], [-1,-1], 'yo-', color='k')
				plt.plot([i+1,i+1], [0,-1], 'yo-', color='k')
			pos = 0 if pos == 1 else 1


def pseudoternary(vetor):
	vetor = [1 if yn == 0 else 0 for yn in vetor]
	pos = 0
	for i in range(0,len(vetor)):
		if vetor[i] == 0:
			plt.plot([i,i+1], [0,0], 'yo-', color='k')
		else:
			if pos == 0:
				plt.plot([i,i], [0,1], 'yo-', color='k')
				plt.plot([i,i+1], [1,1], 'yo-', color='k')
				plt.plot([i+1,i+1], [0,1], 'yo-', color='k')
			else:
				plt.plot([i,i], [0,-1], 'yo-', color='k')
				plt.plot([i,i+1], [-1,-1], 'yo-', color='k')
				plt.plot([i+1,i+1], [0,-1], 'yo-', color='k')
			pos = 0 if pos == 1 else 1

#NonReturnZero
'''
binario = [1,0,1,1,0]
nrz(binario)
plt.show()
'''

#NonReturnZero-Level
'''
binario = [0,1,0,0,1,1,1,0]
nrzl(binario)
plt.show()
'''

#NonReturnZero-Inverter
'''
binario = [0,1,0,0,1,1,1,0]
nrzi(binario)
plt.show()
'''

#ReturnToZero
'''
binario = [0,1,0,0,1]
rz(binario)
plt.show()
'''

#Manchester
'''
binario = [0,1,0,0,1,1]
manchester(binario)
plt.show()
'''

#ManchesterDiferencial
'''
binario = [0,1,0,0,1,1]
manchester_differential(binario)
plt.show()
'''

#AMI
'''
binario = [0,1,0,0,1,0]
ami(binario)
plt.show()
'''

#Pseudoternário
'''
binario = [0,1,0,0,1,0]
pseudoternary(binario)
plt.show()
'''