import sys


class Computer:
    def __init__(self, lst):
        self.given_lst = lst
        self.distinct_list = list()
        self.fx_list = list()

    def evaluate(self):
        self.distinct_list = list(set(self.given_lst))
        for str_num in self.distinct_list:
            self.fx_list.append(self.apply_func(str_num))
        index_2nd_highest = self.get_2nd_highest()
        if index_2nd_highest == -1:
            return -1
        else:
            return self.distinct_list[index_2nd_highest]

    def get_2nd_highest(self):
        """
        :return: the index of 2nd largest number, if does not exist returns -1
        """
        h1 = h2 = -1 * sys.float_info.max
        ih1 = -1
        ih2 = -1
        for i, f_num in enumerate(self.fx_list):
            if f_num > h1:
                h2 = h1
                h1 = f_num
                ih2 = ih1
                ih1 = i
            elif f_num > h2:
                h2 = f_num
                ih2 = i
        return ih2

    def apply_func(self, str_num):
        """
        :param str_num: takes number in form of string
        :return: special hash value of the string
        """
        neg = False
        # handles the case where number is negative
        if str_num[0] == '-':
            neg = True
            str_num = str_num[1:]
        length = len(str_num)
        fx = 0.0
        for i, digit in enumerate(str_num):
            fx = fx + float(float(digit) / 10) * float(length - i)
        if neg:
            return -1 * fx
        return fx


if __name__ == '__main__':
    lst = []  # enter your test case here
    cmp = Computer(lst)
    print(cmp.evaluate())
