# --- Gerrit Coetzee 2018
import logging
import random
import segno

import pickleking
import dataverifiers

dataking_version = "0.0"

saver = pickleking.pickleking
verify = dataverifiers


class dataking(saver):
    def __init__(self, qrdir="qrcodes", imgdir="imgdir"):
        super().__init__()
        self._qrdir = qrdir
        self._imgdir = imgdir
        # self._data = {}
        print("dataking initialized")

    def generate_key(self):
        # return only the last 8 digits of the hex as a string - this will be the unique key
        key = str(hex(random.randint(0, 4294967295)))[2:]
        if key not in self._data:  # in case I win the goddamn lottery
            logging.info("new item key genearted: " + key)
            return key
        else:
            logging.debug("duplicate item key! wow!")
            self.generate_key()

    def new_entry(self):
        key = self.generate_key()
        self._data[key] = {
            "name": "default", "holds": [], "data": self.generate_data_template(key)}
        return key

    def modify_data(self, key, newdata):
        errorlist = {}
        print(self._data[key]['data'])
        print(newdata)
        if key in self._data:
            data = self._data[key]['data']
            for key in newdata:
                if key in data:
                    data[key] = newdata[key]
                else:
                    errorlist[key] = newdata[key]
        else:
            return "error"
        return errorlist

    def add_data(self, key, data):
        accepted_keys = {'hurt':verify.verify_text}
        errorlist=[{},[]]
        if key in self._data:
            for addkey in data:
                if addkey in accepted_keys:
                    checkdata = accepted_keys[addkey](data[addkey])
                    if checkdata[0]==True:
                        self._data[key]['data'][addkey] = data[addkey]
                    else: 
                        errorlist[1].append({addkey:data[addkey], "error":checkdata[1]})
                else:
                    errorlist[0][addkey]=data[addkey]
            return errorlist        
        else:
            return "error"

    def generate_data_template(self, key):
        data = {}
        data['version'] = dataking_version
        data['description'] = ""
        data['qty'] = 0
        data['image'] = ""
        return data

    def save_data(self):
        super().save_data(self._data)




if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    print("main!")
    data = dataking()
    # data.generate_key()
    key = data.new_entry()
    x = data.modify_data(
        key, {"description": "cool stuff!!", "shirt": "it does", "test":"no","testtest":"no"})
    print(x)
    print("______")
    print(data.add_data(key,x))
    key = data.new_entry()
    x = data.modify_data(
        key, {"description": "cool stuff!!", "shirt": "it does", "test":"no","testtest":"no"})
    print(x)
    print("______")
    print(data.add_data(key,x))
    key = data.new_entry()
    x = data.modify_data(
        key, {"description": "cool stuff!!", "shirt": "it does", "test":"no","testtest":"no"})
    print(x)
    print("______")
    print(data.add_data(key,x))
    key = data.new_entry()
    x = data.modify_data(
        key, {"description": "cool stuff!!", "shirt": "it does", "test":"no","testtest":"no"})
    print(x)
    print("______")
    print(data.add_data(key,x))
    key = data.new_entry()
    x = data.modify_data(
        key, {"description": "cool stuff!!", "shirt": "it does", "test":"no","testtest":"no"})
    print(x)
    print("______")
    print(data.add_data(key,x))
    key = data.new_entry()
    x = data.modify_data(
        key, {"description": "cool stuff!!", "hurt": "it does", "test":"no","testtest":"no"})
    print(x)
    print("______")
    print(data.add_data(key,x))

    data.save_data()

    # print(data._data)

    x = data.load_data()

    print(x)
