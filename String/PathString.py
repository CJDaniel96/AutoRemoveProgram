class PathString:
    """
    The program src data path
    """

    def __init__(self):
        # UI Path
        self.win_ui_path_string = r'.\src\Qt\AutoRemoveQt.ui'
        self.cycle_settings_ui_path_string = r'.\src\Qt\CycleSettingsQt.ui'
        self.time_settings_ui_path_string = r'.\src\Qt\TimeSettingsQt.ui'

        # Icon Path
        self.system_tray_icon = r'.\src\Icon\GPM.png'
        self.open_icon = r'.\src\Icon\open_icon.png'
        self.exit_icon = r'.\src\Icon\exit_icon.png'
        self.cycle_settings_icon = r'.\src\Icon\cycle_settings_icon.png'
        self.time_settings_icon = r'.\src\Icon\time_settings_icon.jfif'

        # TxT Path
        self.remove_list_text = r'.\src\Table\RemoveList.txt'
        self.cycle_list_path_string = r'.\src\Table\CycleList.txt'
