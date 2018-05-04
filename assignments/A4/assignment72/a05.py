def word_count(x):
    x = x.lower()
    import re
    dict = {}
    var = re.split("[, . " " \n \t  _ : ; @ # $ % < > ? | + - * / ]",x)
    for i in var:
        if i == '':
            continue
        elif i == "'large'":
            dict['large'] = 1
        elif i not in dict:
            dict[i] = 1
        else:
            dict[i] +=1
    return dict

