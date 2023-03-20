class analysedText(object):
    
    def __init__ (self, text):
        
        # TODO: Remove the punctuation from <text> and make it lower case.
        pnc_rm = text.replace(".","").replace("!","").replace("?","").replace(",","")
        frmt_txt = pnc_rm.lower()

        # TODO: Assign the formatted text to a new attribute called "fmtText"
        self.fmtText = frmt_txt
    
    def freqAll(self):    

        # TODO: Split the text into a list of words  
        splt_txt_list = self.fmtText.split(" ")

        # TODO: Create a dictionary with the unique words in the text as keys
        dict_text ={}
        
        for element_word in set(splt_txt_list) :
            dict_text[element_word] = splt_txt_list.count(element_word)
        
        # and the number of times they occur in the text as values
      
        # return the created dictionary
        return dict_text
    
    def freqOf(self, word):

        # TODO: return the number of occurrences of <word> in <fmtText>
        freq_word = self.freqAll()
        
        if word in freq_word:
            return freq_word[word]
        else :
            return 0
        
                
import sys

sampleMap = {'eirmod': 1,'sed': 1, 'amet': 2, 'diam': 5, 'consetetur': 1, 'labore': 1, 'tempor': 1, 'dolor': 1, 'magna': 2, 'et': 3, 'nonumy': 1, 'ipsum': 1, 'lorem': 2}

def testMsg(passed):
    if passed:
       return 'Test Passed'
    else :
       return 'Test Failed'

print("Constructor: ")
try:
    samplePassage = analysedText("Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet.")
    print(testMsg(samplePassage.fmtText == "lorem ipsum dolor diam amet consetetur lorem magna sed diam nonumy eirmod tempor diam et labore et diam magna et diam amet"))
except:
    print("Error detected. Recheck your function " )
    
    
print("freqAll: ")
try:
    wordMap = samplePassage.freqAll()
    print(testMsg(wordMap==sampleMap))
except:
    print("Error detected. Recheck your function " )
print("freqOf: ")
try:
    passed = True
    for word in sampleMap:
        if samplePassage.freqOf(word) != sampleMap[word]:
            passed = False
            break
    print(testMsg(passed))
    
except:
    print("Error detected. Recheck your function  " )
    