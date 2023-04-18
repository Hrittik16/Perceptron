'''
PROJECT DETAILS:
bmi.csv -> 30000 rows x 3 cols, it's randomly shuffled, has two classes (Healthy and Unhealthy)
'''

import numpy as np
import pandas as pd

class Perceptron:
	def read_data(self):
		self.data = pd.read_csv('data/bmi.csv')
	def print_data(self):
		print(self.data.head)


if __name__ == '__main__':
	classifier = Perceptron()
	classifier.read_data()
	classifier.print_data()

