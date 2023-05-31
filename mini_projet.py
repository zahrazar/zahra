from tkinter import *


class GABApplication:
    def __init__(self):
        self.fenetre_principale = Tk()
        self.fenetre_principale.title("GAB")
        self.fenetre_principale.geometry("320x300")
        self.fenetre_principale.configure(background="#FFDEAD")
        self.message = Label(self.fenetre_principale, fg="red", background="#FFDEAD")

        w = Label(self.fenetre_principale, text="WELCOME TO FLOR BANK", bg="#D2B48C", width="300", height="3",
                  font=("Giorgia", 12, "italic", "bold"), bd=5, relief="groove")
        w.pack()

        self.saisir_mdp = Label(self.fenetre_principale, text="Entrer votre mot de passe:", fg="BLACK",
                                bg="#D2B48C", font=("Giorgia", 10, "italic", "bold"), bd=1, relief="groove")
        self.saisir_mdp.pack()
        self.saisir_mdp.place(x=80, y=100)

        self.mot_de_passe_entry = Entry(self.fenetre_principale, show="*", bg="#E5E5E5", bd=3, relief="groove")
        self.bouton_valider = Button(self.fenetre_principale, text="Valider", command=self.validation, bd=3,
                                     relief="groove", bg="#D2B48C")

        self.mot_de_passe_entry.place(x=95, y=130)
        self.bouton_valider.place(x=135, y=170)
        self.message.place(x=70, y=200)

    def run(self):
        self.fenetre_principale.mainloop()

    def validation(self):
        with open("fich.txt", "r") as file:
            lignes = file.readlines()
            informations = [ligne.strip().split(",") for ligne in lignes]
            mot_de_passe_entre = self.mot_de_passe_entry.get()
            for info in informations:
                if mot_de_passe_entre == info[0]:
                    self.afficher_options(info[0], info[1], info[2], float(info[3]))
                    return
            self.message.config(text="votre mot de passe est incorrect", fg="red", bg="#FFDEAD")

    def afficher_options(self, password, nom, prenom, solde):
        fenetre_options = Toplevel(self.fenetre_principale)
        fenetre_options.geometry("320x70")
        fenetre_options.configure(background="#FFDEAD")
        fenetre_options.title("GESTION GAB")

        bouton_solde = Button(fenetre_options, text="Solde", command=lambda: self.afficher_solde(solde),
                              background="#D2B48C")
        bouton_retirer = Button(fenetre_options, text="Retirer", command=lambda: self.retirer(password, solde),
                               background="#D2B48C")
        bouton_informations = Button(fenetre_options, text="Vos informations",
                                     command=lambda: self.infos(password, nom, prenom, solde),
                                     background="#D2B48C")
        bouton_envoyer = Button(fenetre_options, text="Envoyer de l'argent",
                                command=lambda: self.envoyer_argent(password),
                                background="#D2B48C")

        bouton_solde.place(x=5, y=20)
        bouton_retirer.place(x=50, y=20)
        bouton_informations.place(x=100, y=20)
        bouton_envoyer.place(x=205, y=20)

    def retirer(self, password, solde):
        def retirer_solde():
            nonlocal solde
            montant = float(montant_entry.get())
            if montant > solde:
                msg = Label(fenetre_retirer)
                msg.config(text="Le montant demandé est supérieur à votre solde.", fg="red", font=("georgia", 8),
                           bg="#FFDEAD")
                msg.pack()
            else:
                solde -= montant
                msg1 = Label(fenetre_retirer)
                msg1.config(text=f"Retrait de {montant} Dhs effectué avec succès", fg="green", font=("georgia", 8),
                            bg="#FFDEAD")
                msg1.pack()

                with open("fich.txt", "r") as file:
                    lignes = file.readlines()

                with open("fich.txt", "w") as file:
                    for ligne in lignes:
                        info = ligne.strip().split(",")
                        if info[0] == password:
                            info[3] = str(solde)
                            ligne = ",".join(info) + "\n"
                        file.write(ligne)

        fenetre_retirer = Toplevel()
        fenetre_retirer.geometry("320x200")
        fenetre_retirer.title("Retirer")
        fenetre_retirer.configure(bg="#FFDEAD")

        Label(fenetre_retirer, text="Montant à retirer:", font=("Georgia", 8, "bold", "italic"), bd=3,
              relief="groove", background="#D2B48C").place(x=20, y=50)
        montant_entry = Entry(fenetre_retirer, bd=3, relief="groove")
        montant_entry.place(x=170, y=50)

        valider_button = Button(fenetre_retirer, text="Valider", command=retirer_solde,
                                font=("Georgia", 8, "bold", "italic"), bd=3, relief="groove", background="#D2B48C")
        valider_button.place(x=80, y=100)

        quitter_button = Button(fenetre_retirer, text="Quitter", command=fenetre_retirer.destroy,
                                font=("Georgia", 8, "bold", "italic"), bd=3, relief="groove", background="#D2B48C")
        quitter_button.place(x=150, y=100)

    def infos(self, password, nom, prenom, solde):
        fenetre_informations = Toplevel()
        fenetre_informations.title("vos informations")
        fenetre_informations.geometry("350x200")
        fenetre_informations.configure(background="#FFDEAD")

        Label(fenetre_informations, text="Mot de passe:", width=15, font=("Georgia", 10, "bold", "italic"), bd=5,
              relief="groove", background="#D2B48C").grid(row=0, column=0, padx=10, pady=10)
        Label(fenetre_informations, text=password, width=15, font=("Georgia", 10, "bold", "italic"), bd=5,
              relief="groove", background="#D2B48C").grid(row=0, column=1, padx=10, pady=10)
        Label(fenetre_informations, text="Nom:", width=15, font=("Georgia", 10, "bold", "italic"), bd=5, relief="groove",
              background="#D2B48C").grid(row=1, column=0, padx=10, pady=10)
        Label(fenetre_informations, text=nom, width=15, font=("Georgia", 10, "bold", "italic"), bd=5, relief="groove",
              background="#D2B48C").grid(row=1, column=1, padx=10, pady=10)
        Label(fenetre_informations, text="Prénom:", width=15, font=("Georgia", 10, "bold", "italic"), bd=5,
              relief="groove", background="#D2B48C").grid(row=2, column=0, padx=10, pady=10)
        Label(fenetre_informations, text=prenom, width=15, font=("Georgia", 10, "bold", "italic"), bd=5, relief="groove",
              background="#D2B48C").grid(row=2, column=1, padx=10, pady=10)
        Label(fenetre_informations, text="Solde:", width=15, font=("Georgia", 10, "bold", "italic"), bd=5,
              relief="groove", background="#D2B48C").grid(row=3, column=0, padx=10, pady=10)
        Label(fenetre_informations, text=str(solde) + " Dhs", width=15, font=("Georgia", 10, "bold", "italic"), bd=5,
              relief="groove", background="#D2B48C").grid(row=3, column=1, padx=10, pady=10)

    def afficher_solde(self, solde):
        fenetre_solde = Toplevel()
        fenetre_solde.geometry("300x150")
        fenetre_solde.title("Votre solde")
        fenetre_solde.configure(background="#FFDEAD")

        Label(fenetre_solde, text="Votre solde est de :", font=("Georgia", 10, "bold", "italic"), bd=3, relief="groove",
              background="#D2B48C").place(x=20, y=50)
        solde_label = Label(fenetre_solde, text=str(solde) + " Dhs", font=("Georgia", 10, "bold", "italic"), bd=3,
                            relief="groove", background="#D2B48C")
        solde_label.place(x=170, y=50)

    def envoyer_argent(self, password):
        fenetre_envoi = Toplevel()
        fenetre_envoi.title("Envoyer de l'argent")
        fenetre_envoi.geometry("320x200")
        fenetre_envoi.configure(background="#FFDEAD")

        Label(fenetre_envoi, text="Montant à envoyer:", font=("Georgia", 8, "bold", "italic"), bd=3,
              relief="groove", background="#D2B48C").place(x=20, y=50)
        montant_entry = Entry(fenetre_envoi, bd=3, relief="groove")
        montant_entry.place(x=170, y=50)

        Label(fenetre_envoi, text="Compte bénéficiaire:", font=("Georgia", 8, "bold", "italic"), bd=3,
              relief="groove", background="#D2B48C").place(x=20, y=90)
        compte_entry = Entry(fenetre_envoi, bd=3, relief="groove")
        compte_entry.place(x=170, y=90)

        def envoyer():
            montant = float(montant_entry.get())
            compte = compte_entry.get()

            with open("fich.txt", "r") as file:
                lignes = file.readlines()

            with open("fich.txt", "w") as file:
                for ligne in lignes:
                    info = ligne.strip().split(",")
                    if info[0] == password:
                        if float(info[3]) >= montant:
                            info[3] = str(float(info[3]) - montant)
                            ligne = ",".join(info) + "\n"
                            file.write(ligne)
                            msg = Label(fenetre_envoi)
                            msg.config(text=f"{montant} Dhs envoyés avec succès au compte {compte}", fg="green",
                                       font=("georgia", 8),
                                       bg="#FFDEAD")
                            msg.place(x=20, y=130)
                            return
                        else:
                            msg = Label(fenetre_envoi)
                            msg.config(text="Le montant demandé est supérieur à votre solde.", fg="red",
                                       font=("georgia", 8),
                                       bg="#FFDEAD")
                            msg.place(x=20, y=130)
                            return
                    file.write(ligne)

        valider_button = Button(fenetre_envoi, text="Valider", command=envoyer,
                                font=("Georgia", 8, "bold", "italic"), bd=3, relief="groove", background="#D2B48C")
        valider_button.place(x=80, y=150)

        quitter_button = Button(fenetre_envoi, text="Quitter", command=fenetre_envoi.destroy,
                                font=("Georgia", 8, "bold", "italic"), bd=3, relief="groove", background="#D2B48C")
        quitter_button.place(x=150, y=150)


if __name__ == "__main__":
    app = GABApplication()
    app.run()
