import os
from datetime import datetime
from logging.handlers import WatchedFileHandler


class MultiprocessTimeHandler(WatchedFileHandler):
    def __init__(self, file_path, mode='a', encoding=None, delay=False, errors=None, suffix="%Y-%m-%d"):
        # 如果日志文件夹不存在就创建日志文件夹
        if not os.path.exists(file_path):
            os.makedirs(file_path)

        self.file_path = file_path
        self.suffix = suffix

        # 日志文件名
        self.file_name = "{}.log".format(datetime.now().strftime(suffix))

        # 日志文件路径
        file_path_name = os.path.join(self.file_path, self.file_name)
        super().__init__(file_path_name, mode, encoding, delay, errors)

    def emit(self, record):
        # 获取当前文件名
        current_file_name = "{}.log".format(datetime.now().strftime(self.suffix))

        # 判断当前文件名是否与日志文件名相同
        if current_file_name != self.file_name:

            self.file_name = current_file_name

            # 重新赋值日志文件路径
            self.baseFilename = os.path.abspath(os.path.join(self.file_path, self.file_name))

            if self.stream:
                self.flush()
                self.stream.close()
            self.stream = self._open()

            """
                重新获取当前文件信息
                    def _statstream(self):
                        if self.stream:
                            sres = os.fstat(self.stream.fileno())
                            self.dev, self.ino = sres[ST_DEV], sres[ST_INO]
                sres[ST_DEV], sres[ST_INO] 这两个参数如果发生改变，表示原来的日志被删除，修改，或者重命名等操作，此时就无法写入日志文件
                所以需要重新获取这两个参数，来判断日志文件是否发生改变
            """
            self._statstream()

        """
            父类的emit方法，会判断日志文件是否发生改变，如果发生改变，会重新打开日志文件
            self.reopenIfNeeded()
            logging.FileHandler.emit(self, record)
        """
        super().emit(record)



