from utils.file_exporter import export_to_txt, export_to_docx

text = """
Hello Sakshi!

This is a test export.

Your exporter is working successfully!
"""

txt_path = export_to_txt(text, "test_file")
docx_path = export_to_docx(text, "test_file")

print("TXT Saved:", txt_path)
print("DOCX Saved:", docx_path)