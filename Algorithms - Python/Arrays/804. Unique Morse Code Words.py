class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_dic = {}
        morse_table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        word_morse = set()
        for word in words:
            trans = ''
            for s in word:
                trans += morse_table[ord(s) - 97]
            word_morse.add(trans)
        
        return len(word_morse)
