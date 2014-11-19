import entish
import json
import re

json_data=open("../data/entmoot.json").read()
story = json.loads(json_data)



#s = re.sub(r'[^\w\s]','',s)
def process(chapter):
    title = chapter["title"]
    sentences = chapter["sentences"]
    print("\chapter{"+title+"}")
    for sentence in sentences:
        words = re.sub(r'[^\w\s]','',sentence["english"]).lower().split(" ")
        fw = words[0]
        gen = entish.EntishGenerator(name=fw)
        fs = gen.generate_entish().capitalize().split(" ")
        sidenote = "\sidenote{" + sentence["sidenote"] + "}"
        fs.insert(1,sidenote)
        fs = " ".join(fs)
        print(fs)
        print("")
        for word in words[1:]:
            gen = entish.EntishGenerator(name=word)
            print(gen.generate_entish().capitalize() + ".")
            print("")
        
print(open("../data/pretext.latex").read())
for chapter in story["chapters"]:
    process(chapter)
print(open("../data/posttext.latex").read())
