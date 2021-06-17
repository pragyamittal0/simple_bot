from nltk.chat.util import  Chat , reflections

pairs = [
    ['my name is (.*)' , ['hi %1']],
    ['(hi|hello|hola|hollaa)', ['hey there', 'Haayyyyyy!']],
    ['(.*)(location|city) ?', [' Delhi, India']],
    ['(.*) created you ?', ['Pragya did using NLTK']],
    [' how is the weather (.*)?', ['The weather in 1% is amazing']],
    ['(.*) your name ?' , ['My name is BHAVYA']],
    ['(.*) help (.*)' , ['I can help']],
]
chat = Chat(pairs)
chat.converse()