hlm = '<div><div><b>sdfgh-</b></div><p></div></p>'
a = '<p><b>'
def html_parser(html):
    tags = []
    idx = 0
    while idx < len(html):
        open_tag = html.find('<',idx)
        close_tag = html.find('>',idx+1)
        tags.append(html[open_tag+1:close_tag])
        idx = close_tag+1          
    validation = []
    for tag in tags:
        if tag.startswith('/') == False:
            validation.append(tag)
        elif tag == '/'+validation[-1]:
            validation.pop()
        else: return validation[0]                 
    return 'OK' if len(validation) == 0 else validation[0]

print(html_parser(hlm))

