# https://www.geeksforgeeks.org/python-convert-image-to-pdf-using-img2pdf-module/
# Python3 program to convert image to pfd
# using img2pdf library

# importing necessary libraries
import img2pdf
from PIL import Image
import os


#baca file csv
#convert per file

#--------example------------------
# folder KT-PEMKAB-SERUYAN-10
# file csv KT-PEMKAB-SERUYAN-10.csv
#--------------------------

# pecah nama file csv untuk membaca folder
def split_name(name):
    split_text = name.split('-')
	
    text_len = len(split_text)
    
    if(text_len <= 5):
		#kt-pemkab-seruyan-9-link2jpg2 = 5 kalimat
        #print("pecah 5")
        #print(split_text[0])
        #print(split_text[1])
        #print(split_text[2])
        #print(split_text[3])
        
        split_text = split_text[0].upper()+'-'+split_text[1].upper()+'-'+split_text[2].upper()+'-'+split_text[3].upper()
    else:
		#kt-pemprov-kalimantan-tengah-9-link2jpg2 = 6 kalimat
        #print("pecah 6")
        #print(split_text[0])
        #print(split_text[1])
        #print(split_text[2])
        #print(split_text[3])
        #print(split_text[4])
        
        split_text = split_text[0].upper()+'-'+split_text[1].upper()+'-'+split_text[2].upper()+'-'+split_text[3].upper()+'-'+split_text[4].upper()
    return split_text

def main():
    print("------------- file hasil link2jpg2 (tanpa .csv)-------------")
    file_csv = input("*Nama File CSV: ")

    path_csv = os.getcwd() +'/'+ split_name(file_csv) +'/'+ file_csv
    print('---baca csv---')
    print(path_csv)
    print(split_name(file_csv))

    with open(path_csv + '.csv') as f:
        array_gambar = [s for line in f.readlines() for s in line[:-1].split(',')]
        #print(array_gambar)

        for file_png in array_gambar:
            print(file_png)
            
            #file_csv = input("*Nama File CSV: ")

            # storing image path
            img_path = "D:/MEDIA-KT/PY/KT-PEMKAB-SERUYAN-10/"
            
            # storing pdf path
            pdf_path = "D:/MEDIA-KT/PY/KT-PEMKAB-SERUYAN-10/"
            
            # opening image
            image = Image.open(img_path+file_png)
            
            # converting into chunks using img2pdf
            pdf_bytes = img2pdf.convert(image.filename)
            
            # opening or creating pdf file
            file = open(pdf_path+file_png+'.pdf', "wb")
            
            # writing pdf files with chunks
            file.write(pdf_bytes)
            
            # closing image file
            image.close()
            
            # closing pdf file
            file.close()
            
            # output
            print("Successfully made pdf file")

if __name__ == '__main__':
    main()