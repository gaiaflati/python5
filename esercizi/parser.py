import sys, json

mylist_1 = "['mario', 'gino','lucrezia']"

mylist_2 = ['mario', 'gino','lucrezia']


def serializza(mylist):
    lista=str(mylist)
    print(type(lista))
    return lista

print(serializza(mylist_2))



def deserializza(mylist):
    return (eval(mylist))
print(deserializza(mylist_1))

        
mydict_1 = { "brand": "Ford",
"electric": False,
"year": 1964,
"colors": ["red", "white", "blue"]}

mydict_2 = "{ 'brand':   'Ford'," + \
"'electric': False," + \
"'year': 1964," + \
"'colors': ['red', 'white', 'blue']}"



#dict_1 = json.loads(mydict_2) #deserializzazione

def SerializaJson(dData: dict, file_path)-> bool:
    str1= json.dumps(dData) #serializzazione
    try:
        with open(file_path, "w") as p:
            p.write(str1)
        return True
    
    except:
        return False
   

out=(SerializaJson(mydict_1, "esserialize.json"))


def DeserializeJson(file_path)-> dict:
    with open(file_path, "r") as reader: 
	    return json.load(reader)
bb=print(DeserializeJson("esserialize.json"))


    
