import math
from sklearn import datasets
import numpy as np

data = datasets.load_iris()


def entropy(p1, n1):
    if p1 == 0 and n1 == 0:
        return 1
    elif p1 == 0 or n1 == 0:
        return 0
    else:
        pp = p1 / (p1 + n1)
        np = n1 / (p1 + n1)
        return -pp * math.log2(pp) - np * math.log2(np)


def ig(p1, n1, p2, n2):
    pr = p1 + p2
    nr = n1 + n2
    num = pr + nr
    num1 = p1 + n1
    num2 = p2 + n2
    return entropy(pr, nr) - num1 / num * entropy(p1, n1) - num2 / num * entropy(p2, n2)


def ID3DTrain(feature, target):
    node = {}
    node["data"] = range(len(target))
    tree = []
    tree.append(node)
    t = 0
    while t < len(tree):
        idx = tree[t]["data"]
        if sum(target[idx]) == 0:
            tree[t]["leaf"] = 1
            tree[t]["decision"] = 0
        elif sum(target[idx]) == len(idx):
            tree[t]["leaf"] = 1
            tree[t]["decision"] = 1
        else:
            bestIG = 0
            for i in range(feature.shape[1]):
                pool = list(set(feature[idx, i]))
                pool.sort()
                for j in range(len(pool) - 1):
                    thres = (pool[j] + pool[j + 1]) / 2
                    G1 = []
                    G2 = []
                    for k in idx:
                        if feature[k][i] < thres:
                            G1.append(k)
                        else:
                            G2.append(k)
                    p1 = sum(target[G1] == 1)
                    n1 = sum(target[G1] == 0)
                    p2 = sum(target[G2] == 1)
                    n2 = sum(target[G2] == 0)
                    thisIG = ig(p1, n1, p2, n2)
                    if thisIG > bestIG:
                        bestIG = thisIG
                        bestG1 = G1
                        bestG2 = G2
                        bestthres = thres
                        bestf = i
            if bestIG > 0:
                tree[t]["leaf"] = 0
                tree[t]["selectf"] = bestf
                tree[t]["threshold"] = bestthres
                tree[t]["child"] = [len(tree), len(tree) + 1]
                node = {}
                node["data"] = bestG1
                tree.append(node)
                node = {}
                node["data"] = bestG2
                tree.append(node)
            else:
                tree[t]["leaf"] = 1
                if sum(target[idx] == 1) > sum(target[idx] == 0):
                    tree[t]["decision"] = 1
                else:
                    tree[t]["decision"] = 0
        t += 1
    return tree


def ID3DTtest(T, feature):
    N = feature.shape[0]
    target = np.zeros((N,))
    for i in range(N):
        feature1 = feature[i, :]
        t = 0
        while T[t]["leaf"] == 0:
            node = T[t]
            if feature1[node["selectf"]] < node["threshold"]:
                t = node["child"][0]
            else:
                t = node["child"][1]
        target[i] = T[t]["decision"]
    return target


def majority_vote(pred1, pred2, pred3):
    final_pred = []
    for p1, p2, p3 in zip(pred1, pred2, pred3):
        if p1 == p2:
            final_pred.append(p1)
        elif p2 == p3:
            final_pred.append(p2)
        elif p1 == p3:
            final_pred.append(p1)
        else:
            final_pred.append(0)
    return np.array(final_pred)


feature1 = data.data[50:80][:]
feature2 = data.data[100:130][:]
feature = np.concatenate((feature1, feature2), axis=0)
target = np.concatenate((data.target[50:80] - 1, data.target[100:130] - 1))

testing_feature1 = data.data[80:100][:]
testing_feature2 = data.data[130:150][:]
testing_feature = np.concatenate((testing_feature1, testing_feature2), axis=0)
testing_target = np.concatenate((data.target[80:100] - 1, data.target[130:150] - 1))

T = ID3DTrain(feature, target)
predtarget = ID3DTtest(T, feature)
training_accuracy = np.sum(predtarget == target) / len(target)
print("第一題training_accuracy:", training_accuracy)


predtarget = ID3DTtest(T, testing_feature)
training_accuracy = np.sum(predtarget == testing_target) / len(testing_target)
print("第一題testing accuracy:", training_accuracy)

feature1 = data.data[0:30][:]
feature2 = data.data[50:80][:]
feature = np.concatenate((feature1, feature2), axis=0)
target = np.concatenate((data.target[0:30], data.target[50:80]))
T01 = ID3DTrain(feature, target)

feature1 = data.data[0:30][:]
feature2 = data.data[100:130][:]
feature = np.concatenate((feature1, feature2), axis=0)
target = np.concatenate((data.target[0:30], data.target[100:130] - 1))
T02 = ID3DTrain(feature, target)

feature1 = data.data[50:80][:]
feature2 = data.data[100:130][:]
feature = np.concatenate((feature1, feature2), axis=0)
target = np.concatenate((data.target[50:80] - 1, data.target[100:130] - 1))
T12 = ID3DTrain(feature, target)

train_feature = np.concatenate((data.data[0:30], data.data[50:80], data.data[100:130]))
train_target = np.concatenate(
    (data.target[0:30], data.target[50:80], data.target[100:130])
)
a = ID3DTtest(T01, train_feature)
b = ID3DTtest(T02, train_feature)
c = ID3DTtest(T12, train_feature)
for i in range(len(b)):
    if b[i] == 1:
        b[i] = 2
for i in range(len(c)):
    if c[i] == 0:
        c[i] = 1
    else:
        c[i] = 2
predtarget = majority_vote(a, b, c)
train_accuracy = np.sum(predtarget == train_target) / len(train_target)
print("第二題training accuracy:", train_accuracy)

feature0 = np.concatenate(
    (data.data[30:50], data.data[80:100], data.data[130:150]), axis=0
)
testing_target = np.concatenate(
    (data.target[30:50], data.target[80:100], data.target[130:150]), axis=0
)
a = ID3DTtest(T01, feature0)
b = ID3DTtest(T02, feature0)
c = ID3DTtest(T12, feature0)
for i in range(len(b)):
    if b[i] == 1:
        b[i] = 2
for i in range(len(c)):
    if c[i] == 0:
        c[i] = 1
    else:
        c[i] = 2
predtarget = majority_vote(a, b, c)
testing_accuracy = np.sum(predtarget == testing_target) / len(testing_target)
print("第二題testing_accuracy:", testing_accuracy)
