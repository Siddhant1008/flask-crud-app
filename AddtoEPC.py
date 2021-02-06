from bookmanager import EPC, db

file1 = open('lte_epc.cfg', 'r', encoding="utf8")
Lines = file1.readlines()
list1 = []
cleanList = []

for line in Lines:
    list1.append(line.strip().split())

for i in list1:
    if len(i) == 2:
        if i[0] != "":
            cleanList.append(i)
    elif len(i) == 1:
        if i[0] != "":
            i.append("")
            cleanList.append(i)




#print(cleanList)
for i in cleanList:

    epcObj = None
    try:
        #print(i[0], i[1])
        epcObj = EPC(AttName=str(i[0]), AttValue=str(i[1]))
        db.session.add(epcObj)

    except Exception as e:
        print("Failed to add Attribute")
        print(e)

db.session.commit()


