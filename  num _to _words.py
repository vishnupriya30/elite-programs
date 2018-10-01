num2words1 = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
num2words2 = {2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 6: 'Sixty', 7: 'Seventy', 8:'Eighty', 9: 'Ninety'}
num2words3 = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}

def number(Num):
    if Num > 0 and Num < 20:
        return num2words1[Num]
    elif Num > 19 and Num < 100:
        if Num % 10 == 0:
            return num2words2[Num // 10]
        else:
            return num2words2[Num // 10] + num2words1[Num % 10]
    elif Num > 99 and Num < 1000:
        if Num % 100 == 0:
            return num2words3[Num // 100] + "hundred"
        else:
            return num2words3[Num // 100] + "hundredand" + number(Num - ((Num // 100) * 100))
#function returns no of characters in all numbers ranging from num1 to num2
def count(num1, num2):
    count = 0
    for num in range(num1, num2 + 1):
        count = count + len(number(num))
        num = num + 1
    return count
num1 = int(input("enter a num"))
num2 = int(input("enter a num"))
print(count(num1, num2))

    

