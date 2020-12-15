from operator import attrgetter

class w:
    def __init__(self, id, d, prefId):
        self.id     = id
        self.d      = d
        self.p = prefId

ALL = {}
Q   = {}
S   = {}

startId = 0
lastId  = 5

for id in range(lastId + 1):
    d = {id: w(id, float("inf"), None)}

    Q.update(d)
    ALL.update(d)

Q[startId].d = 0

D = {
    "0-1" : 3,
    "0-4" : 3,
    "1-2" : 1,
    "2-3" : 3,
    "2-5" : 1,
    "3-1" : 3,
    "4-5" : 2,
    "5-0" : 6,
    "5-3" : 1
}

while len(Q) > 0:
    u = min(Q.values(), key = attrgetter('d'))
    S.update({u.id : u})
    Q.pop(u.id)

    for pair in D:
        if pair.startswith(str(u.id) + "-"):
            w = ALL[int(pair.split("-")[1])]

            if (w.d > (u.d + D[pair])):
                w.d = u.d + D[pair]
                w.p = u.id

for id in range(lastId + 1):
    print(str(id) + " d: " + str(S[id].d))
    print(str(id) + " p: " + str(S[id].p))

pathToStartFrom = 2
tmp = pathToStartFrom
while tmp is not None:
    print ("PATH: " + str(tmp))
    tmp = ALL[tmp].p