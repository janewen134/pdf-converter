from pdf2image import convert_from_path
# I think the 500 is number of pages
pages = convert_from_path('1.pdf', 500)
i=0
for page in pages:
    page.save('images/out'+i+'.png', 'PNG')
    i=i+1
    
