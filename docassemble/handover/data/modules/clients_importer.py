import pandas as pd
from docassemble.base.util import DAFileList, DADict, DAList, DAObject

class MJFClientData(DAObject):
    """
    This class is simply an object that populates and
    stores a list of invitees.  Invitees are stored in
    the public `self.clients_list` 
    """

    def init(self, *pargs, **kwargs):
        """
        Not sure why this is called `init` and not
        `__init__` but this seems how DA objects are 
        initialised.

        Parameters
        ----------
        Standard params for initialising `super()`
        """
        super().init(*pargs, **kwargs)
        self.clients_list = DAList()
        self.clients_list.auto_gather = False
        self.populated = False

    def read_in_data(self, data_file):
        """
        Reads data from an excel file and populates the
        internal DAList

        Use Pandas to read the spreadsheet into a 
        data map

        Parameters
        ----------
        data_file : DAFileList() with a single file
        """
        file_path = data_file.path()
        self._data_map = pd.read_excel(file_path)
        self.populate_client_data()
        self.populated = True

    def populate_client_data(self):
        # Will only return required fields
        # TODO: field sanity checking

        # a DAList of DADicts ie:
        # - first_name: 
        #   last_name:
        #   email:
        #   organisation:
        # - first_name
        #   ...
        self.clients_list.clear()
        self.clients_list.auto_gather = False
        for index, row in self._data_map.iterrows():
            result_item = DADict()
            result_item['first_name'] = row['First Name']
            result_item['last_name'] = row['Last Name']
            result_item['email'] = row['Email']
            result_item['app_name'] = row['Name of App']
            result_item['app_link'] = row['Link to App']
            result_item['licence_agreement'] = row['Licence Agreement']
            self.clients_list.append(result_item)

    def get_populated(self):
        return self._populated
