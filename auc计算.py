#从AUC统计意义去计算。所有的正负样本对中，正样本排在负样本前面占样本对数的比例，即这个概率值。

#具体的做法就是它也是首先对prob score从大到小排序，然后令最大prob score对应的sample 的rank为n，第二大score对应sample的rank为n-1，以此类推。

#然后把所有的正类样本的rank相加，再减去M-1种两个正样本组合的情况。

#得到的就是所有的样本中有多少对正类样本的score大于负类样本的score。

#最后再除以M×N。


import numpy as np
from sklearn.metrics import roc_auc_score


def calc_auc(y_labels, y_scores):
    f = list(zip(y_scores, y_labels))
    rank = [values2 for values1, values2 in sorted(f, key=lambda x: x[0])]
    rankList = [i + 1 for i in range(len(rank)) if rank[i] == 1]
    pos_cnt = np.sum(y_labels == 1)
    neg_cnt = np.sum(y_labels == 0)
    auc = (np.sum(rankList) - pos_cnt * (pos_cnt + 1) / 2) / (pos_cnt * neg_cnt)
    print(auc)


def get_score():
    # 随机生成100组label和score
    y_labels = np.zeros(100)
    y_scores = np.zeros(100)
    for i in range(100):
        y_labels[i] = np.random.choice([0, 1])
        y_scores[i] = np.random.random()
    return y_labels, y_scores


if __name__ == '__main__':
    y_labels, y_scores = get_score()
    # 调用sklearn中的方法计算AUC，与后面自己写的方法作对比
    print('sklearn AUC:', roc_auc_score(y_labels, y_scores))
    calc_auc(y_labels, y_scores)



#1.统计所有正样本个数P，负样本个数N；
#2.遍历所有正负样本对，统计正样本预测值大于负样本预测值的样本总个数number
#3.AUC = number / (P * N)


def calcAUC_byProb(labels, probs):
    N = 0
    P = 0
    neg_prob = []
    pos_prob = []
    for _,i in enumerate(labels):
        if (i == 1):
            P += 1
            pos_prob.append(probs[_])
        else:
            N += 1
            neg_prob.append(probs[_])
    number = 0
    for pos in pos_prob:
        for neg in neg_prob:
            if (pos > neg):
                number += 1
            elif (pos == neg):
                number += 0.5
    return number / (N * P)


y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])
pred = np.array([0.1, 0.4, 0.5 ,0.6, 0.35, 0.8, 0.9, 0.4, 0.25, 0.5])
print("sklearn auc:",roc_auc_score(y, pred))
print("my auc calc by area:", calcAUC_byRocArea(y, pred))
print("my auc calc by prob:", calcAUC_byProb(y, pred))
