class NameString:
    """
    Whole program the words transfer
    """

    def __init__(self):
        # MainWindow name string
        self.days_cycle = ' days cycle'
        self.menu_open = '打開'
        self.menu_exit = '退出'
        self.menu_time_settings = '刪除時間設定'
        self.menu_cycle_settings = '刪除週期設定'

        # MessageBox name string
        self.auto_remove_message_text = '列表將被更新'
        self.auto_remove_message_informativeText = '是否保存更改?'
        self.exit_program_text = '程式正在退出'
        self.exit_program_informativeText = '是否要退出程式?'
        self.error = '錯誤'
        self.error_file_path = '檔案路徑不正確!!!'
        self.listWidget_click_message_text = '是否刪除此指令?'
        self.listWidget_click_message_informativeText = '確認請按Yes'
        self.remove_item_cover_text = '您要覆蓋之前已在此路徑的指令嗎?'

        # Wait remove table name string
        self.remove_program_text = 'Auto Remove Program'

        # Settings name string
        self.time_settings_list_default_text = '未選擇'
        self.cycle_settings_error_input_text = '您輸入的不是整數，請重新輸入!'


class PathString:
    """
    The program src data path
    """

    def __init__(self):
        # UI Path
        self.win_ui_path_string = r'..\src\Qt\AutoRemoveQt.ui'
        self.cycle_settings_ui_path_string = r'..\src\Qt\CycleSettingsQt.ui'
        self.time_settings_ui_path_string = r'..\src\Qt\TimeSettingsQt.ui'

        # Icon Path
        self.system_tray_icon = r'..\src\Icon\GPM.png'
        self.open_icon = r'..\src\Icon\open_icon.png'
        self.exit_icon = r'..\src\Icon\exit_icon.png'
        self.cycle_settings_icon = r'..\src\Icon\cycle_settings_icon.png'
        self.time_settings_icon = r'..\src\Icon\time_settings_icon.jfif'

        # TxT Path
        self.remove_list_text = r'..\src\Table\RemoveList.txt'
        self.cycle_list_path_string = r'..\src\Table\CycleList.txt'
