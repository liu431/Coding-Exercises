class Solution:
    def intToRoman(self, num: int) -> str:
        # Dictionary for Roman numerals
        dic = {1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50:'L', 90:'XC', 
               100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M'}
        # Initialize the output string
        roman = ''
        # Add the symbols iteratively
        for key in sorted(dic.keys(), reverse=True):
            # Get quotient
            quotient = num // key
            # Add to output if there are quotients
            if quotient >= 0:
                roman += dic[key] * quotient
            # Update num to be the reminder
            num = num % key
        return roman
                
        
       
