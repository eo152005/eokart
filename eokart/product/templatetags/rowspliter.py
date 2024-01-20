from django import template

register= template.Library()

@register.filter(name= ' rowspliter')
def rowspliter(list_data,row_size):
    rows=[]
    i=1
    for data in list_data:
        rows.append(data)
        i=i+1
        if i ==row_size:
            yield rows
            rows=[]
    yield rows