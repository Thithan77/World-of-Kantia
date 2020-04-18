class Inv:
    list = [0]*30;
    def add(what,hMany):
        founded = False
        for key,value in enumerate(Inv.list):
            if(value["type"] == what):
                Inv.list[key]["n"] += 1;
                print("Added "+str(hMany)+" "+str(what)+" at pose "+str(key));
                founded = True;
                break;
        if(founded == False):
            for key,value in enumerate(Inv.list):
                if(value["type"] == "null"):
                    print("Added "+str(hMany)+" "+str(what)+" at pose "+str(key));
                    Inv.list[key]["n"] += 1;
                    Inv.list[key]["type"] = what
                    break;
for loop in range(30):
    Inv.list[loop] = {"type":"null","n":0}
