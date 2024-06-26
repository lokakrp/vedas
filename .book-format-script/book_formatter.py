import json

def format_book(input_file, output_file):
    bookDict = {}
    # opens the raw book text file
    with open(input_file, "r",encoding="utf-8") as book_file:
        verse = []
        hymnNum = 1
        completedLine = []
        # get each line in book_file
        for line in book_file:
            line = line.strip() # removes whitespace
            if line.isnumeric() and line: # if line is a hymn number
                bookDict[int(line)] = []
                hymnNum = int(line)
                print(hymnNum)
            elif line: #if line contains sanskrit
                line = line.split("    ")
                verse.append(line)
            else: # if line is whitespace
                formattedLine = ""
                # goes through previous verse
                last_letter = ""
                repeat = False
                for count, i in enumerate(verse, 1):
                    letter = i[0][-1]

                    if letter == "a":
                        formattedLine = formattedLine + " " + i[1]
                        if last_letter == "b":
                            repeat = True
                    elif letter == "b":
                        if repeat:
                            formattedLine = formattedLine + " ॥"
                            completedLine.append(formattedLine)
                            bookDict[hymnNum].append(completedLine) 
                            verse = []
                            completedLine = []
                            formattedLine = ""
                            repeat = False
                        else:
                            formattedLine = formattedLine + " " + i[1] + " ।"
                            completedLine.append(formattedLine)
                            formattedLine = ""
                    else:
                        formattedLine = formattedLine + " " + i[1]

                        if count == len(verse):
                            formattedLine = formattedLine + " ॥"
                            completedLine.append(formattedLine)
                            bookDict[hymnNum].append(completedLine) 
                            verse = []
                            completedLine = []
                            formattedLine = ""
                            repeat = False
                    last_letter = letter
                       
                           

        with open(output_file, "w") as target_file:
            json.dump(bookDict, target_file)

# json book format            

#format_book("filtered_book1.txt", "../pages/books/filtered_book1.json")
#format_book("filtered_book2.txt", "../pages/books/filtered_book2.json")
#format_book("filtered_book3.txt", "../pages/books/filtered_book3.json")
#format_book("filtered_book4.txt", "../pages/books/filtered_book4.json")
#format_book("filtered_book5.txt", "../pages/books/filtered_book5.json")
#format_book("filtered_book6.txt", "../pages/books/filtered_book6.json")
#format_book("filtered_book7.txt", "../pages/books/filtered_book7.json")
#format_book("filtered_book8.txt", "../pages/books/filtered_book8.json")
format_book("filtered_book9.txt", "../pages/books/filtered_book9.json")
#format_book("filtered_book10.txt", "../pages/books/filtered_book10.json")
