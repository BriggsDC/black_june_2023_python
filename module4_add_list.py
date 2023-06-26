
#book_ratings = [7, 9, 5, 6, 8]
#book_ratings.append(4) #Example of someone wanting to give a new book rating of 4; it added a new element to the end of the list. 'Append' is a method, and here it belongs to the 'book_ratings' list. Methods are invoked w/ a '.' dot, after the data theyr'e working on. Without the list, there is no method '.append'
#print(book_ratings)


book_ratings = [7, 9, 5, 6, 8]
book_ratings.insert(1, 10) #This inserts the number 10 at index 1; it inserts the second argument'10' at index '1' the first argument, all other values are shifter right to make room for the new value
print(book_ratings)

