rm ../FolienPDF/04-OOP.pdf
rm ../FolienAsciidoc/04-OOP.html
asciidoctor-pdf --template-require ./../Build/template.js ../FolienAsciidoc/04-OOP.adoc -o ../FolienPDF/04-OOP.pdf
rm ../FolienAsciidoc/04-OOP.html
