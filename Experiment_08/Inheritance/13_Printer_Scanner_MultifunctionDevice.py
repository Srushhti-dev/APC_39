class Printer:
    def print_document(self, document):
        print("Printing:", document)


class Scanner:
    def scan_document(self, document):
        print("Scanning:", document)


class MultifunctionDevice(Printer, Scanner):
    def copy_document(self, document):
        self.scan_document(document)
        self.print_document(document)
        print("Copy completed.")


device = MultifunctionDevice()
device.print_document("Report.pdf")
device.scan_document("Photo.jpg")
device.copy_document("Assignment.pdf")
