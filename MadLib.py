#MadLib.py
#Name: Salsabiel Khair Allah
#Date: August 30
#Assignment: Lab 1
#Purpose: To create a MadLib story where the user provides the words

def main():
  print("Madlib")
  noun1 = ("Enter a noun: ")
  adjective1 = ("Enter an adjective: ")
  verb1 = ("Enter a verb: ")
  adverb1 = ("Enter an adverb: ")
  noun2 = ("Enter another noun: ")
  adjective2 = ("Enter andother adjective: ")
  #Ask user for words

  #Print the story with the user supplied words.
  print("\nHere's your story:\n")
  print("One day, a " + adjective1 + " " + noun1 + " decided to " + verb1 + " " + adverb1 + ".")
  print("It ran into a " + adjective2 + " " + noun2 + " and they became best friends.")



#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
