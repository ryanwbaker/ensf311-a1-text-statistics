# Author: Ryan Baker
def count_personal_pronouns(s):
    """Count personal pronouns I, my, me, you, we in string s

    The pronouns are counted regardless of capitalization.

    s (str): string to be searched for pronouns
    returns: (int) Number of personal pronouns
    """

    #TODO: implement function
    count = 0
    #keep only alphanumerics, spaces, and new lines. split() words and convert to lower case for comparison.
    for word in ''.join(el.lower() for el in s if el.isalnum() or el==' ' or el=='\n').split():
        if(word == 'i' or word == 'my' or word == 'me' or word == 'you' or word == 'we'):
            count += 1
    return count

def number_of_words_in_document(s):
    """Counts number of words (separated by whitespace) in string s

    s (str): string to count words in
    returns: (int) number of words
    """
  
    #TODO: implement function
    #remove new lines then split in order to count words
    return len(s.strip().split())

def number_of_sentences(s):
    """Counts number of sentences (separated by '.', '!' or '?') in string s

    s (str): string to count sentences in
    returns: (int) number of sentences
    """
  
    #TODO: implement function
    #strip() to remove new line characters
    #change all sentence terminators to periods for easy counting
    #The final punctuation leaves a blank element at the end. [:-1] removes this.
    return len(s.strip().replace('!','.').replace('?','.').split('.')[:-1])

def print_text_statistics(filename):
    """Prints sentence, word, word-per-sentence and personal pronoun count

    Functions in this module are used for counting.
        
    filename (str): Name of file to analyze (UTF-8 encoded)
    returns: None
    """
   
    #TODO: Read text from UTF-8 encoded file.
    #only care about the text, so immediately call read()
    text_string = open(filename, 'r', encoding='utf-8').read()
    
    #TODO: Print results, use functions above for computations
    words = number_of_words_in_document(text_string)
    sentences = number_of_sentences(text_string)
    print(f'Number of words in document {words}')
    print(f'Number of sentences in document {sentences}')
    print(f'Number of words per sentence {words/sentences:.2f}')
    print(f'Number of personal pronouns {count_personal_pronouns(text_string)}')

if __name__ == '__main__':
    
    print_text_statistics('feynman.txt')