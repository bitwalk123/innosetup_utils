from PySide6.QtCore import Signal

from _widgets import (
    Entry,
    Label,
    ToolBar,
    ToolButtonIcon,
)


class ISUToolBar(ToolBar):
    """Inno Setup Utility Tool Bar
    """
    dirClicked = Signal()
    playClicked = Signal()
    fileClicked = Signal()

    def __init__(self):
        super().__init__()
        lab_dir = Label('base directory')
        self.addWidget(lab_dir)

        # Entry
        self.ent_dir = Entry()
        self.addWidget(self.ent_dir)

        # Dir button
        but_dir = ToolButtonIcon('SP_DirIcon')
        but_dir.setToolTip('Select application root directory(folder).')
        but_dir.clicked.connect(self.dirClicked.emit)
        self.addWidget(but_dir)

        # Play button
        but_play = ToolButtonIcon('SP_MediaPlay')
        but_play.setToolTip('Start generating iss file for Inno Setup.')
        but_play.clicked.connect(self.playClicked.emit)
        self.addWidget(but_play)

        # File button
        but_file = ToolButtonIcon('SP_FileIcon')
        but_file.setToolTip('Load predefined contents in JSON format.')
        but_file.clicked.connect(self.fileClicked.emit)
        self.addWidget(but_file)

    def get_entry(self) -> str:
        return self.ent_dir.text()

    def set_entry(self, path: str):
        self.ent_dir.setText(path)
