rm ../FolienPDF/03-Funktionen.pdf
rm ../FolienAsciidoc/03-Funktionen.html
asciidoctor-pdf --template-require ./../Build/template.js ../FolienAsciidoc/03-Funktionen.adoc -o ../FolienPDF/03-Funktionen.pdf
rm ../FolienAsciidoc/03-Funktionen.html
