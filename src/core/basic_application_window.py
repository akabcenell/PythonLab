# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'basic_application_window.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1665, 810)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_scripts = QtGui.QWidget()
        self.tab_scripts.setObjectName(_fromUtf8("tab_scripts"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tab_scripts)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.btn_plot_script = QtGui.QPushButton(self.tab_scripts)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_plot_script.setFont(font)
        self.btn_plot_script.setObjectName(_fromUtf8("btn_plot_script"))
        self.horizontalLayout_4.addWidget(self.btn_plot_script)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.btn_store_script_data = QtGui.QPushButton(self.tab_scripts)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_store_script_data.setFont(font)
        self.btn_store_script_data.setObjectName(_fromUtf8("btn_store_script_data"))
        self.horizontalLayout_4.addWidget(self.btn_store_script_data)
        self.btn_load_scripts = QtGui.QPushButton(self.tab_scripts)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_load_scripts.setFont(font)
        self.btn_load_scripts.setObjectName(_fromUtf8("btn_load_scripts"))
        self.horizontalLayout_4.addWidget(self.btn_load_scripts)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.tree_scripts = QtGui.QTreeWidget(self.tab_scripts)
        self.tree_scripts.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tree_scripts.sizePolicy().hasHeightForWidth())
        self.tree_scripts.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tree_scripts.setFont(font)
        self.tree_scripts.setAutoFillBackground(False)
        self.tree_scripts.setLineWidth(1)
        self.tree_scripts.setMidLineWidth(0)
        self.tree_scripts.setEditTriggers(QtGui.QAbstractItemView.AllEditTriggers)
        self.tree_scripts.setAlternatingRowColors(True)
        self.tree_scripts.setWordWrap(True)
        self.tree_scripts.setHeaderHidden(False)
        self.tree_scripts.setObjectName(_fromUtf8("tree_scripts"))
        self.tree_scripts.header().setDefaultSectionSize(200)
        self.tree_scripts.header().setHighlightSections(True)
        self.verticalLayout_4.addWidget(self.tree_scripts)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.btn_start_script = QtGui.QPushButton(self.tab_scripts)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_start_script.setFont(font)
        self.btn_start_script.setObjectName(_fromUtf8("btn_start_script"))
        self.horizontalLayout_5.addWidget(self.btn_start_script)
        self.btn_stop_script = QtGui.QPushButton(self.tab_scripts)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_stop_script.setFont(font)
        self.btn_stop_script.setObjectName(_fromUtf8("btn_stop_script"))
        self.horizontalLayout_5.addWidget(self.btn_stop_script)
        self.progressBar = QtGui.QProgressBar(self.tab_scripts)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.progressBar.setFont(font)
        self.progressBar.setToolTip(_fromUtf8(""))
        self.progressBar.setStatusTip(_fromUtf8(""))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.horizontalLayout_5.addWidget(self.progressBar)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem1 = QtGui.QSpacerItem(138, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.lbl_time_estimate = QtGui.QLabel(self.tab_scripts)
        self.lbl_time_estimate.setObjectName(_fromUtf8("lbl_time_estimate"))
        self.horizontalLayout_6.addWidget(self.lbl_time_estimate)
        spacerItem2 = QtGui.QSpacerItem(268, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 1)
        self.horizontalLayout_6.setStretch(2, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.tabWidget.addTab(self.tab_scripts, _fromUtf8(""))
        self.tab_monitor = QtGui.QWidget()
        self.tab_monitor.setObjectName(_fromUtf8("tab_monitor"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.tab_monitor)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.btn_plot_probe = QtGui.QPushButton(self.tab_monitor)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_plot_probe.setFont(font)
        self.btn_plot_probe.setObjectName(_fromUtf8("btn_plot_probe"))
        self.horizontalLayout_2.addWidget(self.btn_plot_probe)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lbl_probe_log_path = QtGui.QLabel(self.tab_monitor)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_probe_log_path.setFont(font)
        self.lbl_probe_log_path.setObjectName(_fromUtf8("lbl_probe_log_path"))
        self.horizontalLayout.addWidget(self.lbl_probe_log_path)
        self.txt_probe_log_path = QtGui.QLineEdit(self.tab_monitor)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_probe_log_path.setFont(font)
        self.txt_probe_log_path.setObjectName(_fromUtf8("txt_probe_log_path"))
        self.horizontalLayout.addWidget(self.txt_probe_log_path)
        self.chk_probe_log = QtGui.QCheckBox(self.tab_monitor)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.chk_probe_log.setFont(font)
        self.chk_probe_log.setObjectName(_fromUtf8("chk_probe_log"))
        self.horizontalLayout.addWidget(self.chk_probe_log)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.tree_monitor = QtGui.QTreeWidget(self.tab_monitor)
        self.tree_monitor.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tree_monitor.sizePolicy().hasHeightForWidth())
        self.tree_monitor.setSizePolicy(sizePolicy)
        self.tree_monitor.setEditTriggers(QtGui.QAbstractItemView.AllEditTriggers)
        self.tree_monitor.setHeaderHidden(False)
        self.tree_monitor.setObjectName(_fromUtf8("tree_monitor"))
        self.tree_monitor.header().setDefaultSectionSize(150)
        self.tree_monitor.header().setHighlightSections(True)
        self.verticalLayout_5.addWidget(self.tree_monitor)
        self.verticalLayout_7.addLayout(self.verticalLayout_5)
        self.tabWidget.addTab(self.tab_monitor, _fromUtf8(""))
        self.tab_settings = QtGui.QWidget()
        self.tab_settings.setObjectName(_fromUtf8("tab_settings"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.tab_settings)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.btn_load_instruments = QtGui.QPushButton(self.tab_settings)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_load_instruments.setFont(font)
        self.btn_load_instruments.setObjectName(_fromUtf8("btn_load_instruments"))
        self.horizontalLayout_3.addWidget(self.btn_load_instruments)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.tree_settings = QtGui.QTreeWidget(self.tab_settings)
        self.tree_settings.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tree_settings.sizePolicy().hasHeightForWidth())
        self.tree_settings.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tree_settings.setFont(font)
        self.tree_settings.setEditTriggers(QtGui.QAbstractItemView.AllEditTriggers)
        self.tree_settings.setHeaderHidden(False)
        self.tree_settings.setObjectName(_fromUtf8("tree_settings"))
        self.tree_settings.header().setDefaultSectionSize(200)
        self.tree_settings.header().setHighlightSections(True)
        self.verticalLayout_3.addWidget(self.tree_settings)
        self.verticalLayout_8.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab_settings, _fromUtf8(""))
        self.tab_data = QtGui.QWidget()
        self.tab_data.setObjectName(_fromUtf8("tab_data"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout(self.tab_data)
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.btn_plot_data = QtGui.QPushButton(self.tab_data)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_plot_data.setFont(font)
        self.btn_plot_data.setObjectName(_fromUtf8("btn_plot_data"))
        self.horizontalLayout_10.addWidget(self.btn_plot_data)
        self.btn_save_data = QtGui.QPushButton(self.tab_data)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_save_data.setFont(font)
        self.btn_save_data.setObjectName(_fromUtf8("btn_save_data"))
        self.horizontalLayout_10.addWidget(self.btn_save_data)
        self.btn_delete_data = QtGui.QPushButton(self.tab_data)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_delete_data.setFont(font)
        self.btn_delete_data.setObjectName(_fromUtf8("btn_delete_data"))
        self.horizontalLayout_10.addWidget(self.btn_delete_data)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.tree_dataset = QtGui.QTreeView(self.tab_data)
        self.tree_dataset.setDragEnabled(True)
        self.tree_dataset.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.tree_dataset.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.tree_dataset.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.tree_dataset.setUniformRowHeights(True)
        self.tree_dataset.setObjectName(_fromUtf8("tree_dataset"))
        self.verticalLayout.addWidget(self.tree_dataset)
        self.horizontalLayout_12.addLayout(self.verticalLayout)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_12)
        self.tabWidget.addTab(self.tab_data, _fromUtf8(""))
        self.verticalLayout_10.addWidget(self.tabWidget)
        self.tabWidget_2 = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_2.sizePolicy().hasHeightForWidth())
        self.tabWidget_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.list_history = QtGui.QListView(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.list_history.setFont(font)
        self.list_history.setAlternatingRowColors(True)
        self.list_history.setWordWrap(True)
        self.list_history.setObjectName(_fromUtf8("list_history"))
        self.verticalLayout_9.addWidget(self.list_history)
        self.tabWidget_2.addTab(self.tab, _fromUtf8(""))
        self.tab_settings_2 = QtGui.QWidget()
        self.tab_settings_2.setObjectName(_fromUtf8("tab_settings_2"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout(self.tab_settings_2)
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.tree_gui_settings = QtGui.QTreeView(self.tab_settings_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tree_gui_settings.setFont(font)
        self.tree_gui_settings.setEditTriggers(QtGui.QAbstractItemView.DoubleClicked|QtGui.QAbstractItemView.EditKeyPressed)
        self.tree_gui_settings.setAlternatingRowColors(True)
        self.tree_gui_settings.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tree_gui_settings.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.tree_gui_settings.setIndentation(0)
        self.tree_gui_settings.setUniformRowHeights(True)
        self.tree_gui_settings.setItemsExpandable(True)
        self.tree_gui_settings.setSortingEnabled(True)
        self.tree_gui_settings.setExpandsOnDoubleClick(True)
        self.tree_gui_settings.setObjectName(_fromUtf8("tree_gui_settings"))
        self.tree_gui_settings.header().setDefaultSectionSize(200)
        self.tree_gui_settings.header().setSortIndicatorShown(True)
        self.verticalLayout_11.addWidget(self.tree_gui_settings)
        self.horizontalLayout_11.addLayout(self.verticalLayout_11)
        self.tabWidget_2.addTab(self.tab_settings_2, _fromUtf8(""))
        self.verticalLayout_10.addWidget(self.tabWidget_2)
        self.horizontalLayout_7.addLayout(self.verticalLayout_10)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.plot_2 = QtGui.QWidget(self.centralwidget)
        self.plot_2.setObjectName(_fromUtf8("plot_2"))
        self.horizontalLayout_15 = QtGui.QHBoxLayout(self.plot_2)
        self.horizontalLayout_15.setMargin(0)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.matplotlibwidget_2 = MatplotlibWidget(self.plot_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.matplotlibwidget_2.sizePolicy().hasHeightForWidth())
        self.matplotlibwidget_2.setSizePolicy(sizePolicy)
        self.matplotlibwidget_2.setMinimumSize(QtCore.QSize(200, 200))
        self.matplotlibwidget_2.setObjectName(_fromUtf8("matplotlibwidget_2"))
        self.horizontalLayout_15.addWidget(self.matplotlibwidget_2)
        self.verticalLayout_2.addWidget(self.plot_2)
        self.plot_1 = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot_1.sizePolicy().hasHeightForWidth())
        self.plot_1.setSizePolicy(sizePolicy)
        self.plot_1.setObjectName(_fromUtf8("plot_1"))
        self.horizontalLayout_14 = QtGui.QHBoxLayout(self.plot_1)
        self.horizontalLayout_14.setMargin(0)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.matplotlibwidget = MatplotlibWidget(self.plot_1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.matplotlibwidget.sizePolicy().hasHeightForWidth())
        self.matplotlibwidget.setSizePolicy(sizePolicy)
        self.matplotlibwidget.setMinimumSize(QtCore.QSize(200, 200))
        self.matplotlibwidget.setObjectName(_fromUtf8("matplotlibwidget"))
        self.horizontalLayout_14.addWidget(self.matplotlibwidget)
        self.verticalLayout_2.addWidget(self.plot_1)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 3)
        self.horizontalLayout_7.addLayout(self.verticalLayout_2)
        self.horizontalLayout_7.setStretch(0, 8)
        self.horizontalLayout_7.setStretch(1, 12)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1665, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.btn_exit = QtGui.QAction(MainWindow)
        self.btn_exit.setObjectName(_fromUtf8("btn_exit"))
        self.btn_load_gui = QtGui.QAction(MainWindow)
        self.btn_load_gui.setObjectName(_fromUtf8("btn_load_gui"))
        self.btn_save_gui = QtGui.QAction(MainWindow)
        self.btn_save_gui.setObjectName(_fromUtf8("btn_save_gui"))
        self.btn_about = QtGui.QAction(MainWindow)
        self.btn_about.setObjectName(_fromUtf8("btn_about"))
        self.menuFile.addAction(self.btn_exit)
        self.menuSettings.addAction(self.btn_load_gui)
        self.menuSettings.addAction(self.btn_save_gui)
        self.menuHelp.addAction(self.btn_about)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        self.tabWidget_2.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Lukin Lab - B26 GUI", None))
        self.btn_plot_script.setText(_translate("MainWindow", "plot script", None))
        self.btn_store_script_data.setText(_translate("MainWindow", "send to dataset", None))
        self.btn_load_scripts.setText(_translate("MainWindow", "import script", None))
        self.tree_scripts.headerItem().setText(0, _translate("MainWindow", "Parameter/Script", None))
        self.tree_scripts.headerItem().setText(1, _translate("MainWindow", "Value", None))
        self.btn_start_script.setText(_translate("MainWindow", "start", None))
        self.btn_stop_script.setText(_translate("MainWindow", "stop", None))
        self.lbl_time_estimate.setText(_translate("MainWindow", "time remaining:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_scripts), _translate("MainWindow", "Scripts", None))
        self.btn_plot_probe.setText(_translate("MainWindow", "plot probe", None))
        self.lbl_probe_log_path.setText(_translate("MainWindow", "Path", None))
        self.txt_probe_log_path.setText(_translate("MainWindow", "Z:\\Lab\\Cantilever\\Measurements", None))
        self.chk_probe_log.setText(_translate("MainWindow", "logging on", None))
        self.tree_monitor.headerItem().setText(0, _translate("MainWindow", "Parameter", None))
        self.tree_monitor.headerItem().setText(1, _translate("MainWindow", "Value", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_monitor), _translate("MainWindow", "Monitor", None))
        self.btn_load_instruments.setText(_translate("MainWindow", "import instrument", None))
        self.tree_settings.headerItem().setText(0, _translate("MainWindow", "Instrument", None))
        self.tree_settings.headerItem().setText(1, _translate("MainWindow", "Value", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_settings), _translate("MainWindow", "Instruments", None))
        self.btn_plot_data.setText(_translate("MainWindow", "plot script", None))
        self.btn_save_data.setText(_translate("MainWindow", "save selected", None))
        self.btn_delete_data.setText(_translate("MainWindow", "delete selected", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_data), _translate("MainWindow", "Dataset", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("MainWindow", "History", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_settings_2), _translate("MainWindow", "GUI Settings", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.btn_exit.setText(_translate("MainWindow", "Exit", None))
        self.btn_load_gui.setText(_translate("MainWindow", "load", None))
        self.btn_save_gui.setText(_translate("MainWindow", "save", None))
        self.btn_about.setText(_translate("MainWindow", "about", None))

from matplotlibwidget import MatplotlibWidget
