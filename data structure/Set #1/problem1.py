# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == ']' and c == '[':
            return True
        elif self.bracket_type == '}' and c == '{':
            return True
        elif self.bracket_type == ')' and c == '(':
            return True
        else:
            return False

if __name__ == "__main__":
    text = sys.stdin.read()

    opening_brackets_stack = []
    result=1
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            opening_brackets_stack.append(next) ###如果左边符号则push到stack中
            result=str(i+1)   ###如果左符号（opening）结尾赋值遍历长度 
        elif next == ')' or next == ']' or next == '}':
            if len(opening_brackets_stack)==0:  ###判断stack是否为空，为空则不匹配
                result=str(i+1)   ###输出不匹配位置closing
                break  ###退出循环
            else:
                c=opening_brackets_stack.pop()  ### 从stack中pop出左边符号，用于匹配
                out=Bracket(next,i) ###是否匹配
                if out.Match(c) and len(opening_brackets_stack)==0:
                   result='Success'  ###全匹配则一直result=‘success’
                elif out.Match(c)==False:  ###不匹配
                   result=str(i+1)  ###输出不匹配位置closing
                   break
                elif out.Match(c) and len(opening_brackets_stack)!=0: ###如果匹配但是stack不为0
                    result=str(text.index(opening_brackets_stack[0])+1) ###找出first opening位置
        else:
            pass

print(result)
