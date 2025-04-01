en2ko = {
    'book' : '책',
    'snake' : '뱀',
    'language' : '언어'
    }
print(en2ko)
ko2en = {}
for key, item in en2ko.items():
    ko2en[item] = key
print(ko2en)
