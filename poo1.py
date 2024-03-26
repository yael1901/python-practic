class persona:
    
    def __init__(self, nombre, edad, correo):
        
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
    def description(self):
        print(f"el nombre es {self.nombre}, su edad es {self.edad} y su correo es {self.correo}")


uno = persona("alexis","18","yael@gmail.com")
dos = persona("yael","25","alexis@gmail.com")
tres = persona("hernandez","35","her@gmail.com")

uno.description()
dos.description()
tres.description()
