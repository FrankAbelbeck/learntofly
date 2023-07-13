#!/usr/bin/env python3

import markdown
import html
import datetime
import re

if __name__ == "__main__":
	
	# read from input
	md = markdown.Markdown(extensions=["smarty","toc"])
	with open("PFCLAug20.md","r") as f:
		strHtml = md.convert(f.read())
	
	lstStack = [0]
	strHtmlOut = ""
	intStart = 0
	for matchHeading in re.finditer(r"""<h([1-6]).*?/h\1>""",strHtml,re.M | re.S):
		intMStart = matchHeading.start(0)
		intMStop  = matchHeading.end(0)
		intHeading  = int(matchHeading.group(1))
		
		strClosing = ""
		while lstStack[-1] >= intHeading:
			lstStack.pop()
			strClosing = strClosing + "</div>"
		
		strHtmlOut = strHtmlOut + strHtml[intStart:intMStart] + strClosing + strHtml[intMStart:intMStop] + "<div class=container>"
		lstStack.append(intHeading)
		intStart = intMStop
	
	# write to file
	with open("PFCLAug20.md.html","w") as f:
		f.write("""<!DOCTYPE html>
<html lang=en>
<!--
2023 (C) Frank Abelbeck <frank@abelbeck.info>

    Dieses Programm ist Freie Software: Sie können es unter den Bedingungen
    der GNU General Public License, wie von der Free Software Foundation,
    Version 3 der Lizenz oder (nach Ihrer Wahl) jeder neueren
    veröffentlichten Version, weiter verteilen und/oder modifizieren.

    Dieses Programm wird in der Hoffnung bereitgestellt, dass es nützlich sein wird, jedoch
    OHNE JEDE GEWÄHR,; sogar ohne die implizite
    Gewähr der MARKTFÄHIGKEIT oder EIGNUNG FÜR EINEN BESTIMMTEN ZWECK.
    Siehe die GNU General Public License für weitere Einzelheiten.

    Sie sollten eine Kopie der GNU General Public License zusammen mit diesem
    Programm erhalten haben. Wenn nicht, siehe <https://www.gnu.org/licenses/>.

Erstellt aus dem EASA-Part-FCL-Dokument vom August 2020
-->
<head>
	<meta charset=utf8>
	<meta name=viewport content="width=device-width, initial-scale=1.0">
<!--	<link rel="shortcut icon" type=image/svg+xml href=favicon.svg> -->
	<title>Part-FCL Syllabus</title>
	<script>

function funOnLoad() {
	document.querySelectorAll("h1,h2,h3,h4,h5,h6").forEach(
		element => element.onclick = funToggle
	);
}

function funToggle() {
	if (this.nextElementSibling.style.display != "block") {
		this.nextElementSibling.style.display = "block";
	}
	else {
		this.nextElementSibling.style.display = "none";
	}
}
	</script>
	<style>
body {
	counter-reset: h1;
}
h1 {
	counter-reset: h2;
	font-size: 125%;
}
h2 {
	counter-reset: h3;
	font-size: 120%;
}
h3 {
	counter-reset: h3;
	font-size: 115%;
}
h4 {
	counter-reset: h3;
	font-size: 110%;
}
h5 {
	counter-reset: h3;
	font-size: 105%;
}
h6 {
	counter-reset: h3;
	font-size: 100%;
}

h1:before {
	counter-increment: h1;
	content: counter(h1) ") ";
}
h2:before {
	counter-increment: h2;
	content: counter(h1) "." counter(h2) ") ";
}
h3:before {
	counter-increment: h3;
	content: counter(h1) "." counter(h2) "." counter(h3) ") ";
}
h4:before {
	counter-increment: h4;
	content: counter(h1) "." counter(h2) "." counter(h3) "." counter(h4) ") ";
}
h5:before {
	counter-increment: h5;
	content: counter(h1) "." counter(h2) "." counter(h3) "." counter(h4) "." counter(h5) ") ";
}
h6:before {
	counter-increment: h6;
	content: counter(h1) "." counter(h2) "." counter(h3) "." counter(h4) "." counter(h5) "." counter(h6) ") ";
}

.container {
	display : none;
}
	</style>
</head>

<body onload="funOnLoad()">
<main>
<article>
""" + strHtmlOut + f"""
</article>
</main>
<footer>
<p>edited on {datetime.datetime.now(tz=datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')} by <a href=mailto:frank@abelbeck.info>Frank Abelbeck</a></p>
</footer>
</body>
</html>
""")
