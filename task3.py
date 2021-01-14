import datetime,json
import hjson
import time
from collections import defaultdict

# Asta nu e un JSON e un HJSON string
txt="""
[
{
    id: 1,
    sourceAccount: "A",
    targetAccount: "B",
    amount: 100,
    time: "2018-03-02T10:33:00.000Z"
},
{
    id: 2,
    sourceAccount: "A",
    targetAccount: "B",
    amount: 100,
    time: "2018-03-02T10:33:50.000Z"
},
{
    id: 3,
    sourceAccount: "A",
    targetAccount: "B",
    amount: 100,
    time: "2018-03-02T10:34:30.000Z"
},
{
    id: 4,
    sourceAccount: "A",
    targetAccount: "B",
    amount: 100,
    time: "2018-03-02T10:36:00.000Z"
},
{
    id: 5,
    sourceAccount: "A",
    targetAccount: "C",
    amount: 250,
    time: "2018-03-02T10:33:00.000Z"
},
{
    id: 6,
    sourceAccount: "A",
    targetAccount: "C",
    amount: 250,
    time: "2018-03-02T10:33:05.000Z"
}
]
"""

def calcEpoch(x):
    return int(time.mktime(time.strptime(x.split(".")[0], '%Y-%m-%dT%H:%M:%S')))


li=hjson.loads(txt) # transformam in JSON
print(li)

def connected_components(lists): # o functie de a da merge la listele care contin aceasi indexi
    neighbors = defaultdict(set)
    seen = set()
    for each in lists:
        for item in each:
            neighbors[item].update(each)
    def component(node, neighbors=neighbors, seen=seen, see=seen.add):
        nodes = set([node])
        next_node = nodes.pop
        while nodes:
            node = next_node()
            see(node)
            nodes |= neighbors[node] - seen
            yield node
    for node in neighbors:
        if node not in seen:
            yield sorted(component(node))

def removeDubs(li): #adaugam id-urile duplicate in liste in functie de cerinte
    transactions=[]
    nr=0
    prev=''
    for l in li:
        for k in li:
            if  li[nr]['id']!=k['id'] and li[nr]['sourceAccount'] == k['sourceAccount'] and li[nr]['targetAccount']== k['targetAccount'] and li[nr]['amount']==k['amount']:
                dif=str(calcEpoch(li[nr]['time']) - calcEpoch(k['time'])).replace('-','')
                if int(dif.replace('-','')) < 60 :
                    transactions.append([li[nr]['id'],k['id']])
                    # transactions.append(li[nr]['id'])
                    print(li[nr]['id'],'e duplicat cu',k['id'],'dif de timp',dif)
        nr+=1
    res = [i for n, i in enumerate(transactions) if i not in transactions[:n]]


    print(res)
    return(res)

li2=removeDubs(li)
l2=list(connected_components(li2))

tran=[]
for l in l2:
    tran2=[]
    for k in l:
        for i in li:
            if i['id']==k:
                id=dict(i)
                break
        tran2.append(id)
    tran.append(tran2)


li=hjson.dumps(tran) # rezultatul final
print(li)
