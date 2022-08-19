import pickle

with open('data.pickle', 'rb') as fr:
    data = pickle.load(fr)
    data.append(60)
    print(data)

print(pickle.dumps(data))