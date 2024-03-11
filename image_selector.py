class ImageSelector:
    def __init__(self):
        self.original_image = None
        self.scanned_image = None
        self.game_sheets = ["Empty","5e"]
        
    def setSheet(self):
        sheet_election = input("¿Qué ficha quieres transformar? Elige entre las siguientes opciones escribiendo solo el número:\n[1] D&D Fifth Edition\n")
        
        self.original_image = f"originals/{self.game_sheets[int(sheet_election)]}_sheet_1.jpg"
        print(self.original_image)
        return self.original_image
    
    def setScannedImage(self):
        scan_extension = "png"
        scan_input = input("Escribe aquí el nombre exacto del achivo que quieres transformar, sin la extensión: ")
        scan_extension_input = input("¿Cuál es la extensión del archivo? Elige entre las extensiones soportadas escribiendo solo el número:\n[1]JPG\n[2]PNG\n")
        if scan_extension_input == "1":
            scan_extension = "jpg"
            print(scan_extension)
            
        self.scanned_image = f"scans/{scan_input}.{scan_extension}"
        print (self.scanned_image)
        
    def getOriginalImage(self):
        return self.original_image
    
    def getScannedImage(self):
        return self.scanned_image
        
    
    

        
        