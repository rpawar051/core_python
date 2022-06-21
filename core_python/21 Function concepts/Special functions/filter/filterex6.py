#filterex6.py--filter() with anonymous functions

findvowel=lambda k : k in ['a','e','i','o','u']
findcons=lambda k : k not in ['a','e','i','o','u']

def disp(lst):
	print("-"*40)
	for val in lst:
		print("\t{}".format(val))
	print("-"*40)

#main program
alplst=['b','c','d','e','f','g','h','i','j','k','l','z','y','k','o','i']
print("\nOriginal Alphabets:")
disp(alplst)
print("\nNo. of Alphabets Found={}".format(len(alplst)))
vowels=list(filter(findvowel,alplst))
print("\nVowels List:")
disp(vowels)
print("\nNo. of Vowels Found={}".format(len(vowels)))
print("="*50)
conslst=list(filter(findcons,alplst))
print("\nConsonents List: ")
disp(conslst)
print("\nNo. of Consonents Found={}".format(len(conslst)))