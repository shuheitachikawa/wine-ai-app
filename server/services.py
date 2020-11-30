import pickle
from pandas import DataFrame

class PredictionService:
  model = pickle.load(open('AI_model01.sav', mode='rb'))

  @staticmethod
  def predict(data):
    # DataFrame形に変換
    df = DataFrame.from_dict(PredictionService.convert_dict(data), orient='columns')
    # 変換したモデルの呼び出し
    predict = PredictionService.model.predict([df['value']])
    # numpy型で帰ってくるのでfloatに変換
    return float(predict[0])
  
  # POSTデータを配列型に変換
  @staticmethod
  def convert_dict(data):
    converted = {'id': [], 'value': []}
    for k in data:
      converted['id'].append(k['id'])
      converted['value'].append(k['value'])
    return converted