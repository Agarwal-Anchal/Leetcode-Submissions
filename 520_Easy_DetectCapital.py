class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.upper()==word:
            return True
        elif word[1:]==word[1:].lower():
                    return True
        else:
            return False 
