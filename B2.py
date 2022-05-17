import hashlib
import random

class genome_blockchain:
	def __init__(self, previous_block_hash, genomic_string):
		self.previous_block_hash = previous_block_hash
		self.genomic_string = genomic_string

		self.block_data = genomic_string + "-" + previous_block_hash
		self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()



# list1 = [1, 2, 3]
# Location = random.choice(list1)
Location = 1

data = input("Enter Hash Key: ")

'''
if Location == 1:
	file = open('Storage1.txt', 'a')
	file.write("\n" + data)
	file.close()
	initial_block = genome_blockchain("Initial String", "Storage1.txt")


elif Location == 2:
	file = open('Storage2.txt', 'a')
	file.write("\n" + data)
	file.close()
	initial_block = genome_blockchain("Initial String", "Storage2.txt")


elif Location == 3:
	file = open('Storage3.txt', 'a')
	file.write("\n" + data)
	file.close()
	initial_block = genome_blockchain("Initial String", "Storage1.txt")

'''

with open("Storage1.txt", "r") as file1:
    blockchain = file1.readlines()

n = len(blockchain)
pr_hash = ""
i = 0
while blockchain[n-1][i] != '-':
	pr_hash = pr_hash + blockchain[n-1][i]
	i += 1
block = genome_blockchain(pr_hash, data)

file = open('Storage1.txt', 'a')
file.write("\n"+block.block_hash+"-"+data)
file.close()



''' 
	Instead of string transactions, we will store the transaction type:
		1. STORE the genomic data
		2. Access Genomic Data
	Above thing implemented using a class and different functions for each will be made.

'''