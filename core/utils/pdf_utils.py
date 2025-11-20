from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from django.http import HttpResponse

# Default paragraph style for wrapping text
default_style = ParagraphStyle(
    'cell_style',
    fontSize=10,
    leading=12,
    wordWrap='LTR'
)

def generate_pdf_response(filename, table_headers, table_data, col_widths=None):
    """
    Generates a PDF response with given table headers and data.
    :param filename: Name of the PDF file
    :param table_headers: List of column headers
    :param table_data: List of rows (each row is a list of cell values or Paragraphs)
    :param col_widths: Optional list of column widths
    :return: HttpResponse with PDF
    """
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    pdf = SimpleDocTemplate(response, pagesize=A4)
    elements = []

    # Prepend headers to data
    data = [table_headers] + table_data

    table = Table(data, colWidths=col_widths)

    # Table style
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.25, colors.grey),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.whitesmoke]),
        ('BOTTOMPADDING', (0,0), (-1,0), 10),
    ]))

    elements.append(table)
    pdf.build(elements)

    return response
