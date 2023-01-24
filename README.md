# BLEC
Bidirectional Logic Evaluation for Consistency (BLEC), an auto metric for logic consistency between Natural Language and Formal Languages.

This is the official implementation of the BLEC in the Findings of ACL 2021 paper: [Logic-Consistency Text Generation from Semantic Parses](https://aclanthology.org/2021.findings-acl.388/)

# Setting Environment
```shell
git clone https://github.com/chatc/BLEC.git
cd BLEC
conda create -n BLEC python==3.7
conda activate BLEC
pip install -r requirements.txt
```

# Logic2text
## Code logic of evaluation
- First, extract keywords in the logic form including numbers operations etc.
- Then, check if there is any natural language in prediction can cover these keywords (bidirectional).
- Last, if some keywords are not covered, return 0, else return 1

Note that BLEC for Logic2text only judges known errors. If the return value is 0, it means some errors are found in the predictions. However, if the return value is 1, it means we did not discover any errors from the predictions (some unknown errors can still exist).

## Demo for Logic2text
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
# Spider
## Code logic of evaluation
- First, extract keywords in the logic form including numbers, operations etc. We call them a template, for example:
```json
{
  "SELECT name_first ,  name_last FROM player WHERE death_year = '';": {
    "{VALUE0}": "",
    "{COLUMN0}": "name_first",
    "{COLUMN1}": "name_last",
    "{COLUMN2}": "death_year",
    "{TABLE0}": "player",
    "{OP0}": "="
  }
}
```
is a template for one SQL query. It extract the keywords in SQL and label them using special tokens such as `{COLUMN1}`.
* we build the template in advance, if you only want to use BLEC on the dev/test set of our paper, you can directly load `template_to_names_{dev/test}.json`. If you want to customize your own dataset, please check carefully the demo code (the part not loading the template) and mimic the files that are related.
- Then, check if there is any natural language in prediction can cover these keywords (bidirectional).
- Last, if some keywords are not covered, return 0, else return 1

Note that BLEC for Spider only judges known errors. If the return value is 0, it means some errors are found in the predictions. However, if the return value is 1, it means we did not discover any errors from the predictions (some unknown errors can still exist).


# Demo for Spider
```python
# For Spider
from BLEC.Spider import BLECSpider

# load template to accelerate repeated evaluation on the same dataset
blec = BLECSpider(template_path="./tests/template_to_names_test.json") # replace test with dev if needed

# Recompute the template by assigning templte_path = None, then the templates will be generated automatically.
# blec = BLECSpider(template_path=None,
#                   translate=False,
#                   original_data_path="./tests/spider/raw/",
#                   mapping_path="./tests/spider/preprocessed/",
#                   eval_type="test")

pred = "How many singers are there?"
logic = "SELECT count(*) FROM singers"
errors_tokens = blec.evaluate(pred, logic)

if len(errors_tokens) == 0:
    print('No errors are found!')
else:
    print('Errors are found in:',errors_tokens)
```

# File Structure
```
.
├── BLEC                                   # Main code for BLEC (Logic2text, Spider)
│   └── Logic2text                         # Code for evaluation on Logic2text
│   │       ├── APIs.py                    # Map operations in logic forms to natural language
│   │       ├── eval.py                    # Functions for evaluations, using mappings in APIs.py
│   │       └── logic2text.py              # A wrapped class as user interface
│   └── Spider                             # Code for evaluation on Spider
│   │       ├── sql_components.json        # Map operations in SQL to natural language
│   │       ├── eval.py                    # Functions for evaluations, using mappings in sql_components.json
│   │       ├── template_config.py         # Configurations for generating templates
│   │       ├── utils.py                   # Some helper functions for eval.py
│   │       └── spider.py                  # A wrapped class as user interface
│   └── blec.py                            # Universal user interface for both Logic2text and Spider
│
├── test                                   # Files to test if BLEC works
│   ├── Spider                             # Spider data copied from original paper
│   ├── logic2text_raw_test.json           # Raw test dataset of Logic2text
│   ├── logic2text_test.py                 # Code for testing BLEC on Logic2text
│   ├── multi_dataset_samples.json         # Model predictions of Logic2text, used as input of logic2text.py
│   ├── spider_test.py                     # Test code of spider without using class
│   ├── template_to_names_dev.json         # The preprocessed template on Spider dev set
│   └── template_to_names_test.json        # The preprocessed template on Spider test set
├── demo_test.py                           # The demo code (the same as the code in readme)
├── README.md                              # This file itself
└── requirements.txt                       # Use pip to install these packages
```

# Citation

Please cite this paper if you use our data or code.

```bibtex
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
