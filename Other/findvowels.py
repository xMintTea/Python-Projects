def findVowels(stri):
    vowels = ["а","у","о","ы","э","е","ё","и","ю","я",
           "a","e","i","o","u","y"]
    res = 0
    stri = stri.lower()
    for b in range(len(stri)):
        a = stri[b] in vowels
        if a == False:
            continue
        else:
            res += 1
        

    print(res)

findVowels("Hello World!")