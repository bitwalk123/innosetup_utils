import glob
import json
import os
import sys

from PySide6.QtCore import Qt, QDir
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow, QMessageBox,
)

from modules.isu_toolbar import ISUToolBar


class ISUtil(QMainWindow):
    conf = None

    toolbar: ISUToolBar = None

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setWindowTitle('utility for Inno Setup Compiler')

    def init_ui(self):
        self.toolbar = ISUToolBar()
        self.toolbar.dirClicked.connect(self.button_dir_clicked)
        self.toolbar.playClicked.connect(self.button_play_clicked)
        self.toolbar.fileClicked.connect(self.button_file_clicked)
        self.addToolBar(Qt.TopToolBarArea, self.toolbar)

    def button_dir_clicked(self):
        path_dir = QFileDialog.getExistingDirectory(
            parent=self,
            caption='Select Folder',
            dir=os.environ['HOME'],
        )
        self.toolbar.set_entry(path_dir)

    def button_file_clicked(self):
        jsonfile = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select JSON file',
            dir=os.environ['HOME'],
        )
        json_open = open(jsonfile[0], 'r')
        self.conf = json.load(json_open)
        print(self.conf)

    def button_play_clicked(self):
        if self.toolbar.get_entry() is None:
            return
        dir_top = self.toolbar.get_entry()
        self.generate_sections(dir_top)

    def generate_sections(self, dir_top):
        list_output = list()
        # Setup section
        self.generate_section_setup(dir_top, list_output)
        # Files section
        self.generate_section_files(dir_top, list_output)
        # Icons
        self.generate_section_icons(list_output)
        # Output
        f = open(
            os.path.join(
                os.path.dirname(dir_top),
                '%s.iss' % self.conf['appname']
            ),
            'w', encoding='shift_jis'
        )
        for line in list_output:
            f.write(line + '\n')
        f.close()
        # completed message
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText('completed!')
        msgBox.exec()

    def generate_section_setup(self, dir_top, list_output):
        list_output.append('[Setup]')
        list_output.append('AppName=%s' % self.conf['appname'])
        list_output.append('AppVersion=%s' % self.conf['appver'])
        list_output.append('WizardStyle=modern')
        list_output.append(
            'DefaultDirName={autopf}\\%s' % self.conf['appname']
        )
        list_output.append('DefaultGroupName=%s' % self.conf['grpname'])
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
                self.conf['appname'],
                self.conf['appver'].replace('.', ''),
                self.conf['build']
            )
        )
        list_output.append('PrivilegesRequired=lowest')

    def generate_section_files(self, dir_top, list_output):
        list_output.append('[Files]')
        files = [
            p.replace('%s/' % dir_top, '')
            for p in glob.glob('%s/**' % dir_top, recursive=True)
            if os.path.isfile(p)
        ]
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

    def generate_section_icons(self, list_output):
        list_output.append('[Icons]')
        list_output.append(
            'Name: "{group}\\%s"; Filename: "{app}\\%s.exe"' % (
                self.conf['appname'],
                self.conf['appname']
            )
        )


def main():
    app = QApplication(sys.argv)
    win = ISUtil()
    win.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
