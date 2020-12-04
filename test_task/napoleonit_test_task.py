"""
Римские цифры представлены в виде I, V, X, L, C, D и M
Необходимо с помощью кода python преобразовать римское число в арабское (стандартное) число.


Решение:
В простейшем случае строка просто разбивается на слагаемые
(не важно в каком порядке) и значения цифр складываются. Проблемы появляются в случаях,
когда происходит вычитание. Это следующие числа: 4, 9, 40, 90, 400, 900. Мы добавим их
в отдельный список и каждый раз будем проверять есть ли такое число в нашей строке.
Если есть соответсвующая комбинация символов - прибавляем ее числовое значение к
общему значению, если нету - берем значение из списка roman_dict.
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50,
                      "C": 100, "D": 500, "M": 1000}
        roman_dict_special = {"IV": 4, "IX": 9, "XL": 40,
                              "XC": 90, "CD": 400, "CM": 900}
        count = 0
        i = 0
        lst = list(s)
        while i < len(s):
            if ''.join(lst[i:i+2]) in roman_dict_special and i+1 < len(s):
                count += roman_dict_special[''.join(lst[i:i+2])]
                i += 2
            else:
                count += roman_dict[lst[i]]
                i += 1

        return count


#instance = Solution()
#print(instance.romanToInt("IV"))  # 4
#print(instance.romanToInt("XC"))  # 90
#print(instance.romanToInt("CM"))  # 900
#print(instance.romanToInt("VLIII"))  # 58
