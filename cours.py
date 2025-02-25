class Product:
    LOYER = 150000
    JIRAMA = 50000
    BANQUE = 460000
    ECOLAGE = 50000
    SAKAFO = 130000
    CARBURANT = 80000
    EPARGNE = 250000
    SALARIE1 = 200000
    LIVRAISON = 80000
    DAYS_IN_MONTH = 26
    WEEKLY_DIVISOR = 4
    WEEKLY_RESELLER_COUNT = 20

    def __init__(self, name, price=250):
        self.name = name
        self.price = price
    
    def calculate_sales_targets(self):
        total_charge = self.calculate_total_charges()
        
        daily_target = total_charge / self.price / self.DAYS_IN_MONTH
        weekly_target = daily_target * self.DAYS_IN_MONTH / self.WEEKLY_DIVISOR
        reseller_target = (total_charge / self.price / self.WEEKLY_RESELLER_COUNT) / self.WEEKLY_DIVISOR
        
        return (
            f"Total charges : {total_charge:,.0f} ar\n"
            f"Prix de vente {self.name} : {self.price:.0f} ar\n"
            f"Objectif journalier : {daily_target:.0f} pièces\n"
            f"Objectif hebdomadaire : {weekly_target:.0f} pièces\n"
            f"Nombre de revendeurs : {reseller_target:.0f}\n"
            f"Bénéfice annuel : {self.EPARGNE * 12:,.0f}"
        )

    def calculate_total_charges(self):
        directeur = sum([
            self.LOYER, self.JIRAMA, self.BANQUE, self.ECOLAGE, 
            self.SAKAFO, self.CARBURANT, self.EPARGNE
        ])
        salarie = sum([self.SALARIE1, self.LIVRAISON])
        return directeur + salarie


product = Product('Sakay')
print(product.calculate_sales_targets())

