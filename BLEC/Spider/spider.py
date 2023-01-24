from BLEC.blec import BLECMetrics
import BLEC.Spider.eval as eval
import json, os

class BLECSpider(BLECMetrics):
    def __init__(self, template_path=None,
                 translate=False,
                 original_data_path="spider/raw/",
                 mapping_path="spider/preprocessed/",
                 eval_type="test"):

        super().__init__('spider')
        self.translate = translate
        if template_path is None:
            mapping_path = os.path.join(mapping_path,f"{eval_type}.json")
            self.template_to_names = self.prepare_template(original_data_path, mapping_path, eval_type)
            template_path = 'template_to_names.json'
        else:
            self.template_to_names = self.load_template(template_path)

    def prepare_template(self, orginal_data_path, mapping_path, eval_type='test', save_to='template_to_names.json'):
        question_query_pairs, detailed_train_pdq = eval.data_to_components(orginal_data_path, eval_type=eval_type)
        origin_templates = eval.extract_coponents(detailed_train_pdq, clean_number=True)
        origin_sql_to_names = {x: y['name dict'] for x, y in origin_templates.items()}
        trans_sql_to_names = eval.extract_translated_sqls(mapping_path, origin_templates)
        self.template_to_names = [origin_sql_to_names, trans_sql_to_names]
        if save_to is not None and len(save_to):
            with open(save_to, 'w') as file:
                json.dump(self.template_to_names, file)
        return self.template_to_names

    def load_template(self, path):
        sql_to_names = json.load(open(path, 'r'))
        origin_sql_to_names = sql_to_names[0]
        trans_sql_to_names = sql_to_names[1]
        templates_to_names = origin_sql_to_names if not self.translate else trans_sql_to_names
        return templates_to_names

    def evaluate(self, pred, logic, gold=None):
        labels = []
        if self.template_to_names is None:
            raise NotImplementedError
        if logic not in self.template_to_names:
            print("Error: the template not found, the logic is ", logic)
        else:
            name_dict = self.template_to_names[logic]
            pred = pred.lower()
            _, labels = eval.question_test(logic, name_dict, pred)
        return labels