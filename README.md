# BLEC
Bidirectional Logic Evaluation for Consistency (BLEC), an auto metrics for logic consistency between Natural Language and Formal Languages.

This is the official implementation of the BLEC in the Findings of ACL 2021 paper: [Logic-Consistency Text Generation from Semantic Parses](https://aclanthology.org/2021.findings-acl.388/)

# Demo for Logic2text
```python
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
```
# Citation

Please cite this paper if you use our data or code.

```angular2html
@inproceedings{shu-etal-2021-logic,
    title = "Logic-Consistency Text Generation from Semantic Parses",
    author = "Shu, Chang  and
      Zhang, Yusen  and
      Dong, Xiangyu  and
      Shi, Peng  and
      Yu, Tao  and
      Zhang, Rui",
    booktitle = "Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021",
    month = aug,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.findings-acl.388",
    doi = "10.18653/v1/2021.findings-acl.388",
    pages = "4414--4426",
}
```
