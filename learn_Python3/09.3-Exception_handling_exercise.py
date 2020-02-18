#cardictionary = {"Make": "BMW", "Model": "355i","Year": 2009}


def testError():
    try:
        cardictionary = {"Make": "BMW", "Model": "355i", "Year": 2009}
        print(cardictionary["Make"])
        print(cardictionary["Color"])

    except:

        print("I see an error")
        raise Exception("THis is where i'd raise said error")

    finally:
        print("I'm always executing this code")


testError()

"""
The dictionary can go either inside or outside the function
"""