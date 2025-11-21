// Base de datos no relacional para MongoDB

// Colección de clínicas particulares
db.clinicas_particulares.insertMany([
  {
    nombre: "Clínica Santa María",
    direccion: "Av. Siempre Viva 123",
    ciudad: "Quito",
    telefono: "022345678",
    tipo_servicio: "Medicina general",
    horario: "08:00-20:00",
    num_consultorios: 10,
    tiene_emergencias: true
  },
  {
    nombre: "Centro Médico Vida Sana",
    direccion: "Calle 10 de Agosto 456",
    ciudad: "Guayaquil",
    telefono: "042223344",
    tipo_servicio: "Pediatría",
    horario: "09:00-18:00",
    num_consultorios: 6,
    tiene_emergencias: false
  }
]);

// Colección de parques recreativos
db.parques_recreativos.insertMany([
  {
    nombre: "Parque La Alegría",
    direccion: "Av. Los Álamos s/n",
    ciudad: "Quito",
    area_m2: 15000,
    tipo_parque: "Infantil",
    tiene_juegos_infantiles: true,
    tiene_parqueadero: true,
    precio_entrada: 0.00,
    horario: "07:00-19:00"
  },
  {
    nombre: "Aventura Park",
    direccion: "Km 5 Vía a la Costa",
    ciudad: "Guayaquil",
    area_m2: 25000,
    tipo_parque: "Acuático",
    tiene_juegos_infantiles: true,
    tiene_parqueadero: true,
    precio_entrada: 5.50,
    horario: "09:00-18:00"
  }
]);

// Consultas de ejemplo

// Todas las clínicas
db.clinicas_particulares.find();

// Clínicas con emergencias
db.clinicas_particulares.find({ tiene_emergencias: true });

// Parques gratuitos
db.parques_recreativos.find({ precio_entrada: 0 });

// Parques en una ciudad específica (ejemplo Quito)
db.parques_recreativos.find({ ciudad: "Quito" });
