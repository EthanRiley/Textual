from textblob import TextBlob


def avg_polarity(speech):
    ''' Takes in speech string and returns average polarity as float'''
    
    sum1 = 0
    # output list of sentences from speech 
    lst_of_sent = speech.split('.')
    
    # calculating avg sentence polarity 
    
    for sent in lst_of_sent:
        polar = TextBlob(sent).sentiment.polarity
        sum1 += polar
    return sum1 / len(lst_of_sent)

def avg_subj(speech):
    ''' Takes in speech string and returns average subjectivity as float '''
    
    sum1 = 0
    lst_of_sent = speech.split('.')
    
    # calculate avg sentence sebjectivity 
    for sent in lst_of_sent:
        sub = TextBlob(sent).sentiment.subjectivity
        sum1 += sub
    return sum1 / len(lst_of_sent)


