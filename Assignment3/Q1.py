import os
file_name = input("Enter your file name:")
if os.path.exists(file_name):
    #Count and display the number of words in the file
    counter = 0
    with open(file_name, "r") as f:
        content = f.read()
        m = content.split()
        counter += len(m)
    print("The number of word in file is: ", counter)
    #identify the most frequent word and how many times it appears
    #solving it by using dictionaries
    content_lower = content.lower()
    word_counts = {}
    for word in content_lower:
        if word == " ":
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

    most_frequent_word = ""
    max_count = 0

    for word, count in word_counts.items():
        if count > max_count:
            max_count = count
            most_frequent_word = word
    print(most_frequent_word)
    print(max_count)


else:
    print("File does not exist.")

