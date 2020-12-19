import sys
import os

def test_a():
	"""
	Dumps sys.path for convenience
	"""
	print()
	print("Cwd", os.getcwd())
	for p in sys.path:
		print("Path", p)
		pass

if __name__ == "__main__":
	test_a()
