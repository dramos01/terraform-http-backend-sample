def titlecase(string):
    if not isinstance(string, str):
        raise TypeError('Input must be string')
    if len(string) == 0:
        return  
    return  ' '.join([ str(word[0].upper() + word[1:]) for word in string.split(' ') if word != ''])
