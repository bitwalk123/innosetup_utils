import glob
import json
import os
import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QMessageBox,
    QStyle,
)

from modules.isu_mainpanel import ISUMainPanel
from modules.isu_toolbar import ISUToolBar


class ISUtil(QMainWindow):
    jsonfile: str = ''

    def __init__(self):
        super().__init__()
        self.setContentsMargins(2, 2, 2, 2)
        self.setWindowTitle('utility for Inno Setup Compiler')
        self.setWindowIcon(
            QIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_TitleBarMenuButton))
        )
        # Toolbar
        self.toolbar = ISUToolBar()
        self.addToolBar(Qt.TopToolBarArea, self.toolbar)
        self.toolbar.dirClicked.connect(self.button_dir_clicked)
        self.toolbar.playClicked.connect(self.button_play_clicked)
        self.toolbar.fileClicked.connect(self.button_file_clicked)
        # Main Panel
        self.panel = ISUMainPanel()
        self.setCentralWidget(self.panel)

    def button_dir_clicked(self):
        path_dir = QFileDialog.getExistingDirectory(
            parent=self,
            caption='Select Folder',
            dir=os.environ['HOME'],
        )
        self.toolbar.set_entry(path_dir)

    def button_file_clicked(self):
        selection = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select JSON file',
            dir=os.environ['HOME'],
            filter='JSON Files (*.json)'
        )
        self.jsonfile = selection[0]
        if os.path.exists(self.jsonfile):
            with open(self.jsonfile) as f:
                conf = json.load(f)
            self.panel.setContents(conf)
        else:
            self.jsonfile = ''

    def button_play_clicked(self):
        if self.toolbar.get_entry() is None:
            return
        dir_top = self.toolbar.get_entry()
        self.generate_sections(dir_top)

    def closeEvent(self, event):
        # update JSON file if loaded.
        if len(self.jsonfile) > 0:
            conf = self.panel.getContents()
            with open(self.jsonfile, 'w') as f:
                json.dump(conf, f, indent=4)

        event.accept()

    def generate_sections(self, dir_top):
        conf = self.panel.getContents()
        # Check all information is prepared to make iss file
        if self.is_valid_information(conf) is False:
            return
        list_output = list()
        # Setup section
        self.generate_section_setup(dir_top, list_output, conf)
        # Files section
        self.generate_section_files(dir_top, list_output, conf)
        # Icons
        self.generate_section_icons(list_output, conf)
        # Tasks
        self.generate_section_tasks(list_output, conf)
        # Output
        f = open(
            os.path.join(
                os.path.dirname(dir_top),
                '%s.iss' % conf['appname']
            ),
            'w', encoding='shift_jis'
        )
        for line in list_output:
            f.write(line + '\n')
        f.close()
        # completed message
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Icon.Information)
        msgBox.setText('completed!')
        msgBox.exec()

    def generate_section_setup(self, dir_top, list_output, conf):
        list_output.append('[Setup]')
        list_output.append('AppName=%s' % conf['appname'])
        list_output.append('AppVersion=%s' % conf['appver'])
        list_output.append('WizardStyle=modern')
        list_output.append(
            'DefaultDirName={autopf}\\%s' % conf['appname']
        )
        list_output.append('DefaultGroupName=%s' % conf['grpname'])
        list_output.append('Compression=lzma2')
        list_output.append('SolidCompression=yes')
        list_output.append(
            'SourceDir=Z:%s' % dir_top.replace('/', '\\')
        )
        list_output.append(
            'OutputDir=Z:%s' % os.path.dirname(dir_top).replace('/', '\\')
        )
        list_output.append(
            'OutputBaseFilename=%s_%s_setup_%s' % (
                conf['appname'],
                conf['appver'].replace('.', ''),
                conf['build']
            )
        )
        # list_output.append('PrivilegesRequired=lowest')
        list_output.append('PrivilegesRequiredOverridesAllowed=dialog')
        # License File
        if 'license' in conf.keys():
            text_license = conf['license']
            if len(text_license) > 0:
                list_output.append(
                    'LicenseFile=%s' % text_license.replace('/', '\\')
                )

    def generate_section_files(self, dir_top, list_output, conf):
        list_output.append('[Files]')
        old_ishidden = glob._ishidden  # need to find hidden files start with .
        glob._ishidden = lambda x: False
        files = [
            p.replace('%s/' % dir_top, '')
            for p in glob.glob('%s/**' % dir_top, recursive=True)
            if os.path.isfile(p)
        ]
        glob._ishidden = old_ishidden
        # ---------------------------------------------------------------------
        for file in files:
            file_src = file.replace('/', '\\')
            dir = os.path.dirname(file)
            if len(dir) == 0:
                dir_dst = '{app}'
            else:
                dir_dst = '{app}\\%s' % dir.replace('/', '\\')

            line = 'Source: "%s"; DestDir: "%s"' % (file_src, dir_dst)
            list_output.append(line)

    def generate_section_icons(self, list_output, conf):
        list_output.append('[Icons]')
        list_output.append(
            'Name: "{group}\\%s"; Filename: "{app}\\%s.exe"' % (
                conf['appname'],
                conf['appname']
            )
        )
        list_output.append(
            'Name: "{userdesktop}\%s"; Filename: "{app}\\%s.exe"; Tasks: desktopicon' % (
                conf['appname'],
                conf['appname']
            )
        )

    def generate_section_tasks(self, list_output, conf):
        list_output.append('[Tasks]')
        list_output.append('Name: desktopicon; Description: "Create a &desktop icon";')

    def is_valid_information(self, conf):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Icon.Warning)
        # source directory
        if len(self.toolbar.get_entry()) == 0:
            msgBox.setText('no source directory!')
            msgBox.exec()
            return False
        # source directory exists
        if not os.path.exists(self.toolbar.get_entry()):
            msgBox.setText('source directory does not exist!')
            msgBox.exec()
            return False
        #
        if len(conf['appname']) == 0:
            msgBox.setText('no application name is provided!')
            msgBox.exec()
            return False
        #
        if len(conf['appver']) == 0:
            msgBox.setText('no application version is provided!')
            msgBox.exec()
            return False
        #
        if len(conf['grpname']) == 0:
            msgBox.setText('no group name is provided!')
            msgBox.exec()
            return False
        #
        if len(conf['build']) == 0:
            msgBox.setText('no build number is provided!')
            msgBox.exec()
            return False

        return True


def main():
    app = QApplication(sys.argv)
    win = ISUtil()
    win.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
