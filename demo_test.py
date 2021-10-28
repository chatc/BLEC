# For Logic2text
from BLEC.Logic2text import BLECLogic2text
blec = BLECLogic2text()
logic = 'most_eq { filter_eq { all_rows ; start ; 194 } ; day power ( w ) ; 1000 } = true'
pred = 'for jim clark, when his start was in the 190s, most of the day power was 1000w.'
truth = 'for media in the quad cities, when the start was in the 1940s, the day power is 1000 the majority of the time.'
errors_tokens = blec.evaluate(logic, pred, truth)

if len(errors_tokens) == 0:
    print('No errors are found!')
else:
    print('Errors are found in:',errors_tokens)

