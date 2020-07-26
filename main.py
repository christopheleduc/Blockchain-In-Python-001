#!/usr/bin/env python
# main : exploite le principe de fonctionnement d'une Blockchain
# -*- coding: utf-8 -*-

# This file is part of Blockchain In Python with Python3
# See wiki doc for more information
# Copyright (C) CryptoDox <cryptodox@cryptodox.net>
# This program is published under a GPLv2 license

__author__ = "CodeKiller"
__date__ =  "18 juillet 2020"

import hashlib, json, pprint, time, datetime

"""
Blockchain experiment in Python
"""

__version__ = "1.0.1 Beta"

class Block():

    # posix_now = time.time()
    # d = datetime.datetime.fromtimestamp(posix_now)
    this_time = datetime.datetime.utcnow() # datetime.datetime type
    epoch_time = this_time.timestamp()      # posix time or epoch time

    def __init__(self, position, date_creation = epoch_time, infos = '0', precedantHash = ''):
        self.position = position
        self.date_creation = date_creation
        self.infos = infos
        self.precedantHash = precedantHash
        self.hash = self.hashBlock()

    def hashBlock(self):
        return hashlib.sha256(bytes(str(hashlib.sha256(bytes(str(self.position) + self.precedantHash + str(self.date_creation) + json.dumps(self.infos, separators=(',', ':')), 'utf-8')).hexdigest()), 'utf-8')).hexdigest()

class Blockchain():
    def __init__(self):
        self.chain = [self.genesisBlock()]
    
    def genesisBlock(self):
        return Block(0, 1525183714.464137, "Cointelegraph:CFTC Chairman On Crypto Regulation: ‘I Don’t See It Being Resolved Anytime Soon’", "0")

    def lastBlock(self):
        # return self.chain[len(self.chain) -1]
        return self.chain[ -1]
    
    def addBlock(self, newBlock):
        newBlock.precedantHash = self.lastBlock().hash
        newBlock.hash = newBlock.hashBlock()
        self.chain.append(newBlock)
    
    def secureChain(self):
        for i in range (1, len(self.chain)):
            ceBlock = self.chain[i]
            precedantBlock = self.chain[i - 1]

            if ceBlock.hash != ceBlock.hashBlock():
                return False

            if ceBlock.precedantHash != precedantBlock.hash:
                return False

        return True


if __name__=="__main__":
    c = Blockchain()
    # On ajoute 2 Block
    c.addBlock(Block(1, infos=[('montant', 5)] ))
    c.addBlock(Block(2, infos= [('montant', 12)] ))

    # On affiche les Block
    print('**************************************************')
    for i in range (0, len(c.chain)):
        #print(c.chain[i])
        print('--------------------------------------------------------')
        print ("BLOCK:   " + json.dumps(c.chain[i].position, separators=(',', ':')))
        print ("DATE:    " + "Posix: " + "[" + json.dumps(c.chain[i].date_creation, separators=(',', ':')) + "];" + " Convert: " + "[" + str(datetime.datetime.fromtimestamp (float(c.chain[i].date_creation)))+ "];")
        print ("DATA:    " + json.dumps(c.chain[i].infos, separators=(': ', ':')))
        print ("HASH:    " + json.dumps(c.chain[i].hash, separators=(',', ':')))
        print ("PreHASH: " + json.dumps(c.chain[i].precedantHash, separators=(',', ':')))
        print('--------------------------------------------------------')

    print('**************************************************')
    print('##################################################')
    # On verifie l'intégrité des Block
    print ('Intégrité Blockchain ? ' + str(c.secureChain()))

    # On falsifie un Block
    c.chain[1].infos = [('montant', 100)]
    c.chain[1].hash = c.chain[1].hashBlock()
    print('**************************************************')
    # On affiche les Block
    for i in range (0, len(c.chain)):
        #print(c.chain[i])
        print('--------------------------------------------------------')
        print ("BLOCK:   " + json.dumps(c.chain[i].position, separators=(',', ':')))
        print ("DATE:    " + "Posix: " + "[" + json.dumps(c.chain[i].date_creation, separators=(',', ':')) + "];" + " Convert: " + "[" + str(datetime.datetime.fromtimestamp (float(c.chain[i].date_creation)))+ "];")
        print ("DATA:    " + json.dumps(c.chain[i].infos, separators=(': ', ':')))
        print ("HASH:    " + json.dumps(c.chain[i].hash, separators=(',', ':')))
        print ("PreHASH: " + json.dumps(c.chain[i].precedantHash, separators=(',', ':')))
        print('--------------------------------------------------------')

    print('**************************************************')
    print('##################################################')
    # On verifie l'intégrité des Block
    print ('Intégrité Blockchain ? ' + str(c.secureChain()))
    

# motdepass = input("String2Hash ? \n>")

# hashPass = hashlib.sha256(bytes(motdepass, 'utf-8')).hexdigest()

# print (hashPass)