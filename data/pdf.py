# from PyPDF2 import PdfReader
# import json
# import re
# import ace_tools as tools
#
# # 读取 PDF 文件
# pdf_path = "source.pdf"
# reader = PdfReader(pdf_path)
#
# # 提取全部文本
# full_text = ""
# for page in reader.pages:
#     full_text += page.extract_text() + "\n"
#
# # 用正则表达式分割作文，每篇作文以“范文”+数字开头
# essay_splits = re.split(r"范文\s*\d+", full_text)
# essays = [e.strip() for e in essay_splits if len(e.strip().split()) > 50]  # 排除空文本或非正文
#
# # 保存为 JSONL 文件
# jsonl_path = "/mnt/data/ielts_band7_essays.jsonl"
# with open(jsonl_path, "w", encoding="utf-8") as f:
#     for idx, content in enumerate(essays, 1):
#         entry = {
#             "id": idx,
#             "content": content
#         }
#         f.write(json.dumps(entry, ensure_ascii=False) + "\n")
#
#  tools.display_file(jsonl_path)
#
