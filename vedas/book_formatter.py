import json

def format_book(input_file, output_file):
    bookDict = {}
    # Opens the raw book text file
    with open(input_file, "r") as book_file:
        verse = []
        hymnNum = 1
        completedLine = []
        # Get each line in book_file
        for line in book_file:
            line = line.strip() # Removes whitespace
            if line.isnumeric() and line: # If line is a hymn number
                bookDict[int(line)] = []
                hymnNum = int(line)
                print(hymnNum)
            elif line: # If line contains Sanskrit
                line = line.split("    ")
                verse.append(line)
            else: # If line is whitespace
                formattedLine = ""
                # Goes through previous verse
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
            

format_book("book1.txt", "vedas/books/filtered_book1.json")
#format_book("book2.txt", "vedas/books/filtered_book2.json")
#format_book("book3.txt", "vedas/books/filtered_book3.json")
#format_book("book4.txt", "vedas/books/filtered_book4.json")