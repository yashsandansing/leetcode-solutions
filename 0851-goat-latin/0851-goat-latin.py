class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        # word is between 1 to 50 length

        # convert sentence to list of words
        # word -> check if first letter is consonant
        # if yes, split word and add consonant to the end
        # append ma to the new word
        # add index+1 amount of a's to this word
        # replace this with the current word
        
        vowels = 'aeiou'
        sentence = sentence.split(" ")

        for ind, word in enumerate(sentence):
            new_word = word
            # check if first letter is a consonent
            # if it is, remove it from the first position
            # and append it to the end of the word
            # ONLY if len > 1 -> edge case
            if word[0].lower() not in vowels:
                new_word = new_word[1:] + new_word[0] if len(new_word) > 1 else new_word
            
            # add ma + a*position in sentence
            new_word += "ma" + "a"*(ind+1)
            sentence[ind] = new_word
        
        return " ".join(sentence)
