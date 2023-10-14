import os

name = [
    ('klee', 'ZH'),
    ('keqing', 'ZH')
]

out_file = './filelists/genshin_out.txt'


def process_line(line):
    pass


def process():
    with open(out_file, 'w', encoding='utf-8') as wf:
        for item in name:
            ch_name, ch_lang = item
            path = f'./raw/{ch_name}'
            files = os.listdir(path)
            for f in files:
                if f.endswith('.lab'):
                    with open(os.path.join(path, f), 'r', encoding='utf-8') as perFile:
                        line = perFile.readline()
                        line = process_line(f, line)
                        result = f"./dataset/{ch_name}/{f.split('.')[0]}.wav|{ch_name}|{ch_lang}|{line}"
                        wf.write(f"{result}\n")

import re
# 处理数据集代词文本
def process_line(f, line):
    # 1. 替换{F#她}{M#他}成“他”
    line = re.sub(r'\{M#他\}\{F#她\}', '他', line)

    # 2. 根据文件名保留“哥哥”或“姐姐”
    # 检查文件名最后一个字符（不包括文件扩展名）是不是'a'或'b'
    if f[-5:-4] == 'a':  
        line = re.sub(r'\{M#哥哥\}\{F#姐姐\}', '哥哥', line)
        # 增加的通用规则
        line = re.sub(r'\{PLAYERAVATAR#SEXPRO\[.*?\]\}', '哥哥', line)
    elif f[-5:-4] == 'b':  
        line = re.sub(r'\{M#哥哥\}\{F#姐姐\}', '姐姐', line)
        # 增加的通用规则
        line = re.sub(r'\{PLAYERAVATAR#SEXPRO\[.*?\]\}', '姐姐', line)
    else: 
        line = re.sub(r'\{PLAYERAVATAR#SEXPRO\[.*?\]\}', '哥哥', line)
    return line

if __name__ == '__main__':
    process()
