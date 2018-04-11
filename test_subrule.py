sub_rule = 'A_B_C_D_E'
list_rule = []
def sub_r(sub_rule):
    sub = sub_rule.split('_')
    if len(sub) == 2:
        sub_rule += '->'
        for item in sub:
            sub_rule += ' '
            sub_rule += item
        list_rule.append(sub_rule)
    else:
        sub_rule += '->'
        for item in sub[1:-1]:
            sub[0] += '_'
            sub[0] += item
        sub_rule += sub[0]
        sub_rule += ' '
        sub_rule += sub[-1]
        sub_r(sub[0])
        list_rule.append(sub_rule)
    l = []
    for i in range(len(list_rule)):
        l.append(list_rule[len(list_rule)-i-1])
    return l
#print(sub_r(sub_rule))
a = sub_r(sub_rule)
print(a)
def reverse(list):
    l = []
    for i in range(len(list)):
        l.append(a[len(list)-i-1])
    return l
print(reverse(a))