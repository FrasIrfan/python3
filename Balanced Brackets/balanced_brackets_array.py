
def is_Balanced(self):
    bracket = {'{': '}', '(': ')', '[': ']'}  
    List_1 = ['{','[','(']
    List_2 = ['}',']',')']
    
    New_List = List_1+List_2

    if New_List == bracket:
        return "YES"
    else:
        return "NO"

result = is_Balanced("{[()]}")
print (result)