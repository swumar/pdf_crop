import glob
from PyPDF2 import PdfFileWriter, PdfFileReader

inputFile = glob.glob("input/*.pdf")[0]
pdfInFile = open(inputFile,"rb")
pdfReader1 = PdfFileReader(pdfInFile)
pdfReader2 = PdfFileReader(pdfInFile)
pdfReader3 = PdfFileReader(pdfInFile)
pdfReader4 = PdfFileReader(pdfInFile)
pdfWriter1 = PdfFileWriter()
pdfWriter2 = PdfFileWriter()

numPages = pdfReader1.getNumPages()

for i in range(numPages):

  page1 = pdfReader1.getPage(i)
  page1.mediaBox.lowerLeft = (0, 423)
  page1.mediaBox.lowerRight = (296, 423)
  page1.mediaBox.upperLeft = (0, 842)
  page1.mediaBox.upperRight = (296, 842)
  pdfWriter1.addPage(page1)

  page2 = pdfReader2.getPage(i)
  page2.mediaBox.lowerLeft = (0, 0)
  page2.mediaBox.lowerRight = (296, 0)
  page2.mediaBox.upperLeft = (0, 419)
  page2.mediaBox.upperRight = (296, 419)
  pdfWriter1.addPage(page2)
  
  page3 = pdfReader3.getPage(i)
  page3.mediaBox.lowerLeft = (299, 423)
  page3.mediaBox.lowerRight = (595, 423)
  page3.mediaBox.upperLeft = (299, 842)
  page3.mediaBox.upperRight = (595, 842)
  pdfWriter2.addPage(page3)

  page4 = pdfReader4.getPage(i)
  page4.mediaBox.lowerLeft = (299, 0)
  page4.mediaBox.lowerRight = (595, 0)
  page4.mediaBox.upperLeft = (299, 419)
  page4.mediaBox.upperRight = (595, 419)
  pdfWriter2.addPage(page4)

with open("output/label.pdf", "wb") as outf1:
  pdfWriter1.write(outf1)

with open("output/invoice.pdf", "wb") as outf2:
  pdfWriter2.write(outf2)