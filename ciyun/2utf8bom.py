from chardet.universaldetector import UniversalDetector
import os
import codecs
import chardet

__file_type__ = [".cpp", ".h", ".ui"]
g_encode_info = []
g_files = []

# 获取文件编码类型
def get_encoding(file):
    # 二进制方式读取，获取字节数据，检测类型
    with open(file, 'rb') as f:
        data = f.read()
        return chardet.detect(data)['encoding']


def read_file(file):
    with open(file, 'rb') as f:
        return f.read()


def write_file(content, file):
    with open(file, 'wb') as f:
        f.write(content)


def get_files(direct):
    for root, dirs, files in os.walk(direct):
        for file in files:
            g_files.append(os.path.join(root, file))


def convert_encode2utf8(file, original_encode, des_encode, logFile):
    file_content = read_file(file)
    try:
        file_decode = file_content.decode(original_encode)
        file_encode = file_decode.encode(des_encode)
        write_file(file_encode, file)
    except Exception as e:
        print("[Error] e: ", e)
        logFile.write(file + "\n")
    print("[Info] file: ]: ", file)
    print("[Info] original_encode: ]: ", original_encode)


if __name__ == "__main__":
    logFile = codecs.open(os.path.split(os.path.realpath(__file__))[0]+"\\2Utf8Bom-py3-log", "w+", "utf-8")
    logFile.write("[Convert Failed]" + "\n\n")

    convert_direct = os.path.split(os.path.realpath(__file__))[0] + "\..\..\.."
    get_files(convert_direct)
    for filename in g_files:
        bool_continue = True
        for file_type in __file_type__:
            if filename.endswith(file_type):
                bool_continue = False
                break
        if bool_continue:
            continue
        if os.path.getsize(filename) == 0:
            continue
        file_content = read_file(filename)
        encode_info = get_encoding(filename)
        if encode_info != 'UTF-8-SIG':
            g_encode_info.append(filename)
            g_encode_info.append(encode_info)
            convert_encode2utf8(filename, encode_info, 'UTF-8-SIG', logFile)
    logFile.write("[Convert Info]" + "\n\n")
    for info in g_encode_info:
        if info:
            logFile.write(info + "\n")
        else:
            logFile.write("None\n")

    logFile.close()

