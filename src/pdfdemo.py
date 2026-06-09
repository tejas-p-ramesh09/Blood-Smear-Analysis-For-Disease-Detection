from fpdf import FPDF
from PIL import Image
import glob
def process(pname,age,gen,doc,totalrbc,totalwbc,totalplatelets,class_name,treat):
    treat1=[]
    treat1=str(treat).split('\n')
    print("treat1",treat1)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 10, 'Blood Smear Analysis Report !',0,1,'c')
    pdf.cell(40, 10, 'Patient Name:',0,0,'c')
    pdf.cell(40,10,pname,0,1,'c')
    pdf.cell(40, 10, 'Patient Age:',0,0,'c')
    pdf.cell(40,10,age,0,1,'c')
    pdf.cell(40, 10, 'Gender:',0,0,'c')
    pdf.cell(40,10,gen,0,1,'c')
    pdf.cell(40, 10, 'Doctor:',0,0,'c')
    pdf.cell(40,10,doc,0,1,'c')
    pdf.cell(40, 10, 'Your RBC is :',0,0,'c')
    pdf.cell(40,10,str(totalrbc),0,1,'c')
    pdf.cell(40, 10, 'Your WBC is :',0,0,'c')
    pdf.cell(40,10,str(totalwbc),0,1,'c')
    pdf.cell(40, 10, 'Your Platelets :',0,0,'c')
    pdf.cell(40,10,str(totalplatelets),0,1,'c')
    pdf.cell(40, 10, 'Disease:',0,0,'c')
    pdf.cell(40,10,class_name,0,1,'c')
    pdf.cell(40, 10, 'Treatment:',0,0,'c')
    for item in treat1:
        pdf.cell(40,10,str(item),0,1,'c')
        
    
    path=pname+'.pdf'
    pdf.output(path, 'F')
    print("Pdf Created")
#process('p1','eswar','3','Male')
