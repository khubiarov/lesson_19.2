
wrong_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


cleaned_data = 'рипта'

if cleaned_data.lower() in wrong_words:
    raise ValueError('В заголовке есть недопустимое слово')
else:
    print(cleaned_data)


