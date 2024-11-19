import json
import re


def extract_keyword(file_path_list):
    keyword_file_list = []
    for file_path in file_path_list:
        content = open(file_path).read()
        keyword_file_path = file_path + ".key"
        content = content.replace("\\n", " ").replace("\\t", " ")
        content = re.sub(' +', ' ', content)
        content = re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z\s]", "", content).split(" ")
        try:
            with open(keyword_file_path, "w", encoding="utf-8") as f:
                json.dump(content, f, ensure_ascii=False, indent=4)
        except EOFError as e:
            print(f"파일 저장 실패: {e}")
        keyword_file_list.append(keyword_file_path)

