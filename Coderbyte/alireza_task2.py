a = '<div><div><b></b></div><p></div></p>'
b= 'div em a i b'
c = '<p>'
def htmlparser(html): 
    html_list = html.replace('<','').replace('>', ' ').strip().split() 
    print(html_list) 
    print("=================================================") 
    while len(html_list) > 0:
        closeing_tag = '/'+html_list[0]
        if closeing_tag in html_list:
            html_list.remove(html_list[0])
            html_list.remove(closeing_tag)
            print(html_list)
        else: return html_list[0]  
    return 'OK'           

print(htmlparser(a))