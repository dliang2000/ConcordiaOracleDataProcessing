import json
import pandas as pd

with open("../data.json", "r") as f:
    data = json.load(f)

json_list = []
headers = ["repository", "url", "type", "description", "validation", "detectionTools", "validators"]
for i in range(len(data)):
    numberOFRefactorings = len(data[i]["refactorings"])
    refactorings = data[i]["refactorings"]
    for j in range(numberOFRefactorings):
        if ((refactorings[j]["type"] == "Extract Method")
            and ("public test" in refactorings[j]["description"] or "protected test" in refactorings[j]["description"])):
            temp_list = []
            temp_list.append(data[i]["repository"])
            temp_list.append(data[i]["url"])
            temp_list.append(refactorings[j]["type"])
            temp_list.append(refactorings[j]["description"])
            temp_list.append(refactorings[j]["validation"])
            temp_list.append(refactorings[j]["detectionTools"])
            temp_list.append(refactorings[j]["validators"])
            json_list.append(temp_list)

dfObj = pd.DataFrame(json_list, columns=headers)
dfObj.to_csv("oracle_refactoring_processed.csv", index=False)
