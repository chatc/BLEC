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

# For Spider
from BLEC.Spider import BLECSpider
# load template to accelerate repeated evaluation on the same dataset
# blec = BLECSpider(template_path="./tests/template_to_names_test.json") # replace test with dev if needed

# Recompute the template by assigning templte_path = None, then the templates will be generated automatically.
blec = BLECSpider(template_path=None,
                  translate=False,
                  original_data_path="./tests/spider/raw/",
                  mapping_path="./tests/spider/preprocessed/",
                  eval_type="test")

pred = "How many singers are there?"
logic = "SELECT count(*) FROM singers"
errors_tokens = blec.evaluate(pred, logic)

if len(errors_tokens) == 0:
    print('No errors are found!')
else:
    print('Errors are found in:',errors_tokens)
