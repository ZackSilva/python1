if __name__ == '__main__':
   user_input = input("Let's piglatinize that sentence, bucko!")

   def piglatinize():
       split_input = user_input.split()
       for i in range(len(split_input)):
           if split_input[i][:1] == 'a' or split_input[i][:1] == 'e' or split_input[i][:1] == 'i' or split_input[i][:1] == 'o' or split_input[i][:1] == 'u':
               print(f"{split_input[i]}yay")
           else:
               print(f"{split_input[i][1:]}{split_input[i][0]}ay")

   piglatinize()