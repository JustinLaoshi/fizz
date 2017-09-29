"""
fizz_rnd_list.py
"""

import numpy as np

class Fizz_Rnd_List(object):

	def __init__(self, n):
		"""
		Constructor for the fizz_rnd_list class.

		Parameters: n, or the size of the internal list to be made
		"""
		assert type(n) is int and n > 0, "Please provide an integer greater than 0"
		self.lst = np.random.uniform(0.0, 1.0, n) 							# I chose to use numpy arrays and functions instead of Python's
																			# built-in list because they are much faster performance wise
																			# https://www.scipy.org/scipylib/faq.html#how-can-scipy-be-fast-if-it-is-written-in-an-interpreted-language-like-python
	def get_stats(self, x):
		"""
		Returns y (closest value in self.lst to x), m (index of y), 
		mean of the values in self.lst for indexes [0:m], and the standard 
		deviation of the values in self.lst for indexes [0:m].
		"""
		assert type(x) is float and 0.0 <= x <= 1.0, "Please provide a float between 0.0 and 1.0"
		m = (np.abs(self.lst-x)).argmin()
		y = self.lst[m]
		mean = np.mean(self.lst[:m+1], dtype=np.float64)				# spec says for indexes [0:m], so I did m+1 to include m
		std_dev = np.std(self.lst[:m+1], dtype=np.float64)				# I used the float64 type because I'd figure in a LiDAR application, we'd need max precision
		return y, m, mean, std_dev 

def test():
	"""
	Testing the numpy functions with hard coded values.
	"""
	fizz = Fizz_Rnd_List(5)
	fizz.lst = np.array([0.1, 0.2, 0.3, 0.4, 0.5])
	y, m, mean, std_dev = fizz.get_stats(0.22)
	res = np.array([y, m, mean, std_dev])
	ans = np.array([0.2, 1, 0.15, 0.05])
	np.testing.assert_almost_equal(res, ans)       # this was needed to test due to floating point precision
	print("test passes")


#test() #comment in or out to test
