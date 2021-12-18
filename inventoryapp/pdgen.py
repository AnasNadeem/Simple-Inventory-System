from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import os


class GenereatePdf:
    def create_inv(self, file_name, cus_name, cus_num, cus_add,invoice_id,crnt_date,total_price,price_in_words):
        # Checking if the folder exists
        crnt_path = os.getcwd()
        bill_fol = 'bill_invoice'
        full_path = os.path.join(crnt_path, bill_fol)
        check_if_exists = os.path.exists(full_path)
        if check_if_exists==False:
            os.mkdir(bill_fol)

        # Main Pdf Code started
        my_canvas = canvas.Canvas(f'{file_name}.pdf',pagesize=A4)
        styles = getSampleStyleSheet()
        
        # Invoice Num
        inv_no_text = f'<font size=12>INVOICE: <b>{invoice_id}</b></font>'
        inv_no_style = styles["Normal"]
        inv_no_para = Paragraph(inv_no_text,style=inv_no_style)
        inv_no_para.wrapOn(my_canvas, 140,20)
        inv_no_para.drawOn(my_canvas, 430,700)
        
        # Company Name
        company_name = f'<font size=24><b>Virtual Company Ltd.</b></font>'
        company_name_style = styles["Normal"]
        company_name_para = Paragraph(company_name,style=company_name_style)
        company_name_para.wrapOn(my_canvas, 340,80)
        company_name_para.drawOn(my_canvas, 280,680)

        # Customer Desc  
        customer_desc = f"""
            <font size=14><b>Bill To:</b></font><br/>
            <font size=12 textColor = Color(0,0,0,0.8)>Customer Name: <b>{cus_name}</b></font><br/>
            <font size=12 textColor = Color(0,0,0,0.8)>Customer Number: <b>{cus_num}</b></font><br/>
            <font size=12 textColor = Color(0,0,0,0.8)>Customer Address: <b>{cus_add}</b></font><br/>
        """
        customer_desc_style = styles["Normal"]
        customer_desc_style.leading=16
        customer_para = Paragraph(customer_desc,style=customer_desc_style)
        customer_para.wrapOn(my_canvas, 500, 240)
        customer_para.drawOn(my_canvas, 40,600)

        # Company Address Desc  
        comp_adr_desc = f"""
            <font size=12 textColor = Color(0,0,0,0.8)>+91-6207781113</font><br/>
            <font size=12 textColor = Color(0,0,0,0.8)>anas5678go@gmail.com</font><br/>
            <font size=12 textColor = Color(0,0,0,0.8)>221B Baker Street</font><br/>
        """
        comp_adr_desc_style = styles["Normal"]
        comp_adr_desc_style.leading=16
        comp_adr_para = Paragraph(comp_adr_desc,style=comp_adr_desc_style)
        comp_adr_para.wrapOn(my_canvas, 180, 80)
        comp_adr_para.drawOn(my_canvas, 390, 600)

        # Product Description 
        colWidths = [270,90, 80, 80]
        b_data = [
                    self.create_bold_text('Item/Description'),
                    self.create_bold_text('Price per unit'),
                    self.create_bold_text('Quantity'),
                    self.create_bold_text('Price')
                ]
        data = []
        data.append(b_data)
        # for prd in prd_list:
        #     data.append(prd)
        
        # Inserting total price
        data.append(['TOTAL', '', '', '2000/-'])


        tblstyle = TableStyle([('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                                ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                                ])

        table = Table(data, colWidths=colWidths)
        table.setStyle(tblstyle)
        table.wrapOn(my_canvas, 620, 400)
        table.drawOn(my_canvas, 40, 460)

        # Note
        note = "<font size=12 textColor = Color(0,0,0,0.6)>Thank you for shopping with us! .</font>"
        note_desc_style = styles["Normal"]
        note_desc_style.leading=16
        note_desc_para = Paragraph(note,style=note_desc_style)
        note_desc_para.wrapOn(my_canvas, 350, 40)
        note_desc_para.drawOn(my_canvas, 200,200)

        my_canvas.showPage()
        my_canvas.save()

    def create_bold_text(self, text, size=12):
        return Paragraph(f"""
        <font size={size}>
        <b>{text}</b>
        </font>
        """)

if __name__=="__main__":
    file_name = 'testing'
    cus_name = "Anas Nadeem"
    cus_num = "6207781113"
    cus_add = "Danapur Patna 801105"
    invoice_id = 1
    crnt_date = "23.12.2021"
    total_price = "2000"
    price_in_words = "Two thousands only"
    gen_pdf = GenereatePdf()
    gen_pdf.create_inv(file_name, cus_name, cus_num, cus_add,invoice_id,crnt_date,total_price,price_in_words)