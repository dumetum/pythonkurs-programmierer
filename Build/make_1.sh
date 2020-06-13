rm ../FolienPDF/01-Datentypen.pdf
rm ../FolienAsciidoc/01-Datentypen.html
asciidoctor-pdf --template-require ./../Build/template.js ../FolienAsciidoc/01-Datentypen.adoc -o ../FolienPDF/01-Datentypen.pdf
rm ../FolienAsciidoc/01-Datentypen.html
