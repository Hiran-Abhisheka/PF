sentence = input("Enter a sentence: ") 
search_term = input("Enter a search term: ")

index = sentence.find(search_term)

if index != -1: 
    print(f"The search term '{search_term}' is found at index position: {index}") 
else: 
    print("Search term not found in the sentence")