def count_words(text):
  words_list = text.split()
  return len(words_list)

def count_letters(text):
  letters_dict = {}
  for letter in text.lower():
    if letter in letters_dict:
      letters_dict[letter] += 1
    else:
      letters_dict[letter] = 1
  
  return dict_to_list(letters_dict)

def sort_on(dict):
  return dict["num"]
  
def dict_to_list(dict):
  list = []
  for item in dict:
    if item.isalpha() == False:
      continue
    new_dict = {}
    new_dict["char"] = item
    new_dict["num"] = dict[item]
    list.append(new_dict)
  
  list.sort(reverse=True, key=sort_on)

  return list