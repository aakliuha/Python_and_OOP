class Saying:

    def sayIt(self, type='shout'):

        def outLoud(word):
            print(word.capitalize())
            return word.capitalize()

        def whisper(word):
            print(word.lower())
            return word.lower()

        if type == 'shout':
            return outLoud
        else:
            return whisper


saying1 = Saying()
func = saying1.sayIt()
func('yes')





