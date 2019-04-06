'''
Given a string "abc" and assuming that each letter in the string has a value equal to its position in the alphabet, our string will have a value of 1 + 2 + 3 = 6. This means that: a = 1, b = 2, c = 3 ....z = 26.

You will be given a list of strings and your task will be to return the values of the strings as explained above multiplied by the position of that string in the list. For our purpose, position begins with 1.

nameValue ["abc","abc abc"] should return [6,24] because of [ 6 * 1, 12 * 2 ]. Note how spaces are ignored.

"abc" has a value of 6, while "abc abc" has a value of 12. Now, the value at position 1 is multiplied by 1 while the value at position 2 is multiplied by 2.

Input will only contain lowercase characters and spaces.

Good luck!

link solution: https://www.codewars.com/kata/reviews/598ea864f0aeb75a87000297/groups/5ca5162700f2270001f1b099
'''

def name_value(my_list):
  soma = [[ord(let)-96 for let in palavra.replace(" ","")] for palavra in my_list]
  #print("Palavras:",my_list,"\nVetor soma:",soma)
  soma = [sum(word)*(ind+1) for ind, word in enumerate(soma)]
  #print("Soma das palavras na lista:", soma)
  return soma



