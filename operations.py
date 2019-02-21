from constants import OPERATIONS_DICT


class Operations():

    def __init__(self, operation, formula_number):   # , **operations_dict):
        # self.operation = operations_dict[operation][0]
        self.operation = operation
        # self.tempalte_tuple = operations_dict[operation][4]
        self.template_tuple = OPERATIONS_DICT[operation][4]

        # self.lower_limit = operations_dict[operation][1]
        self.lower_limit = OPERATIONS_DICT[operation][1]
        # self.upper_limit = operations_dict[operation][2]
        self.upper_limit = OPERATIONS_DICT[operation][2]
        # self.parameters_num = operations_dict[operation][3]
        self.parameters_num = OPERATIONS_DICT[operation][3]
        self.formula_number = formula_number
        self.formula_list = []
        self.operations_dict = {}
        self.init_operation_dict()
        self.generator()

    def get_formulars(self):
        return self.formula_list.copy()

    def init_operation_dict(self):
        for key, value in OPERATIONS_DICT.items():
            self.operations_dict[key] = value[0]
            if value[0] == 'add':
                self.operations_dict[key] = self.gen_add
            if value[0] == 'sub':
                self.operations_dict[key] = self.gen_sub
            if value[0] == 'mix':
                self.operations_dict[key] = self.gen_mix

    def generator(self):
        self.operations_dict[self.operation]()

    def gen_add(self):
        if self.parameters_num < 2 or self.parameters_num > 3:
            return

        self.formula_list = []

        for _ in range(int(self.formula_number)):
            if self.parameters_num == 2:
                self.formula_list.append(self.add())
            if self.parameters_num == 3:
                self.formula_list.append(self.serial_add_3())

    def add(self):
        from random import randint
        while True:
            first_num = randint(self.lower_limit, self.upper_limit)
            second_num = randint(self.lower_limit, self.upper_limit)
            if first_num + second_num <= self.upper_limit:
                return self.template_tuple[0].format(first_num, second_num)

    def serial_add_3(self):
        from random import randint

        while True:
            first_num = randint(self.lower_limit, self.upper_limit)
            second_num = randint(self.lower_limit, self.upper_limit)
            third_num = randint(self.lower_limit, self.upper_limit)
            if first_num + second_num + third_num <= self.upper_limit:
                return self.template_tuple[0].format(
                        first_num, second_num, third_num)

    def gen_sub(self):
        if self.parameters_num < 2 or self.parameters_num > 3:
            return

        self.formula_list = []

        for _ in range(int(self.formula_number)):
            if self.parameters_num == 2:
                self.formula_list.append(self.sub())
            if self.parameters_num == 3:
                self.formula_list.append(self.serial_sub_3())

    def sub(self):
        from random import randint

        while True:
            first_num = randint(self.lower_limit, self.upper_limit)
            second_num = randint(self.lower_limit, self.upper_limit)
            if first_num - second_num >= 0:
                if len(self.template_tuple) == 1:
                    return self.template_tuple[0].format(first_num, second_num)
                else:
                    return self.template_tuple[1].format(first_num, second_num)

    def serial_sub_3(self):
        from random import randint

        while True:
            first_num = randint(self.lower_limit, self.upper_limit)
            second_num = randint(self.lower_limit, self.upper_limit)
            third_num = randint(self.lower_limit, self.upper_limit)
            if first_num - second_num - third_num >= 0:
                if len(self.template_tuple) == 1:
                    return self.template_tuple[0].format(
                        first_num, second_num, third_num)
                else:
                    return self.template_tuple[1].format(
                        first_num, second_num, third_num)

    def gen_mix(self):
        if self.parameters_num < 2 or self.parameters_num > 3:
            return

        if self.parameters_num == 2:
            self.gen_mix_2()

        if self.parameters_num == 3:
            self.gen_mix_3()

    def mix_add_sub(self):
        if len(self.template_tuple) < 3:
            return '0+0-0='

        from random import randint

        while True:
            first_num = randint(self.lower_limit, self.upper_limit)
            second_num = randint(self.lower_limit, self.upper_limit)
            third_num = randint(self.lower_limit, self.upper_limit)
            if first_num + second_num <= self.upper_limit and  \
                    0 <= first_num + second_num - third_num <= \
                    self.upper_limit:
                return self.template_tuple[2].format(
                    first_num, second_num, third_num)

    def mix_sub_add(self):
        if len(self.template_tuple) < 4:
            return '0-0+0='

        from random import randint

        while True:
            first_num = randint(self.lower_limit, self.upper_limit)
            second_num = randint(self.lower_limit, self.upper_limit)
            third_num = randint(self.lower_limit, self.upper_limit)
            if first_num - second_num >= 0 and \
               0 <= first_num - second_num + third_num <= self.upper_limit:
                return self.template_tuple[3].format(
                    first_num, second_num, third_num)

    def gen_mix_2(self):
        if not self.parameters_num == 2 or len(self.template_tuple) < 2:
            return

        from random import randint, shuffle

        self.formula_list = []
        total = int(self.formula_number)

        add_num = randint(10, total)
        sub_num = total - add_num

        for _ in range(add_num):
            self.formula_list.append(self.add())
        for _ in range(sub_num):
            self.formula_list.append(self.sub())
        return shuffle(self.formula_list)

    def gen_mix_3(self):
        if not self.parameters_num == 3 or len(self.template_tuple) < 4:
            return

        from random import randint, shuffle

        self.formula_list = []
        rest = int(self.formula_number)

        if self.template_tuple[0]:
            serial_add_num = randint(0, rest)
        else:
            serial_add_num = 0

        rest -= serial_add_num

        if rest > 0 and self.template_tuple[1]:
            serial_sub_num = randint(0, rest)
        else:
            serial_sub_num = 0

        rest -= serial_sub_num

        if rest > 0 and self.template_tuple[2]:
            mix_add_sub_num = randint(0, rest)
        else:
            mix_add_sub_num = 0

        rest -= mix_add_sub_num

        if rest > 0 and self.template_tuple[3]:
            mix_sub_add_num = rest
        else:
            mix_sub_add_num = 0

        for _ in range(serial_add_num):
            self.formula_list.append(self.serial_add_3())
        for _ in range(serial_sub_num):
            self.formula_list.append(self.serial_sub_3())
        for _ in range(mix_add_sub_num):
            self.formula_list.append(self.mix_add_sub())
        for _ in range(mix_sub_add_num):
            self.formula_list.append(self.mix_sub_add())
        return shuffle(self.formula_list)
