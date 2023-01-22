import pickle
import os
def add_contact(contact: dict) -> bool:
    try:
        os.mkdir('base/'+str(contact['user_id']))
        os.mkdir('base/'+str(contact['user_id'])+"/photos")
        with open('info',"rb") as file:
            file = pickle.Unpickler(file)
            m = file.load()
        m.append(contact)
        with open('info','wb') as file:
            pickle.dump(m,file)
        print("acc: add_contact")
        return True
    except Exception as e:
        print("err: add_contact")
        print(e)
        return False
def read_contact() -> list:
    try:
        with open('info',"rb") as file:
            m = pickle.load(file)
            file.close()
        print("acc: read_contact")
        return m
    except:
        print('err: read_contact')
        return [False]
def tek_id(id: int) -> bool:
    try:
        os.mkdir('base/'+str(id))
        os.mkdir('base/'+str(id)+"/photos")
        with open('info',"rb") as file:
            m = pickle.load(file)
            file.close()
        for i in m:
            if i["user_id"] == id:
                print("acc: tek_id")
                return True
        print("acc: tek_id")
        return False
    except:
        print("err: tek_contact")
        return False

