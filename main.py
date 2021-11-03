if __name__ == '__main__':
   user_input = input("Please type a sentence with an apostrophe.")
   def split_print_sentence():
       split_result = user_input.split()
       for i in (split_result):
           print(i)
   split_print_sentence()