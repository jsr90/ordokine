from fpdf import FPDF
import webbrowser
from datetime import datetime

def generate_pdf(praticien, patient, dispositifs, prescription):

    class PDF(FPDF):
        def header(self):
            self.set_font('Helvetica', 'B', 13)
            self.cell(0, 10, praticien['nom'].upper(
            )+' '+praticien['prenom'].capitalize(), align='C', ln=True)
            self.set_font('Helvetica', 'I', 11)
            self.cell(0, 8, praticien['profession'], align='C', ln=True)
            self.cell(
                0, 8, praticien['numero_professionnel'], align='C', ln=True)
            self.cell(0, 8, praticien['adresse']['voie'], align='C', ln=True)
            self.cell(0, 8, praticien['adresse']['code_postal']+' ' +
                      praticien['adresse']['ville'].upper(), align='C', ln=True)
            self.cell(
                0, 8, f"{praticien['telephone']} / {praticien['portable']}", align='C', ln=True)
            self.cell(0, 8, f"{praticien['email']}", align='C', ln=True)
            self.ln(10)

        def footer(self):
            self.set_y(-25)
            self.set_font('Helvetica', 'I', 10)
            self.cell(0, 10, praticien['nom'].upper(
            )+' '+praticien['prenom'].capitalize(), 0, 0, 'C')
            self.set_y(-20)
            self.cell(0, 10, f"Cabinet de kinésithérapie - {praticien['adresse']['voie']}. {praticien['adresse']['code_postal']}, {praticien['adresse']['ville']}",
                      0, 0, 'C')
            self.set_y(-15)
            self.cell(
                0, 10, f"{praticien['telephone']} - {praticien['portable']}", 0, 0, 'C')

    pdf = PDF()
    pdf.add_page()

    # Date et lieu
    pdf.set_y(75)
    pdf.set_font('Helvetica', size=12)
    date_prescription = datetime.strptime(
        prescription['date_prescription'], "%Y-%m-%d").strftime('%d/%m/%Y')
    pdf.cell(
        0, 10, f"À {praticien['adresse']['ville']}, le {date_prescription}", ln=True, align='R')

    # Patient
    line = f"{patient['nom'].upper()} {patient['prenom'].capitalize()}"
    if patient.get('date_naissance'):
        date_naissance = datetime.strptime(
            patient['date_naissance'], '%a, %d %b %Y %H:%M:%S %Z').strftime('%d/%m/%Y')
        line += f", né(e) le {date_naissance}"
    if patient.get('nir'):
        line += f" ({patient['nir']})"
    pdf.set_font('Helvetica', 'B', size=12)
    pdf.cell(0, 10, line, ln=True, border=0)

    # Dispositif(s)
    pdf.set_font('Helvetica', size=12)
    for dispositif in dispositifs:
        l = f"  - {dispositif['nom']}"
        l += f": {str(dispositif.get('quantity', 1))} unité(s)"
        pdf.cell(0, 10, l, ln=True, border=0)

    # Chemin pour enregistrer le fichier PDF
    print(prescription)
    file_path = f"{patient['nom'].upper()}_{patient['prenom'].capitalize()}_{prescription['_id']}.pdf"

    # Enregistrer le fichier PDF
    pdf.output(file_path)

    # Ouvrir le fichier PDF dans nouvel onglet du navigateur
    webbrowser.open_new_tab(file_path)

    return f"Ordonnance générée avec succès dans {file_path}."
