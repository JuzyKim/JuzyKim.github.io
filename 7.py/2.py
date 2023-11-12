def howtofind(qw):
    while '//' in qw:
        qw = qw.replace('//', '/')

    if qw[-1] == '/':
        qw = qw[:-1]

    return qw 

zh = input()
print(howtofind,zh)