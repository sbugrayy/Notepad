import sys
from PyQt5 import QtWidgets, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QMenu

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_files = {}
        self.init_ui(self)

        # Tam ekran
        self.actionFullscreen = QtWidgets.QAction("Toggle Fullscreen", self)
        self.actionFullscreen.setShortcut("F11")
        self.actionFullscreen.triggered.connect(self.toggle_fullscreen)
        self.menuView = self.menuBar().addMenu("View")
        self.menuView.addAction(self.actionFullscreen)

        # Yeni sekme
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.tabCloseRequested.connect(self.close_tab)
        self.add_new_tab("Untitled")

        # Layout optimizasyonları
        self.centralwidget.setLayout(QtWidgets.QVBoxLayout())
        self.centralwidget.layout().addWidget(self.tabWidget)
        self.centralwidget.layout().setContentsMargins(0, 0, 0, 0)
        
        self.tabWidget.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding
        )

        self.tabWidget.currentChanged.connect(self.update_actions)

        # Menüdeki yeni sekme
        self.actionNew_Tab = QtWidgets.QAction("New Tab", self)
        self.actionNew_Tab.triggered.connect(lambda: self.add_new_tab("Untitled"))
        self.menuFile.insertAction(self.actionNew, self.actionNew_Tab)

        self.connect_actions()
    
    def init_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 791, 521))
        self.tabWidget.setObjectName("tabWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionKes = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("edit-cut")
        self.actionKes.setIcon(icon)
        #self.actionKes.setMenuRole(QtCore.Qt.QAction::MenuRole::NoRole)
        self.actionKes.setObjectName("actionKes")
        self.actionKopyala = QtWidgets.QAction(MainWindow)
        self.actionKopyala.setCheckable(False)
        self.actionKopyala.setChecked(False)
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::EditCopy")
        self.actionKopyala.setIcon(icon)
        #self.actionKopyala.setMenuRole(QtCore.Qt.QAction::MenuRole::NoRole)
        self.actionKopyala.setObjectName("actionKopyala")
        self.actionYapistir = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::EditPaste")
        self.actionYapistir.setIcon(icon)
        #self.actionYapistir.setMenuRole(QtCore.Qt.QAction::MenuRole::NoRole)
        self.actionYapistir.setObjectName("actionYapistir")
        self.actionTumSec = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::EditSelectAll")
        self.actionTumSec.setIcon(icon)
        #self.actionTumSec.setMenuRole(QtCore.Qt.QAction::MenuRole::NoRole)
        self.actionTumSec.setObjectName("actionTumSec")
        self.actionNew = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::DocumentNew")
        self.actionNew.setIcon(icon)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::DocumentOpen")
        self.actionOpen.setIcon(icon)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::DocumentSave")
        self.actionSave.setIcon(icon)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::DocumentSaveAs")
        self.actionSave_As.setIcon(icon)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::EditCopy")
        self.actionCopy.setIcon(icon)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::EditPaste")
        self.actionPaste.setIcon(icon)
        self.actionPaste.setObjectName("actionPaste")
        self.actionCut = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::EditCut")
        self.actionCut.setIcon(icon)
        self.actionCut.setObjectName("actionCut")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::EditRedo")
        self.actionRedo.setIcon(icon)
        self.actionRedo.setObjectName("actionRedo")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::EditUndo")
        self.actionUndo.setIcon(icon)
        self.actionUndo.setObjectName("actionUndo")
        self.actionNotepad = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::HelpAbout")
        self.actionNotepad.setIcon(icon)
        self.actionNotepad.setObjectName("actionNotepad")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addAction(self.actionUndo)
        self.menuAbout.addAction(self.actionNotepad)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionSave_As)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCut)
        self.toolBar.addAction(self.actionCopy)
        self.toolBar.addAction(self.actionPaste)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionRedo)
        self.toolBar.addAction(self.actionUndo)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionNotepad)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionKes.setText(_translate("MainWindow", "Kes"))
        self.actionKes.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionKopyala.setText(_translate("MainWindow", "Kopyala"))
        self.actionKopyala.setToolTip(_translate("MainWindow", "Kopyala"))
        self.actionKopyala.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionYapistir.setText(_translate("MainWindow", "Yapistir"))
        self.actionYapistir.setToolTip(_translate("MainWindow", "Yapistir"))
        self.actionYapistir.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionTumSec.setText(_translate("MainWindow", "TumSec"))
        self.actionTumSec.setToolTip(_translate("MainWindow", "Tümünü seç"))
        self.actionTumSec.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_As.setText(_translate("MainWindow", "Save as"))
        self.actionSave_As.setShortcut(_translate("MainWindow", "Ctrl+T"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+Y"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionNotepad.setText(_translate("MainWindow", "About Notepad"))
    
    def contextMenuEvent(self, event):
        contextMenu = QMenu(self)

        newAction = contextMenu.addAction("New")
        openAction = contextMenu.addAction("Open")
        quitAction = contextMenu.addAction("Quit")

        action = contextMenu.exec_(event.globalPos())
        if action == newAction:
            self.new_file()
        elif action == openAction:
            self.open_file()
        elif action == quitAction:
            self.close()

        return super().contextMenuEvent(event)

    def update_actions(self):
        editor = self.get_current_editor()
        self.actionCut.triggered.disconnect()
        self.actionCopy.triggered.disconnect()
        self.actionPaste.triggered.disconnect()
        self.actionUndo.triggered.disconnect()
        self.actionRedo.triggered.disconnect()
        if editor:
            self.actionCut.triggered.connect(editor.cut)
            self.actionCopy.triggered.connect(editor.copy)
            self.actionPaste.triggered.connect(editor.paste)
            self.actionUndo.triggered.connect(editor.undo)
            self.actionRedo.triggered.connect(editor.redo)

    def connect_actions(self):
        # File actions
        self.actionNew.triggered.connect(self.new_file)
        self.actionOpen.triggered.connect(self.open_file)
        self.actionSave.triggered.connect(self.save_file)
        self.actionSave_As.triggered.connect(self.save_as_file)
        # About action
        self.actionNotepad.triggered.connect(self.about)
    
    def add_new_tab(self, title, content="", file_path=None):
        new_textedit = QtWidgets.QTextEdit()
        new_textedit.setPlainText(content)
        new_textedit.modified = False
        
        new_textedit.textChanged.connect(
            lambda: self.update_tab_title(self.tabWidget.indexOf(new_textedit))
        )
        index = self.tabWidget.addTab(new_textedit, title)
        self.tabWidget.setCurrentIndex(index)
        self.current_files[index] = file_path
        
        new_textedit.setFocus()
        return new_textedit

    def get_current_editor(self):
        return self.tabWidget.currentWidget()

    def get_current_file(self):
        index = self.tabWidget.currentIndex()
        return self.current_files.get(index)

    def update_tab_title(self, index):
        current_title = self.tabWidget.tabText(index)
        editor = self.tabWidget.widget(index)
        
        if not current_title.endswith('*'):
            self.tabWidget.setTabText(index, current_title + '*')
        
        if not hasattr(editor, 'modified'):
            editor.modified = False
        editor.modified = True

    def close_tab(self, index):
        if self.tabWidget.count() == 1:
            return
        
        editor = self.tabWidget.widget(index)
        
        # Kaydedilmemiş değişiklik kontrolü
        if hasattr(editor, 'modified') and editor.modified:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Belgede kaydedilmemiş değişiklikler var!")
            msg.setInformativeText(f"{self.tabWidget.tabText(index)} kaydedilsin mi?")
            msg.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
            msg.setDefaultButton(QMessageBox.Save)
            
            response = msg.exec_()
            
            if response == QMessageBox.Save:
                self.save_file()
            elif response == QMessageBox.Cancel:
                return
        
        self.tabWidget.removeTab(index)
        if index in self.current_files:
            del self.current_files[index]
        
        # Kalan sekmelerin index'lerini güvenli şekilde güncelle
        new_idx = 0
        for old_idx in list(self.current_files.keys()):  # list() ile kopya oluştur
            if old_idx > index:
                self.current_files[new_idx] = self.current_files.pop(old_idx)
                new_idx += 1

    def new_file(self):
        new_editor = self.add_new_tab("Untitled")
        index = self.tabWidget.currentIndex()
        self.current_files[index] = None
        new_editor.setPlainText("")
        new_editor.modified = False
        self.tabWidget.setTabText(index, "Untitled")
    
    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)")
        if filename:
            try:
                with open(filename, 'r') as file:
                    content = file.read()
                editor = self.add_new_tab(filename.split('/')[-1], content, filename)
                self.tabWidget.setCurrentWidget(editor)
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Could not open file: {e}")

    def save_file(self):
        index = self.tabWidget.currentIndex()
        if self.current_files.get(index):
            try:
                with open(self.current_files[index], 'w') as file:
                    file.write(self.get_current_editor().toPlainText())
                # Yıldızı kaldır
                title = self.tabWidget.tabText(index).replace('*', '')
                self.tabWidget.setTabText(index, title)
                self.get_current_editor().modified = False
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Could not save file: {e}")
        else:
            self.save_as_file()

    def save_as_file(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save As", "", "Text Files (*.txt);;All Files (*)")
        if filename:
            try:
                with open(filename, 'w') as file:
                    file.write(self.get_current_editor().toPlainText())
                index = self.tabWidget.currentIndex()
                self.current_files[index] = filename
                self.tabWidget.setTabText(index, filename.split('/')[-1])
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Could not save file: {e}")
    
    def about(self):
        QMessageBox.about(self, "About Notepad", 
                         "Simple Notepad Application\nCreated with PyQt5")
    
    def toggle_fullscreen(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())