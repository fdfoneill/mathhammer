from random import randint

class Die:
	"""A class to represent a multi-sided die"""

	def __init__(self,sides):
		self.sides = sides

	def roll(self, modifier = 0, reroll=None, bestof = None, *args, **kwargs) -> int:
		"""Method to roll the die

		Parameters
		----------
		modifier: int
			Positive or negative modifier to result. Applied after re-rolls
		reroll: list
			List of integer results on which the die should be re-rolled.
		bestof: int
			Roll the die multiple times, return only the highest.

		Returns
		-------
		Integer output of the die roll
		"""
		assert (reroll is None) or (bestof is None)
		result = randint(1,self.sides)

		# handle rerolls
		if reroll is not None:
			if result in reroll:
				result = self.roll(modifier = modifier, *args, **kwargs)

		# handle best-of-multiple-rolls
		elif bestof is not None:
			list_of_results = [result]
			while len(list_of_results) < bestof:
				list_of_results.append(self.roll(*args, **kwargs))
			result = max(list_of_results)

		return result + modifier


class D6(Die):
	"""A class to represent a 6-sided die"""

	def __init__(self):
		super().__init__(sides=6)


class D3(Die):
	"""A class to represent a 3-sided die"""

	def __init__(self):
		super().__init__(sides=3)