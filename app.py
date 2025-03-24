import streamlit as st

def evaluar_ingreso(mujer):
    """Evalúa si una mujer puede ingresar al refugio según los criterios."""
    inclusion = (
        mujer.get("situacion_violencia", False) and
        mujer.get("riesgo_vida_integridad", False) and
        mujer.get("mayor_edad", False) and
        (
            not mujer.get("redes_apoyo", True) or  
            mujer.get("indigena", False) or  
            (
                mujer.get("victima_delito", False) and
                not mujer.get("vinculo_delincuencia", False) and
                mujer.get("sin_redes_apoyo_viables", False) and
                mujer.get("pleno_ejercicio_derechos", True)
            ) or
            (
                mujer.get("diagnostico_psiquiatrico", False) and
                mujer.get("tratamiento_manejable", True)
            )
        )
    )
    
    exclusion = (
        mujer.get("vinculo_delincuencia", False) or
        mujer.get("enfermedad_cronica", False) or
        (
            mujer.get("diagnostico_psiquiatrico", False) and
            not mujer.get("tratamiento_manejable", True)
        ) or
        (mujer.get("consumo_sustancias", False) and mujer.get("consumo_reciente", False)) or
        mujer.get("riesgo_suicidio_alto", False)
    )
    
    if inclusion and not exclusion:
        return "Ingreso Aprobado"
    else:
        return "Ingreso Denegado"

st.title("Evaluación de Ingreso al Refugio")

situacion_violencia = st.checkbox("Situación de violencia")
riesgo_vida_integridad = st.checkbox("Riesgo de vida e integridad")
mayor_edad = st.checkbox("Mayor de edad")
redes_apoyo = st.checkbox("Cuenta con redes de apoyo")
indigena = st.checkbox("Es indígena")
victima_delito = st.checkbox("Víctima de delito")
vinculo_delincuencia = st.checkbox("Vinculada a delincuencia organizada o trata")
sin_redes_apoyo_viables = st.checkbox("Sin redes de apoyo viables")
pleno_ejercicio_derechos = st.checkbox("En pleno ejercicio de sus derechos")
diagnostico_psiquiatrico = st.checkbox("Diagnóstico psiquiátrico")
tratamiento_manejable = st.checkbox("En tratamiento psiquiátrico manejable")
enfermedad_cronica = st.checkbox("Padece enfermedad crónica grave")
consumo_sustancias = st.checkbox("Consumo de sustancias")
consumo_reciente = st.checkbox("Consumo reciente de sustancias")
riesgo_suicidio_alto = st.checkbox("Riesgo alto de suicidio")

datos_mujer = {
    "situacion_violencia": situacion_violencia,
    "riesgo_vida_integridad": riesgo_vida_integridad,
    "mayor_edad": mayor_edad,
    "redes_apoyo": redes_apoyo,
    "indigena": indigena,
    "victima_delito": victima_delito,
    "vinculo_delincuencia": vinculo_delincuencia,
    "sin_redes_apoyo_viables": sin_redes_apoyo_viables,
    "pleno_ejercicio_derechos": pleno_ejercicio_derechos,
    "diagnostico_psiquiatrico": diagnostico_psiquiatrico,
    "tratamiento_manejable": tratamiento_manejable,
    "enfermedad_cronica": enfermedad_cronica,
    "consumo_sustancias": consumo_sustancias,
    "consumo_reciente": consumo_reciente,
    "riesgo_suicidio_alto": riesgo_suicidio_alto
}

if st.button("Evaluar Ingreso"):
    resultado = evaluar_ingreso(datos_mujer)
    st.write(f"**Resultado:** {resultado}")
