import markdown2
import pdfkit
import os
import sys

def check(file_name):
    if not os.path.isfile(file_name):
        raise FileNotFoundError(f"Error:File '{file_name}' does not exist.")
    return file_name

def convert(md_file):
    pdf = os.path.splitext(md_file)[0] + ".pdf"

    with open(md_file, "r") as file:
        markdown_content = file.read()

    content = markdown2.markdown(markdown_content)

    styling = f"""
    <html>
    <head>
    <style>
        body {{
            background-color: white;
            font-family: Arial, sans-serif;
            color: black;
            margin: 20px;
        }}
        h1, h2, h3 {{
            color: #2E86C1;
        }}
        p {{
            font-size: 14px;
            line-height: 1.6;
        }}
        table, th, td {{
            border: 1px solid black;
            border-collapse: collapse;
            padding: 8px;
        }}
    </style>
    </head>
    <body>
    {content}
    </body>
    </html>
    """

    html = "temp.html"
    with open(html, "w") as file:
        file.write(styling)

    pdfkit.from_file(html, pdf)

    os.remove(html)

    print(f"PDF saved as '{pdf}'")

if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            raise ValueError("Usage: python3 md2pdf.py <file.md>")

        md = sys.argv[1]

        check(md)
        convert(md)

    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except ValueError as val_error:
        print(val_error)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
