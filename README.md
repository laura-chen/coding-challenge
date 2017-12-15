# Description
Given a dictionary text file as a command line parameter, anagrams.py prints all the anagrams of a word from user input. 
My algorithm uses two helper functions: make_dict and print_anagrams. 

make_dict is the offline step. It parses the command line arguments and reads in words from the dictionary text file. It converts each word to lowercase, sorts each word, and adds it to an anagrams dictionary (key: sorted word, value: list of anagrams of that key.) Finally, it returns the anagrams dictionary. 

print_anagrams is the online step. It takes in the dictionary we returned from make_dict and prints anagrams of a user-inputted word.While the user has not quit by pressing enter, it reads in a word from standard input. Like in make_dict, it converts the word to lowercase and sorts the word. If the sorted word is a key in the dictionary, then it prints all words in the list. If the sorted word is not in the 
dictionary, we print '-'. 

# Runtime
The offline step takes O(nmlogm + n) time, where n is the number of words in the text file and m is the length of the longest word. make_dict sorts every word using Python's built-in sorted() function, which takes mlogm time. Since we sort all n words, this is a total of O(nmlogm) time. For each word, we also check if it is in the anagrams dictionary and add it it was not present. Adding keys to a hash table is worst-case O(t), where t is the capacity of the underlying array. In case we fill the capacity of the hash table, we would need to grow the capacity of the array and rehash all elements. However, it is amortized O(1) time since we will only have to increase capacity when we reach capacity, so we can say that adding n words to the anagrams dictionary takes O(n) time. The total runtime for the offline step is thus O(nmlogm + n). 

The online step takes O(nmlogm + nl) time, where n is the number of words the user inputs, m is the length of the longest word, and l is the length of the longest anagram list. We sort every word, which is O(mlogm) as explained above. We also check if the word is in the dictionary, which is amortized O(1) time. If the word is a key in the dictionary, we iterate through the value (a list). If we call the length of the longest list l, then printing anagrams for all words takes O(nl) time. So the total runtime of the online step is O(nmlogm + nl). 

# Memory
The offline step takes O(n) space, where n is the number of words in the text file. We add every word in the text file to the anagrams dictionary.

The online step takes O(1) space. We do not use additional storage. We just check if the user's word is in the anagrams dictionary. 

# Other
I decided to use two helper functions, one for the offline step and one for the online step, to improve readability and clarity of the code. 
