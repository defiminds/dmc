import re

# receber a input do usuário
binary_str = input("Input Binary String: ")

# sequência de regex para modificar a string
regex_seq = [
    ('000000000', '670a0640a'),
    ('00000000', '650a660a'),
    ('0000000', '6906d0a'),
    ('000000', '6906e0'),
    ('00000', '64073'),
    ('0000', 'MIFA'),
    ('000', 'OQF'),
    ('00', 'MM'),
    ('0', 'x')
]

# substituir cada sequência de 0s na string com sua correspondente regex
for seq, regex in regex_seq:
    binary_str = re.sub(seq, regex, binary_str)

# imprimir a string modificada
print(binary_str)
