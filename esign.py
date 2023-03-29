from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
import io
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors



input_pdf = PdfReader(open("./test.pdf", "rb"))
output_pdf = PdfWriter()

for i in range(len(input_pdf.pages)):
    output_pdf.add_page(input_pdf.pages[i])


output_stream = open("output.pdf", "wb")
output_pdf.write(output_stream)
output_stream.close()

output_pdf = PdfWriter()
output_pdf.add_metadata({
    '/Title': '5Gsign',
    '/Author': 'Cmic',
    '/Subject': 'Cmic Auto Sign',
    '/Creator': 'YCQ create',
    '/Producer': 'Inner Man',
    '/Keywords': 'esign 5Gsign'
})
output_pdf.write(open("./test1.pdf", "wb"))

# 获取pdf文件信息
pdf_file = open("example.pdf", "rb")
# 创建一个 Reader 对象来读取 PDF 文件
pdf_Reader = PdfReader(pdf_file)
# 获取文档信息，返回的是一个字典对象
document_info = pdf_Reader.metadata
print(document_info)

# 拆分pdf文件：将每一页单独保存为一个pdf文档
input_pdf = PdfReader(open("example.pdf", "rb"))
for i in range(len(input_pdf.pages)):
    output_pdf = PdfWriter()
    output_pdf.add_page(input_pdf.pages[i])
    output_stream = open(f"page_{i+1}.pdf", "wb")
    output_pdf.write(output_stream)
    output_stream.close()

pdf_files = ["example1.pdf", "example2.pdf", "example3.pdf"]
output_pdf = PdfWriter()


for pdf_file in pdf_files:
    input_pdf = PdfReader(open(pdf_file, "rb"))
    for i in range(len(input_pdf.pages)):
        output_pdf.add_page(input_pdf.pages[i])
output_stream = open(f"merged.pdf", "wb")
output_pdf.write(output_stream)
output_stream.close()




# 输入pdf文件名
input_file_name = "unsigned.pdf"

# 输出的签名pdf文件名
output_file_name = "signed.pdf"

# 签名位置
x = 300
y = 720 
color = colors.red

# 读取原始的pdf文件
input_pdf = PdfReader(open(input_file_name, "rb"))
# 创建签名
packet = io.BytesIO()
can = canvas.Canvas(packet, pagesize=letter)
can.setFillColor(color)
can.setFontSize(10)
can.drawString(x, y, "Signed by Cmic")
can.save()

# 读取签名数据
packet.seek(0)
signature_pdf = PdfReader(packet)
# 创建一个新的pdf文件，将签名添加到指定页码、指定位置
output_pdf = PdfWriter()
for i in range(len(input_pdf.pages)):
    page = input_pdf.pages[i]
    if i == 0:
        page.merge_page(signature_pdf.pages[0])
    output_pdf.add_page(page)

# 将签名后的pdf文件保存到本地
output_pdf_stream = open(output_file_name, "wb")
output_pdf.write(output_pdf_stream)
output_pdf_stream.close()