def isPalindrome(x: int) -> bool:
    orginal  = str(x)
    reverse = orginal[::-1]
    if orginal == reverse:
        return True
    else: 
        return False
    
x=121

print(isPalindrome(x))
