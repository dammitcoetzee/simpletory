# --- Gerrit Coetzee
# --- 10/17/2018
# --- LabelGen
# --- Manages the creation of any assets for the printing of labels inside simpletory
## This code currently doesn't do what it's supposed to. A lot of its functionality is now handled by dataking

import json
import logging
import os

# Segno is a QR Code and Micro QR Code encoder which has no further dependencies.
# https://github.com/heuer/segno/
import segno


class LabelGen(object):
    ''' main class for label generator '''

    def __init__(self, name="default", photo="default_image", qr="default", qrdir="labels_qrcode", jsondir="labels_json"):
        logging.debug('Label Object Created')

        self.name = name
        self.photo = photo
        self.qr = qr

        self._qrdir = qrdir
        self._jsondir = jsondir

    def generate_qr(self):
        ''' This generates the qr doe in the qrdirectory defined at the start of the object '''
        qr = segno.make(self._qr[0], micro=False)
        # logging.info("is the qr code micro? " + str(qr.is_micro))
        return qr

    def generate_json(self):
        ''' this generates a json output of the label '''
        logging.debug("generate_json called")
        input = {}
        input['name'] = self._name
        input['qr'] = self._qr
        input['photo'] = self._photo

        output = json.dumps(input, sort_keys=True,
                            indent=4, separators=(',', ': '))
        return output

    def save_json(self):
        ''' writes the json to a file in jsondir, this doesn't take an argument, it calls generate_json '''
        # Create target Directory if don't exist
        if not os.path.exists(self._jsondir):
            os.mkdir(self._jsondir)
            logging.info("Directory " + self._jsondir + " Created ")
        else:
            logging.info("Directory " + self._jsondir + " already exists")

        f = open("./"+self._jsondir+"/"+self.name+".json", "w")
        f.write(self.generate_json())

    def save_qr(self, qr):
        ''' Saves the qr code to qrdir'''
        logging.debug("Saving QR to File")
        # Create target Directory if don't exist
        if not os.path.exists(self._qrdir):
            os.mkdir(self._qrdir)
            logging.info("Directory " + self._qrdir + " Created ")
        else:
            logging.info("Directory " + self._qrdir + " already exists")

        qr.save("./"+self._qrdir+"/"+self._qr[1], scale=10, color='darkblue')

    # Name getter, setter, deleter
    @property
    def name(self):
        # logging.debug("name getter called")
        print("hello")
        return self._name

    @name.setter
    def name(self, value):
        # logging.debug("name setter, value:" + str(value))
        self._name = value

    @name.deleter
    def name(self):
        # logging.debug("name deleter called")
        del self._name

    # Photo getter, setter, deleter

    @property
    def photo(self):
        # logging.debug("photo getter called")
        return self._photo

    @photo.setter
    def photo(self, value):
        # logging.debug("photo setter, value:" + str(value))
        self._photo = [str(value), str(value)+"_photo"+".png"]

    @photo.deleter
    def photo(self):
        #logging.debug("photo deleter called")
        del self._photo

    # QR getter, setter, deleter

    @property
    def qr(self):
        #logging.debug("qr getter called")
        return self._qr

    @qr.setter
    def qr(self, value):
        #logging.debug("qr setter, value:" + str(value))
        self._qr = [str(value), str(value)+"_qr"+".png"]

    @qr.deleter
    def qr(self):
        #logging.debug("qr detleter called")
        del self._qr


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    label = LabelGen()

    # print(label.qrdir)
    qr = label.generate_qr()
    label.save_qr(qr)
    label.save_json()
