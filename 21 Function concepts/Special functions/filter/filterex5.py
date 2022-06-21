#filterex5.py--filter() with anonymous functions

findvowel=lambda k : k in ['a','e','i','o','u']
findcons=lambda k : k not in ['a','e','i','o','u']

#main program
alplst=['b','c','d','e','f','g','h','i','j','k','l','z','y','k','o','i']
print("\nOriginal Alphabets: {}".format(alplst))
print("\nNo. of Alphabets Found={}".format(len(alplst)))
vowels=list(filter(findvowel,alplst))
print("\nVowels List: {}".format(vowels))
print("\nNo. of Vowels Found={}".format(len(vowels)))
print("="*50)
conslst=list(filter(findcons,alplst))
print("\nConsonents List: {}".format(conslst))
print("\nNo. of Consonents Found={}".format(len(conslst)))