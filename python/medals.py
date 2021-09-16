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
print(medalResults[0].get("podium")[0][2:])

def createMedalTable(results):
    # Use the results object above to create a medal table
    # The winner gets 3 points, second place 2 points and third place 1 point
    medalTable = {}
    for sport in results:
        print(sport.get("podium"))
        for pos in sport.get("podium"):
            if pos[2:] not in medalTable:
                medalTable[pos[2:]] = 0
            print(pos[:1])
            if pos[:1] == 1:
                medalTable[pos[2:]] += 3
            elif pos[:1] == 2:
                medalTable[pos[2:]] += 2
            elif pos[:1] == 3:
                medalTable[pos[2:]] += 1


    return medalTable

print(createMedalTable(medalResults))
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
