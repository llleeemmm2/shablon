import pymorphy3
from words2numsrus import NumberExtractor

morph = pymorphy3.MorphAnalyzer()
name = (morph.parse(input('Введите имя: '))[0]).inflect({'ablt'})
number = input('Введите число: ').split()
noun = morph.parse(input('Введите существительное: '))[0].inflect({'accs'})
adj = morph.parse(input('Введите прилагательное: '))[0].inflect({noun.tag.gender})
verb = morph.parse(input('Введите глагол: '))[0]
number = [morph.parse(i)[-1].inflect({'ablt'}).word for i in number]

def unpack(s):
    return " ".join(map(str, s))

ext = NumberExtractor()

money = morph.parse("рубль")[0].make_agree_with_number(int(ext.replace(number[-1]))).word

print(f'Плохого человека {name.word.capitalize()} не назовут. \
Обладая {unpack(number)} рублями, он{"a" if "femn" in name.tag else ""} может {verb.word} {adj.word} {noun.word}')