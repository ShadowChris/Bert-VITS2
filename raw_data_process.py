import os
import re
# 工具类，根据格式生成数据集的音频列表
name = [
    ('silverwolf_zh', 'ZH')
]

out_file = f'filelists/raw_data_out.txt'
def process():
    with open(out_file, 'w', encoding='utf-8') as wf:
        for item in name:
            tmp_name = item[0]
            tmp_language = item[1]
            path = f'./raw/{tmp_name}'
            # 进入角色的文件夹
            files = os.listdir(path)

            for f in files:
                if f.endswith('.lab'):
                    with open(os.path.join(path, f), 'r', encoding='utf-8') as perFile:
                        line = perFile.readline()
                        line = process_line(line)
                        result = f"./dataset/{tmp_name}/{f.split('.')[0]}.wav|{tmp_name}|{tmp_language}|{line}"
                        wf.write(f'{result}\n')

# 处理数据集文本，删除多余标签符号（似乎preprocess_text.py会处理大部分文本）
def process_line(line):
    # 1. 替换{F#她}{M#他}成“他”
    line = re.sub(r'\{M#他\}\{F#她\}', '他', line)
    # # 2. 删除所有被{}包裹的文本
    # line = re.sub(r'\{[^}]+\}', '', line)
    # # 3. 删除所有的html tag
    # pattern = re.compile(r'<.*?>')
    # line = re.sub(pattern, '', line)
    # # 4. 删除「」标识
    # line = line.replace('「', '').replace('」', '')

    return line




if __name__ == '__main__':
    process()