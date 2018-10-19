# --- Gerrit Coetzee 2018
import logging
import random
import segno

import stackutils
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

        self.accepted_keys = {'description': verify.verify_text,
                              'qty': verify.verify_decimal,
                              'image': verify.verify_image}

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
            "holds": [], "data": self.generate_data_template(key)}
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
        errorlist = [{}, []]
        if key in self._data:
            for addkey in data:
                if addkey in self.accepted_keys:
                    checkdata = self.accepted_keys[addkey](data[addkey])
                    if checkdata[0] == True:
                        self._data[key]['data'][addkey] = data[addkey]
                    else:
                        errorlist[1].append(
                            {addkey: data[addkey], "error": checkdata[1]})
                else:
                    errorlist[0][addkey] = data[addkey]
            return errorlist
        else:
            return "error"

    def generate_data_template(self, key):
        data = {}
        data['name'] = "default"
        data['dataking_version'] = dataking_version
        return data

    def put_in(self, inkey, boxkey):
        '''This inserts an item into a box!'''
        if (boxkey in self._data) and (inkey in self._data):
            if inkey not in self._data[boxkey]['holds']:
                self._data[boxkey]['holds'].append(inkey)
            else:
                return "already in box!"
        else:
            return "error"

    def take_out(self, outkey, boxkey):
        if (boxkey in self._data) and (outkey in self._data):
            if outkey in self._data[boxkey]['holds']:
                self._data[boxkey]['holds'].remove(outkey)
            else:
                return "error"
        else:
            return "error"

    def save_data(self):
        super().save_data(self._data)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    print("main!")
    data = dataking()

    key = data.new_entry()
    x = data.modify_data(
        key, {"name": "cool things!", "description": "cool stuff!!", "shirt": "it does", "test": "no", "testtest": "no"})

    print("______")
    print(data.add_data(key, x))
    key2 = data.new_entry()

    data.put_in(key2, key)
    print(data.put_in(key2, key))

    data.take_out(key2, key)
    print(data.put_in(key2, key))

    key2 = data.new_entry()
    data.take_out(key2, key)

    print(data.put_in(key2, key))
    key2 = data.new_entry()

    key2 = data.new_entry()
    key2 = data.new_entry()
    key2 = data.new_entry()

    data.save_data()

    # print(data._data)

    x = data.load_data()

    stackutils.dump(x,4)
