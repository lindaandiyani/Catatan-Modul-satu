def palindrome(kata):
    for i in range(round(len(kata)/2)):
        palindromekah = False
        if kata[i]==kata[len(kata)-1-i]:
            palindromekah=True
        else:
            palimdromkah = False
            break
    return palindromekah
print(palindrome2('katak'))