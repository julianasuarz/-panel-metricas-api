from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

app = FastAPI(
    title="Panel de Operaciones - Fibra Óptica",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def inicio():
    return FileResponse("index.html")


@app.get("/api/metricas")
def obtener_metricas():

    return {
        "empresa": "Contratista de Fibra Óptica",
        "cliente": "Claro",
        "periodo": "Septiembre 2026",

        "obras_activas": 12,
        "obras_terminadas": 38,
        "tecnicos": 64,
        "metros_fibra": 184750,
        "avance_general": 78,
        "incidencias": 7,
        "ordenes_pendientes": 23,
        "cumplimiento": 94,
        "productividad": 87,

        "presupuesto": 12500000,
        "ejecutado": 9825000,

        "cuadrillas": {
            "activas": 18,
            "disponibles": 4,
            "mantenimiento": 2
        },

        "actividad": [
            {
                "tipo": "obra",
                "titulo": "Obra FTTH finalizada",
                "detalle": "Sector Norte - Mar del Plata",
                "hora": "Hace 12 min"
            },
            {
                "tipo": "fibra",
                "titulo": "2.450 metros instalados",
                "detalle": "Cuadrilla FTTH-08",
                "hora": "Hace 28 min"
            },
            {
                "tipo": "incidencia",
                "titulo": "Nueva incidencia reportada",
                "detalle": "Nodo MDQ-042",
                "hora": "Hace 41 min"
            },
            {
                "tipo": "orden",
                "titulo": "Orden de trabajo asignada",
                "detalle": "Cuadrilla FTTH-12",
                "hora": "Hace 55 min"
            }
        ],

        "obras": [
            {
                "codigo": "FTTH-001",
                "nombre": "Zona Norte",
                "zona": "Mar del Plata",
                "avance": 92,
                "cuadrilla": "FTTH-08",
                "estado": "En ejecución"
            },
            {
                "codigo": "FTTH-002",
                "nombre": "Zona Sur",
                "zona": "Mar del Plata",
                "avance": 82,
                "cuadrilla": "FTTH-12",
                "estado": "En ejecución"
            },
            {
                "codigo": "FTTH-003",
                "nombre": "Barrio Constitución",
                "zona": "Mar del Plata",
                "avance": 68,
                "cuadrilla": "FTTH-04",
                "estado": "En ejecución"
            },
            {
                "codigo": "FTTH-004",
                "nombre": "Zona Puerto",
                "zona": "Mar del Plata",
                "avance": 100,
                "cuadrilla": "FTTH-02",
                "estado": "Finalizada"
            },
            {
                "codigo": "FTTH-005",
                "nombre": "Zona Oeste",
                "zona": "Mar del Plata",
                "avance": 54,
                "cuadrilla": "FTTH-15",
                "estado": "En ejecución"
            }
        ],

        "productividad": {
            "labels": [
                "Lun",
                "Mar",
                "Mié",
                "Jue",
                "Vie",
                "Sáb",
                "Dom"
            ],
            "metros": [
                18200,
                22500,
                19800,
                27100,
                25400,
                21300,
                20450
            ],
            "ordenes": [
                42,
                51,
                47,
                63,
                59,
                48,
                45
            ]
        }
    }