import tarfile
import os

file_path = "../data/ldcc-20140209.tar.gz"
save_path = "../data/livedoor"

# 解凍処理
tar = tarfile.open(file_path)
tar.extractall(save_path)
tar.close()

# フォルダのファイルとディレクトリを確認
files_folders = [name for name in os.listdir(f"{save_path}/text/")]
print(files_folders)

# カテゴリーのフォルダのみを抽出
categories = [name for name in os.listdir(f"{save_path}/text/") if os.path.isdir(f"{save_path}/text/" + name)]

print(f"カテゴリー数：{len(categories)}")
print(categories)
