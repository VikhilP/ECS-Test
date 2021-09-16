from collections import defaultdict
medalResults = [
    {
        "sport": "cycling",
        "podium": ["1.China", "2.Germany", "3.ROC"]
    },
    {
        "sport": "fencing",
        "podium": ["1.ROC", "2.France", "3.Italy"]
    },
    {
        "sport": "high jump",
        "podium": ["1.Italy", "1.Qatar", "3.Belarus"]
    },
    {
        "sport": "swimming",
        "podium": ["1.USA", "2.France", "3.Brazil"]
    }
]
print(medalResults)
print(medalResults[0].get("podium")[0][:1])
print(medalResults[0].get("podium")[0][:1]==1)

def createMedalTable(results):
    # Use the results object above to create a medal table
    # The winner gets 3 points, second place 2 points and third place 1 point
    medalTable = {}
    for sport in results:
        for pos in sport.get("podium"):
            if pos[2:] not in medalTable:
                medalTable[pos[2:]] = 0
                #print(medalTable)
            #print(pos[:1])
            #print(pos[2:])
            num = medalTable[pos[2:]]
            #print(medalTable[pos[2:]])
            temp = {}
            
            if pos[:1] is 1:
                # num+=3
                # temp = {pos[2:]:num}
                #print(temp)
                print("first")
                medalTable[pos[2:]] +=3
            elif pos[:1] is 2:
                # num+=2
                # temp = {pos[2:]:num}
                print("sec")
                medalTable[pos[2:]] += num+2
            elif pos[:1] is 3:
                # num+=1
                # temp = {pos[2:]:num}
                print("thrid")
                medalTable[pos[2:]] += num+1
            #print(temp)
            medalTable.update(temp)
    print(medalTable)
    return medalTable
medalTable = createMedalTable(medalResults)
#print(medalTable)
#print(medalTable["China"])
def test_function():
    #This it the test function, please don't change me
    medalTable = createMedalTable(medalResults)
    expectedTable = {
        "Italy": 4,
        "France": 4,
        "ROC": 4,
        "USA": 3,
        "Qatar": 3,
        "China": 3,
        "Germany": 2,
        "Brazil": 1,
        "Belarus": 1,
    }
    assert medalTable == expectedTable
