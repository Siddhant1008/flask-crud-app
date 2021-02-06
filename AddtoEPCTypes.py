from bookmanager import EPCTypes, db

file2 = open('EPCAttributesTypes.txt', 'r', encoding="utf8")
AttTypesLines = file2.readlines()
list1 = []
AttTypesList = []
for line in AttTypesLines:
    list1.append(line.strip().split())

for i in list1:
    if len(i) == 2:
        if i[0] != "":
            AttTypesList.append(i)
    elif len(i) == 1:
        if i[0] != "":
            i.append("")
            AttTypesList.append(i)

for i in AttTypesList:



    epctypesObj = None
    try:
        epctypesObj = EPCTypes(AttName=str(i[0]), AttType=str(i[1]))
        db.session.add(epctypesObj)
    except Exception as e:
        print("Failed to add AttributeTypes")
        print(e)

db.session.commit()


