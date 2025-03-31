amount = int(input("Enter the amount to be withdrawn :"))
note_1 = amount//500
note_2 = (amount%500)//100
note_3 = ((amount%500)%100)//50
note_4 = (((amount%500)%100)%50)//10
print("The 500 rupee notes are", note_1)
print("The 100 rupee notes are", note_2)
print("The 50 rupee notes are", note_3)
print("The 10 rupee notes are", note_4)