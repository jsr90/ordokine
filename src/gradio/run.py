import gradio as gr
import requests
import json
from datetime import datetime
from utils.utils import ajouter_patient, ajouter_dispositif, obtenir_praticiens, obtenir_patients, obtenir_dispositifs, generer_ordonnance

# Obtenir la date d'aujourd'hui
date = datetime.now().strftime("%Y-%m-%d")

def reload_dropdowns():
    """
    Recharge les listes déroulantes avec les praticiens, patients et dispositifs disponibles.
    """
    praticiens = [(f"{p['nom']}", p) for p in obtenir_praticiens()]
    patients = [(f"{p['nom']}, {p['prenom']}", p) for p in obtenir_patients()]
    dispositifs = [(d['nom'], d) for d in obtenir_dispositifs()]
    return gr.Dropdown(choices=patients), gr.Dropdown(choices=dispositifs)

with gr.Blocks() as demo:
    with gr.Tab("Générer Prescription"):
        with gr.Row():
            with gr.Column():
                praticien_input = gr.Dropdown(choices=[(
                    f"{p['nom']}", p) for p in obtenir_praticiens()], label="Sélectionnez un praticien")
                patient_input = gr.Dropdown(choices=[(
                    f"{p['nom']}, {p['prenom']}", p) for p in obtenir_patients()], label="Sélectionnez un patient")
                dispositifs_input = gr.Dropdown(multiselect=True,
                                                choices=[(d['nom'], d) for d in obtenir_dispositifs()], label="Sélectionnez un dispositif")
                date_input = gr.DateTime(
                    label="Sélectionner Date", include_time=False, type="string", value=date)
                quantity_input = gr.Number(
                    label="Sélectionnez une quantité", value=1)

                b = gr.Button("Générer l'ordonnance")

                result_output2 = gr.Markdown()

            with gr.Column():
                result_output = gr.Markdown()

            b.click(generer_ordonnance, inputs=[
                praticien_input, patient_input, dispositifs_input, date_input], outputs=result_output)

    with gr.Tab("Ajouter Patient/Dispositif"):
        with gr.Row("Ajouter un patient"):
            with gr.Column():
                nom_input = gr.Textbox(label="Nom")
                prenom_input = gr.Textbox(label="Prénom")
                date_naissance_input = gr.DateTime(
                    label="Date de Naissance", include_time=False, type="string")
                nir_input = gr.Textbox(label="NIR", value=None)
                ajout_result = gr.Markdown()
                gr.Button("Ajouter Patient").click(ajouter_patient, inputs=[
                    nom_input, prenom_input, date_naissance_input, nir_input], outputs=ajout_result).then(
                    reload_dropdowns, outputs=[patient_input, dispositifs_input])

            with gr.Column("Ajouter un dispositif"):
                nom_dispositif_input = gr.Textbox(label="Nom du Dispositif")
                description_dispositif_input = gr.Textbox(
                    label="Description du Dispositif")
                ajout_dispositif_result = gr.Markdown()
                gr.Button("Ajouter Dispositif").click(ajouter_dispositif, inputs=[
                    nom_dispositif_input, description_dispositif_input],
                    outputs=ajout_dispositif_result).then(
                    reload_dropdowns, outputs=[patient_input, dispositifs_input])

if __name__ == "__main__":
    demo.launch(server_port=7860)
