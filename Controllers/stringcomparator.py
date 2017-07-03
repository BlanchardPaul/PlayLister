class StringComparator(object):
    'Contains the static method that allow to compare two strings with a coeff'

    @staticmethod
    def isTheSame(name, nameToCompare, coeff):
        index = 0;
        nameList = list(name);
        nameToCompareList = list(nameToCompare);
        for n in nameList:
            for m in nameToCompareList:
                if(n == m):
                    index += 1;
                    del nameToCompareList[nameToCompareList.index(m)];
                    break;
        return (index > len(name)/10*coeff and index > len(nameToCompare)/10*coeff);
