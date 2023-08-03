from deep_translator import MyMemoryTranslator

def englishToFrench(englishText):
    '''
    Returns the text translated into french.
        Parameters:
            englishText (str): the english text to be translated
        Returns:
            frenchText (str): the text translated into french
    '''
    frenchText = MyMemoryTranslator(source='en-GB', target='fr-FR').translate(englishText)
    return frenchText

def frenchToEnglish(frenchText):
    '''
    Returns the text translated into english.
        Parameters:
            frenchText (str): the french text to be translated
        Returns:
            englishText (str): the text translated into english
    '''
    englishText = MyMemoryTranslator(source='fr-FR', target='en-GB').translate(frenchText)
    return englishText
