class ImpressoraPDF:
    def imprimir(self, contingut):
        print(f"Imprimint PDF: {contingut}")


class Factura:
    def __init__(self, client, import_total, impressora):
        self.client = client
        self.import_total = import_total
        self.impressora = impressora  # Acoplament directe

    def imprimir_factura(self):
        contingut = f"Factura per a {self.client}, total: {self.import_total} €"
        self.impressora.imprimir(contingut)

