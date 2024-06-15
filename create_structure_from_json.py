import os
import json


def create_directory_structure(base_path, structure):
    for folder, contents in structure.items():
        # ベースディレクトリまたはサービスフォルダのパスを設定
        folder_path = os.path.join(base_path, folder) if folder != "." else base_path
        # フォルダが'.'でなければ、フォルダを作成
        if folder != ".":
            os.makedirs(folder_path, exist_ok=True)
        # 各ファイルまたはサブディレクトリに対して処理
        for item in contents:
            if isinstance(
                item, dict
            ):  # サブディレクトリの場合（今回のJSON構造では使用されていない）
                create_directory_structure(folder_path, item)
            else:  # ファイルの場合
                file_path = os.path.join(folder_path, item)
                with open(file_path, "w") as f:
                    pass  # ファイルを空で作成


def main():
    json_file_path = "directory_structure.json"
    with open(json_file_path, "r") as f:
        directory_structure = json.load(f)

    base_path = "."
    for key, value in directory_structure.items():
        # ベースディレクトリ（プロジェクトフォルダ）を作成
        project_path = os.path.join(base_path, key)
        os.makedirs(project_path, exist_ok=True)
        # ディレクトリ構造を作成
        create_directory_structure(project_path, value)

    print("Directory structure created successfully")


if __name__ == "__main__":
    main()
