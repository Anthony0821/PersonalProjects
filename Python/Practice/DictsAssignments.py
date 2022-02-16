def makes_scores_dict(names, scores):
    score_dict = {}
    
    for x in range(len(names)):
        score_dict[names[x]] = int(scores[x]) # when makeing this dictionary its important to make th index key as shown in this line
    return(score_dict)

scores = [75,65,85,45,99]
names = ["Tom","Joe","Alice", "Bob", "Jane"]
rtndict = makes_scores_dict(names, scores)

if "Joe" in rtndict:
    print(rtndict.get("Joe"))

rtndict["Ralph"] = 80