rm ../FolienPDF/02-Kontrollstrukturen.pdf
rm ../FolienAsciidoc/02-Kontrollstrukturen.html
asciidoctor-pdf --template-require ./../Build/template.js ../FolienAsciidoc/02-Kontrollstrukturen.adoc -o ../FolienPDF/02-Kontrollstrukturen.pdf
rm ../FolienAsciidoc/02-Kontrollstrukturen.html
