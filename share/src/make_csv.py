# %%
# ライブラリのインポート
from asyncore import read
import os

# %%
# path変数
read_path = "../data/livedoor/text"
write_path = "../data/livedoor/livedoor.csv"

# %%
# カテゴリー名の抽出
categories = [name for name in os.listdir(f"{read_path}") if os.path.isdir(f"{read_path}/{name}")]

# %%
# データをCSVに出力
with open(write_path, 'w') as write_file:
    for i, categorie in enumerate(categories):
        for file_name in os.listdir(f"{read_path}/{categorie}"):
            with open(f"{read_path}/{categorie}/{file_name}") as read_file:
                text = read_file.readlines()[3:]

                text = [sentence.strip() for sentence in text]
                text = list(filter(lambda line: line != '', text))
                text = ''.join(text)
                text = text.translate(str.maketrans({'\n': '', '\t': '', '\r': '', '\u3000': ''}))

                for sentence in text.split('。'):
                    write_file.write(f"{sentence}, {i}\n")

# %%
