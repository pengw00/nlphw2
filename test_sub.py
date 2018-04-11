sub_rule = 'A_B_C_D_E'
list_rule = []
def sub_r(sub_rule):
    sub = sub_rule.split('_')
    if len(sub) >= 2:
        sub_rule += '->'
        for item in sub[1:-1]:
            sub[0] += '_'
            sub[0] += item
        sub_rule += sub[0]
        sub_rule += ' '
        sub_rule += sub[-1]
        sub_r(sub[0])
        print(sub_rule)
    else:
        sub_rule += '->'
        for item in sub:
            sub_rule += ' '
            sub_rule += item
        print(sub_rule)

sub_r(sub_rule)