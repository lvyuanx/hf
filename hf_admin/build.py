import argparse
import os
import shutil


class BuildObj(object):

    def __init__(self):
        self.input_path = ""
        self.out_path = ""
        self.clear = False

    def get_args(self):
        parser = argparse.ArgumentParser(description='Build vue to django project')
        parser.add_argument('-i', '--input_path', help='输入路径', required=False,
                            default='D:\\HF\\web\\hf_admin\\static')
        parser.add_argument('-o', '--out_path', help='输出路径', required=False,
                            default='D:\\Project\\pycharm\\hf_system')
        parser.add_argument('-c', '--clear', help='清理目标路径', required=False, default=False)
        args = parser.parse_args()
        self.input_path = args.input_path
        self.out_path = args.out_path
        self.clear = args.clear

    def clear_path(self):
        if self.clear:
            web_dir = os.path.join(self.out_path, 'web','static')
            if os.path.exists(web_dir):
                shutil.rmtree(web_dir)

    def npm_run_build(self):
        os.system('npm run build')

    def migration_dist(self):
        dict_dir = self.input_path
        web_staitc_dir = os.path.join(self.out_path, 'web', 'static')

        shutil.copytree(dict_dir, web_staitc_dir)

    def start(self):
        self.get_args()
        self.clear_path()
        self.npm_run_build()
        self.migration_dist()


if __name__ == '__main__':
    BuildObj().start()
