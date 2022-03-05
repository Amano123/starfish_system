import tarfile
import os

file_path = "../data/ldcc-20140209.tar.gz"

# 解凍処理
tar = tarfile.open(file_path)
tar.extractall("../data/livedoor/")
tar.close()

# フォルダのファイルとディレクトリを確認
files_folders = [name for name in os.listdir("../data/livedoor/text/")]
print(files_folders)

# カテゴリーのフォルダのみを抽出
categories = [name for name in os.listdir("../data/livedoor/text/") if os.path.isdir("../data/livedoor/text/" + name)]

print(f"カテゴリー数：{len(categories)}")
print(categories)

