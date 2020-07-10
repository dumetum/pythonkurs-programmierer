rm ../FolienPDF/05-Ableitung.pdf
rm ../FolienAsciidoc/05-Ableitung.html
asciidoctor-pdf --template-require ./../Build/template.js ../FolienAsciidoc/05-Ableitung.adoc -o ../FolienPDF/05-Ableitung.pdf
rm ../FolienAsciidoc/05-Ableitung.html
