# Problem: Creating a Frequency Counter

# Write a Python function called calculate_frequency that takes a list of words as input and returns a dictionary where the keys are the unique words from the list, and the values are the frequencies of those words in the list.

# {
#     "apple": 3,
#     "banana": 2,
#     "orange": 1,
#     "grape": 1
# }

listOfWords = ["orange","apple","orange","mango","mango","apple","banana","orange"]

def calculate_frequency(list):
    finalDict = {}
    for word in list:
        if word in finalDict:
            finalDict[word] += 1
        else:
            finalDict[word] = 1

    return finalDict

print(calculate_frequency(listOfWords))
        