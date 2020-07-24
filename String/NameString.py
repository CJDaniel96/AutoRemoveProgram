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

        # DataBase name String
        self.connect_db_error_text = '連線失敗，請檢察輸入是否正確!'
        self.db_table_programming_error_text = '資料表不存在，或您沒有權限'

        # Log format
        self.logger_format = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        self.log_date_format = '%Y%m%d %H:%M:%S'
        self.remove_data_success_log_msg = ' Remove Success!'
        self.connect_db_success_log_msg = 'Connect to the Database Success!'
        self.connect_db_fail_log_msg = 'Connect to the Database Fail!'
