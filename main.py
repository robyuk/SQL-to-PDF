#! /usr/bin/env /usr/bin/python3
# Reads from a SQLITE database outputs to outfile
db='database.db'
outfile='database'
pageformat='A4'
pageorient='P'  # Portrait page orientation
units='pt'      # Measure size in points
tblborder=1     # Table border
cw=100          # Cell width in units
ch=25           # Cell height
headerfont='Times'
headerstyle='B' # Bold
headersize=14   # Header font size in units
cellfont='Times'
cellstyle=''    # Normal font style (not bold or italic etc.)
cellsize=14

import sqlite3
from fpdf import FPDF

# Establish a connection to the database
con=sqlite3.connect(db)
cur=con.cursor()

# Create a PDF object, add a page for the output, and set font
pdf=FPDF(orientation=pageorient, unit=units, format=pageformat)
pdf.add_page()
pdf.set_font(family=headerfont, style=headerstyle, size=headersize)

# Get a list of tuples. each tuple represents a column in the 'ips' table
cur.execute('PRAGMA table_info(ips)')
columns=cur.fetchall()
print(columns)
exit(0)
# We only want the column names (2nd item in each tuple) in the pdf document
for colname in columns:
  pdf.cell(w=cw, h=ch, txt=colname[1], border=tblborder)

# Get the remaining rows
rows=cur.execute("SELECT * FROM 'ips'")

# Set the pdf font to normal
pdf.set_font(family=cellfont, style=cellstyle, size=cellsize)

#Add the rows to the pdf table
for row in rows:
  pdf.ln()
  for cell in row:
    pdf.cell(w=cw, h=ch, txt=str(cell), border=tblborder)

pdf.output(f'{outfile}.pdf')
