# create-directory-structure

このスクリプトは、JSON ファイルで定義されたディレクトリ構造を読み込み、それに基づいてファイルシステム上にディレクトリと空のファイルを作成します。

## ディレクトリ構成

```
.
├── README.md                      # プロジェクトの説明書
├── create_structure_from_json.py  # メインスクリプトファイル
└── directory_structure.json       # ディレクトリ構造を定義したJSONファイル
```

## 使い方

1. `directory_structure.json` ファイルに、作成したいディレクトリ構造を JSON 形式で定義します。

2. スクリプトを実行して、ディレクトリ構造を作成します。

```bash
python create_structure_from_json.py
```
