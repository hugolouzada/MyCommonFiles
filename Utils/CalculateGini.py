import math
from sklearn import metrics


def CalculateGini(df, defaultName, scoreName):
    performances = []
    for id,row in df.iterrows():
        score = float(row[scoreName])
        if not math.isnan(score):
         performances.append([score,int(row[defaultName])])

    return -1+2*metrics.roc_auc_score([x[1] for x in performances],[-x[0] for x in performances])