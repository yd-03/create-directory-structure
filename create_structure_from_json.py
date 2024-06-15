import os
import json


def create_directory_structure(base_path, structure):
    # 構造内の各フォルダに対してループ
    for folder, contents in structure.items():
        # フォルダのフルパスを作成
        folder_path = os.path.join(base_path, folder)
        # フォルダを作成（既に存在する場合はスキップ）
        os.makedirs(folder_path, exist_ok=True)
        # フォルダ内のアイテム（サブフォルダまたはファイル）に対してループ
        for item in contents:
            # アイテムが辞書（サブフォルダ）の場合、再帰的に関数を呼び出す
            if isinstance(item, dict):
                create_directory_structure(folder_path, item)
            else:
                # アイテムがファイルの場合、ファイルパスを作成して空のファイルを作成
                file_path = os.path.join(folder_path, item)
                with open(file_path, "w") as f:
                    pass  # ファイルは空で作成


def main():
    # JSONファイルのパス
    json_file_path = "directory_structure.json"
    with open(json_file_path, "r") as f:
        directory_structure = json.load(f)

    # 基準となるパス（ここではカレントディレクトリ）
    base_path = "."

    create_directory_structure(base_path, directory_structure)

    print("Directory structure created successfully")


if __name__ == "__main__":
    main()
