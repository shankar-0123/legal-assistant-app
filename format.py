import re

def format_paragraph(text):
    
    text = text.replace("**", "</b>").replace("**", "<b>")
    
    
    pattern = re.compile(r'</b>')
    
    text = re.sub(pattern, lambda m: "<b>" if pattern.subn('', text[:m.start()])[1] % 2 == 0 else m.group(0), text)
    text = text.replace('\n','<br>')
    text = text.replace('*','&#8226')
    return text