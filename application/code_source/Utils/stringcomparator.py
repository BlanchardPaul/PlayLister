class StringComparator(object):
    'Contains the static method that allow to compare two strings with a coeff'

    @staticmethod
    def isTheSame(name, nameToCompare, coeff):
        lName = len(name)
        lNameTo = len(nameToCompare)
        index = 0
        nameList = list(name)
        nameToCompareList = list(nameToCompare)
        for n in nameList:
            for m in nameToCompareList:
                if(n == m):
                    index += 1
                    del nameToCompareList[nameToCompareList.index(m)]
                    break
        return (index > lName/10*coeff and index > lNameTo/10*coeff)
        # if the name with less len has 90% in common with the index, or if both have the coeff % in common with the index
