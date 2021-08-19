''' Gokul D
    Best Enlist Python Internship
    Final Project - Certificate Generator using Python'''


# Importing Neccessary Package
import xlrd
from PIL import Image, ImageDraw, ImageFont

# Opening Excel sheet
Excel = xlrd.open_workbook("details.xlsx")

# Mentioning Excel sheet pointer as 0
Sheet = Excel.sheet_by_index(0)

# Collecting and adding Entry from the Excel Sheet 
Excel_Names=[]
for i in range(Sheet.nrows):
    temp=[]
    temp.append(Sheet.row_values(i)[0])
    Excel_Names.append(temp)
j=1

for i in Excel_Names:

    # To open Certificate to append Name
    img = Image.open('Certificate.png')
    draw = ImageDraw.Draw(img)

    # Location where the Text to be added in pixels
    location = (337, 332)

    # Font Color in RGB
    text_color = (139,69,19)

    # Font Type and Size
    font = ImageFont.truetype("VLADIMIR.ttf", 60)

    # To Embed NAME using Location, Text Colour, Font type and size
    draw.text(location, i[0], fill = text_color, font = font)

    # To save the Generated Certificates as PNG File
    img.save("Certificate of Appreciation" + str(j) + ".png")
    j+=1

# Completion Message
print("Certificate Generated Successfully !!")
