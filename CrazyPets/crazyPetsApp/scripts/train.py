import pickle

from lightgbm import LGBMRegressor, LGBMClassifier
import pandas as pd
import numpy as np
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error


def get_data():
    train = pd.read_csv('../input/train.csv')
    # 4人のscoreの平均を取る
    train = train.groupby(
        [col for col in train.columns if not col == 'score'], as_index=False)[['score']].mean()
    return train

def train_model(train: pd.DataFrame):
    folds = KFold(n_splits=3, shuffle=True, random_state=42)
    # CVのためいくつかモデルをつくる
    models = []

    oof_preds = np.zeros(train.shape[0])
    for n_fold, (trn_idx, val_idx) in enumerate(folds.split(train)):
        train_x = train.drop(columns='score').iloc[trn_idx]
        train_y = train['score'].iloc[trn_idx]
        valid_x = train.drop(columns='score').iloc[val_idx]
        valid_y = train['score'].iloc[val_idx]
        
        params = {
            'num_leaves': 10,#これと
        }
        model = LGBMRegressor(#n_estimators=10000,
                            n_estimators=100000,#これと
                            metric='rmse',
                            learning_rate=0.001)#これと
                            # learning_rate=0.001)
        model.fit(train_x, train_y,
                eval_set=[(train_x, train_y), (valid_x, valid_y)],
                # early_stopping_rounds=500,
                early_stopping_rounds=500,
                eval_metric='rmse',
                verbose=1000)
        oof_preds[val_idx] = model.predict(valid_x)
        models.append(model)
    print('CV score: ', mean_squared_error(train['score'], oof_preds))
    return models

if __name__ == '__main__':
    train = get_data()
    models = train_model(train)
    pickle.dump(models, open('../model/model.pkl', 'wb'))