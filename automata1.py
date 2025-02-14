from pathlib import Path

# VOの各フォルダのうち、sub_jp.csvファイルが無いフォルダの名前をリストアップするpythonプログラムです
# 出力は"no_JP_sub_list.txtに書かれます
# exclude.txtにリストアップされたフォルダは無視します

excludespath = "./excludes.txt"
resultlist = "./no_JP_sub_list.txt"

def main():
    VO = Path("./VO")
    try:
        excludes = ReadText(excludespath)
    except:
        WriteTextLines(excludespath)
        excludes = ""
    result = []
    folders = [folder for folder in VO.iterdir() if folder.is_dir()]
    for folder in folders:
        if folder.name in excludes:
            continue
        if not "sub_jp.csv" in [file.name for file in folder.iterdir() if file.is_file()]:
            print(f"no sub_jp.csv in {folder.name}")
            result.append(folder.name)
    WriteTextLines(resultlist, result)

def ReadText(path):
    with open(file=path, mode="r", encoding="utf-8") as file:
        result = []
        for line in file:
            result.append(line.replace("\n", ""))
        return result

def WriteTextLines(path, text=""):
    with open(file=path, mode="w", encoding="utf-8") as file:
        for line in text:
            file.write(f'{line}\n')

if __name__ == "__main__":
    main()