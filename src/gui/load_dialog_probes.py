"""
Basic gui class designed with QT designer
"""
# import sip
# sip.setapi('QVariant', 2)# set to version to so that the old_gui returns QString objects and not generic QVariants
import os

from PyQt4 import QtGui
from PyQt4.uic import loadUiType

from src.core.read_write_functions import load_b26_file

# load the basic old_gui either from .ui file or from precompiled .py file
try:
    # import external_modules.matplotlibwidget
    Ui_Dialog, QDialog = loadUiType('load_dialog.ui') # with this we don't have to convert the .ui file into a python file!
except (ImportError, IOError):
    # load precompiled old_gui, to complite run pyqt_uic basic_application_window.ui -o basic_application_window.py
    from src.gui.load_dialog import Ui_Dialog
    from PyQt4.QtGui import QMainWindow
    from PyQt4.QtGui import QDialog
    print('Warning!: on the fly conversion of load_dialog.ui file failed, loaded .py file instead!!')



class LoadDialogProbes(QDialog, Ui_Dialog):
    """
LoadDialog(intruments, scripts, probes)
    - type: either script, instrument or probe
    - loaded_elements: dictionary that contains the loaded elements
ControlMainWindow(settings_file)
    - settings_file is the path to a json file that contains all the settings for the old_gui
Returns:
    """

    def __init__(self, elements_old={}, filename=None):
        super(LoadDialogProbes, self).__init__()
        self.setupUi(self)

        if filename is None:
            filename = ''
        self.txt_probe_log_path.setText(filename)

        # create models for tree structures, the models reflect the data
        self.tree_infile_model = QtGui.QStandardItemModel()
        self.tree_infile.setModel(self.tree_infile_model)
        QtGui.QStandardItemModel().reset()

        self.tree_infile_model.setHorizontalHeaderLabels(['Instrument', 'Probe'])
        self.tree_loaded_model = QtGui.QStandardItemModel()
        self.tree_loaded.setModel(self.tree_loaded_model)
        self.tree_loaded_model.setHorizontalHeaderLabels(['Instrument', 'Probe'])
        # connect the buttons
        self.btn_open.clicked.connect(self.open_file_dialog)

        # create the dictionaries that hold the data
        #   - elements_old: the old elements (scripts, instruments) that have been passed to the dialog
        #   - elements_from_file: the elements from the file that had been opened
        self.elements_selected = {}
        for element_name, element in elements_old.iteritems():
            self.elements_selected.update( {element_name: {'class': element.__class__.__name__ , 'settings':element.settings}})
        if os.path.isfile(filename):
            self.elements_from_file = self.load_elements(filename)
        else:
            self.elements_from_file = {}

        # fill trees with the data
        self.fill_tree(self.tree_loaded, self.elements_selected)
        self.fill_tree(self.tree_infile, self.elements_from_file)

        self.tree_infile.selectionModel().selectionChanged.connect(self.show_info)
        self.tree_loaded.selectionModel().selectionChanged.connect(self.show_info)

        self.tree_infile_model.itemChanged.connect(self.item_dragged_and_dropped)
        self.tree_loaded_model.itemChanged.connect(self.item_dragged_and_dropped)


    def item_dragged_and_dropped(self):

        index = None
        self.tree_infile_model.itemChanged.disconnect()
        self.tree_loaded_model.itemChanged.disconnect()

        index_infile = self.tree_infile.selectedIndexes()
        index_loaded = self.tree_loaded.selectedIndexes()
        if index_infile != []:
            index = index_infile[0]
            dict_target = self.elements_selected
            dict_source = self.elements_from_file
        elif index_loaded != []:
            index = index_loaded[0]
            dict_source = self.elements_selected
            dict_target= self.elements_from_file

        if index is not None:

            parent = index.model().itemFromIndex(index).parent()
            if parent is None:
                instrument_name = str(index.model().itemFromIndex(index).text())
                probe_names = [str(index.model().itemFromIndex(index).child(i).text()) for i in range(index.model().itemFromIndex(index).rowCount())]
            else:
                instrument_name = str(parent.text())
                probe_names = [str(index.model().itemFromIndex(index).text())]

            if not instrument_name in dict_target.keys():
                dict_target.update({instrument_name: {probe_name:instrument_name for probe_name in probe_names}})
                for probe_name in probe_names:
                    del dict_source[instrument_name][probe_name]
            else:
                for probe_name in probe_names:
                    if not probe_name in dict_target[instrument_name].keys():
                        dict_target[instrument_name].update({probe_name: instrument_name})
                        del dict_source[instrument_name][probe_name]

            if instrument_name in dict_source and  dict_source[instrument_name] == {}:
                del dict_source[instrument_name]
            if instrument_name in dict_target and dict_target[instrument_name] == {}:
                del dict_target[instrument_name]

        else:
            #
            raise TypeError

        self.fill_tree(self.tree_loaded, self.elements_selected)
        self.fill_tree(self.tree_infile, self.elements_from_file)
        self.tree_infile_model.itemChanged.connect(self.item_dragged_and_dropped)
        self.tree_loaded_model.itemChanged.connect(self.item_dragged_and_dropped)

    def show_info(self):
        """
        displays the doc string of the selected element
        """
        # print('INFO NOT IMPLEMENTED YET. Check back later....')
        sender = self.sender()
        tree = sender.parent()
        index = tree.selectedIndexes()
        info = ''
        if index != []:
            index = index[0]
            name = str(index.model().itemFromIndex(index).text())

            if name in set(self.elements_from_file.keys() + self.elements_selected.keys()):
                probe_name = None
                instrument_name = name
            else:
                instrument_name = str(index.model().itemFromIndex(index).parent().text())
                probe_name = name



            module = __import__('src.instruments', fromlist=[instrument_name])
            if probe_name is None:
                info = getattr(module, instrument_name).__doc__
            else:
                if probe_name in getattr(module, instrument_name)._PROBES.keys():
                    info = getattr(module, instrument_name)._PROBES[probe_name]

        if info is not None:
            self.lbl_info.setText(info)

    def open_file_dialog(self):
        """
        opens a file dialog to get the path to a file and
        """
        dialog = QtGui.QFileDialog
        filename = dialog.getOpenFileName(self, 'Select a file:', self.txt_probe_log_path.text())
        if str(filename)!='':
            self.txt_probe_log_path.setText(filename)
            # load elements from file and display in tree
            elements_from_file = self.load_elements(filename)
            self.fill_tree(self.tree_infile, elements_from_file)
            # append new elements to internal dictionary
            self.elements_from_file.update(elements_from_file)
    def load_elements(self, filename):
        """
        loads the elements from file filename
        """
        input_data = load_b26_file(filename)
        if isinstance(input_data, dict) and 'probes' in input_data:
            return input_data['probes']
        else:
            return {}

    def fill_tree(self, tree, input_dict):
        """
        fills a tree with nested parameters
        Args:
            tree: QtGui.QTreeView
            parameters: dictionary or Parameter object

        Returns:

        """


        def removeAll(tree):

            if tree.model().rowCount() > 0:
                for i in range(0, tree.model().rowCount()):
                    item = tree.model().item(i)
                    del item
                    tree.model().removeRows(0, tree.model().rowCount())
                    tree.model().reset()

        def add_probe(tree, instrument, probes):
            item = QtGui.QStandardItem(instrument)
            item.setEditable(False)
            for key, value in probes.iteritems():
                child_name = QtGui.QStandardItem(key)
                child_name.setDragEnabled(True)
                child_name.setSelectable(True)
                child_name.setEditable(False)
                item.appendRow(child_name)
            tree.model().appendRow(item)

        removeAll(tree)

        for index, (instrument, probes) in enumerate(input_dict.iteritems()):
            add_probe(tree, instrument, probes)
            # tree.setFirstColumnSpanned(index, self.tree_infile.rootIndex(), True)

    def getValues(self):
        """
        Returns: the selected elements
        """

        return self.elements_selected

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    folder = "C:/Users/Experiment/PycharmProjects/PythonLab/b26_files/probes_auto_generated/"
    dialog = LoadDialogProbes(elements_old={},
                              filename=folder)
    dialog.show()
    dialog.raise_()
    if dialog.exec_():
        probes = dialog.getValues()

        print(probes)
        # added_probes = set(probes.keys()) - set(self.probes.keys())
        # removed_probes = set(self.probes.keys()) - set(probes.keys())
        sys.exit(app.exec_())





    # import sys
    # app = QtGui.QApplication(sys.argv)
    # folder = "C:/Users/Experiment/PycharmProjects/PythonLab/b26_files/instruments_auto_generated/"
    # dialog = LoadDialog(elements_type="instruments", elements_old={},
    #                     filename=folder)
    # dialog.show()
    # dialog.raise_()
    # if dialog.exec_():
    #     probes = dialog.getValues()
    #
    #     print(probes)
    #     # added_probes = set(probes.keys()) - set(self.probes.keys())
    #     # removed_probes = set(self.probes.keys()) - set(probes.keys())
    #     sys.exit(app.exec_())