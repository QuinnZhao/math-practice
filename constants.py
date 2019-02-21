TYPES =["20以内加",
        "和为20到100两位数加",
        "100以内两位数减",
        "100以内加减运算",
        "10以内连加",
        "10以内连减",
        # "10以内混合加减"
]

'''
OPERATIONS_DICT = {
        TYPES[0] : 'add_within_20',
        TYPES[1] : 'add_within_20_100',
        TYPES[2] : 'sub_within_100',
        TYPES[3] : 'mix_within_100',
        TYPES[4] : 'add_within_10',
        TYPES[5] : 'sub_within_10',
        # TYPES[6] : 'mix_within_10'
}
'''

OPERATIONS_DICT = {
        TYPES[0] : ['add_within_20', 0, 20],
        TYPES[1] : ['add_within_20_100', 0, 100],
        TYPES[2] : ['sub_within_100', 0, 100],
        TYPES[3] : ['mix_within_100', 0, 100],
        TYPES[4] : ['add_within_10', 0, 10],
        TYPES[5] : ['sub_within_10', 0, 10],
        # TYPES[6] : ['mix_within_10']
}

add_template_2 = '{}+{}='
add_template_3 = '{}+{}+{}='
sub_template_2 = '{}-{}='
sub_template_3 = '{}-{}-{}='
mix_template_ps = '{}+{}-{}='
mix_template_sp = '{}-{}+{}='

OPERATIONS_DICT_1 = {
        TYPES[0] : ['add', 0, 20, 2, (add_template_2, )],
        TYPES[1] : ['add', 0, 100, 2, (add_template_2, )],
        TYPES[2] : ['sub', 0, 100, 2, (sub_template_2, ) ],
        TYPES[3] : ['mix', 0, 100, 2, (add_template_2, sub_template_2)],
        TYPES[4] : ['add', 0, 10, 3, (add_template_3, )],
        TYPES[5] : ['sub', 0, 10, 3, (sub_template_3, )],
        # TYPES[6] : ['mix', 0, 10, 3, (add_template_3, sub_template_3, mix_template_ps, mix_template_sp)]
        }
