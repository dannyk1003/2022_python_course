def a():
    text = None
    return text.upper()

def b():
    a()

def c():
    b()

#c()

try:
    c()
except (AttributeError):
    print('except happened!')
    import traceback
    traceback.print_exc() # 輸出錯誤訊息