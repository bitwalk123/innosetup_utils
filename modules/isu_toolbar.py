from PySide6.QtCore import Signal

from widgets import (
    Entry,
    Label,
    ToolBar,
    ToolButtonIcon,
)


class ISUToolBar(ToolBar):
    dirClicked = Signal()
    playClicked = Signal()
    fileClicked = Signal()

    def __init__(self):
        super().__init__()
        label_dir = Label('base directory')
        self.addWidget(label_dir)

        # Entry
        self.entry_dir = Entry()
        self.addWidget(self.entry_dir)

        # Dir button
        button_dir = ToolButtonIcon('SP_DirIcon')
        button_dir.setToolTip('Select application root directory(folder).')
        button_dir.clicked.connect(self.dirClicked.emit)
        self.addWidget(button_dir)

        # Play button
        button_play = ToolButtonIcon('SP_MediaPlay')
        button_play.setToolTip('Start generating iss file for Inno Setup.')
        button_play.clicked.connect(self.playClicked.emit)
        self.addWidget(button_play)

        # File button
        button_file = ToolButtonIcon('SP_FileIcon')
        button_file.setToolTip('Load predefined contents in JSON format.')
        button_file.clicked.connect(self.fileClicked.emit)
        self.addWidget(button_file)

    def get_entry(self) -> str:
        return self.entry_dir.text()

    def set_entry(self, path: str):
        self.entry_dir.setText(path)
