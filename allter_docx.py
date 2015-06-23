#latin-1
from docx import Document


document = Document("a.docx")

a = document.paragraphs

for i in a:
	#print i.text
	i.text = i.text.replace('<<<ggggg>>>', 'Victor')
	#print '--------------------------'
	#print i.text
'''
print "for 2"
for i in a:
	
	print i.text
'''

document.save("a.docx")