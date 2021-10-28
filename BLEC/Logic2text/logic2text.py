from BLEC.blec import BLECMetrics
import BLEC.Logic2text.eval as eval

class BLECLogic2text(BLECMetrics):
    def __init__(self):
        super().__init__()
    def evaluate(self, pred, logic, gold):
        labels = eval.logic_matching(pred, logic, gold)
        return labels