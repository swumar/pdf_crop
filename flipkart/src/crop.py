from PyPDF2 import PdfFileWriter, PdfFileReader
import glob

inputFile = glob.glob("input/*.pdf")[0]
pdfInFile = open(inputFile,"rb")
pdfReader1 = PdfFileReader(pdfInFile)
pdfReader2 = PdfFileReader(pdfInFile)
pdfOutFile1 = open("output/label.pdf","wb")
pdfOutFile2 = open("output/invoice.pdf","wb")
pdfWriter1 = PdfFileWriter()
pdfWriter2 = PdfFileWriter()

numPages = pdfReader1.getNumPages()

for i in range(numPages):

    page1 = pdfReader1.getPage(i)
    page1.mediaBox.lowerLeft = (175, 470)
    page1.mediaBox.lowerRight = (420, 470)
    page1.mediaBox.upperLeft = (175, 815)
    page1.mediaBox.upperRight = (420, 815)
    pdfWriter1.addPage(page1)

    page2 = pdfReader2.getPage(i)
    page2.mediaBox.lowerLeft = (0, 0)
    page2.mediaBox.lowerRight = (595, 0)
    page2.mediaBox.upperLeft = (0, 470)
    page2.mediaBox.upperRight = (595, 470)
    pdfWriter2.addPage(page2)

pdfWriter1.write(pdfOutFile1)
pdfWriter2.write(pdfOutFile2)
