#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 13 Synthesizing Tasks"""

import os
import pickle


class PickleCache(object):
    """A file-backed caching engine.
    Stores data to a named or default filepath.
    Args:
        file_path(string, optional): The name and location of a file to be used
        for storing the data as a string.
        autosync(bool, optional): Defaults to False, if True, auto-syncs changes
        to disc cache.
    Attributes:
        file_path(string, optional): The name and location of a file to be used
        for storing the data as a string.
        autosync(bool, optional): Defaults to False, if True, auto-syncs changes
        to disc cache.
    """

    def __init__(self, file_path='datastore.pkl', autosync=False):
        """Constructor for PickleCache() class.
        Args:
            file_path(string, optional): The name and location of a file to be
            used for storing the data as a string.
            autosync(bool, optional): Defaults to False, if True, auto-syncs
            changes to disc cache.
        Attributes:
            file_path(string, optional): The name and location of a file to be
            used for storing the data as a string.
            autosync(bool, optional): Defaults to False, if True, auto-syncs
            changes to disc cache.            
        """
        self.__file_path = file_path
        self.__data = {}
        self.autosync = autosync
        self.load()

    def __setitem__(self, key, value):
        """Magic method for defining behavior for items assigned to key and
        value.
        Args:
            key(various): the name of the item to be assigned to a dictionary
            key.
            value(various): The name of an item to be assgined to a dictionary
            value.
        """
        self.key = key
        self.value = value
        self.__data[key] = value

    def __len__(self):
        """Magic method for the len() function.
        Allows PickleCache data dict to be called inside of len() function.
        """
        return len(self.__data)

    def __getitem__(self, key):
        """Magic method for defining behavior for items accssed, using the key
        of the data dictionary.
        """
        return self.__data[key]

    def __delitem__(self, key):
        """Method for defining behavior for when an item is deleted using
        the key of the data dictionary.
        """
        del self.__data[key]

    def load(self):
        """Checks the filepath and file size and if they meet parameters, opens
        the file and loads the data using Pickle."""
        fexists = os.path.exists(self.file_path)
        fsize = os.path.getsize(self.file_path)
        if fexists and fsize > 0:
            fhandler = open(self.file_path, 'r')
            mydata = pickle.load(fhandler)
            self.__data.update(mydata)
            fhandler.close()

    # def flush()
       # """Docstring."""
