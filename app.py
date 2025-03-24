import streamlit as st

def evaluar_ingreso(mujer):
    """
    Evalúa si una mujer puede ingresar al refugio según los criterios actualizados.
    """
    inclusion = (
        mujer.get("situacion_violencia", False) and
        mujer.get("riesgo_vida_integridad", False) and
        mujer.get("mayor_edad", False) and
        (
            not mujer.get("redes_apoyo", True) or  
            mujer.get("indigena", False) or  
            mujer.get("pleno_ejercicio_derechos", True)
        ) and
        (
            not mujer.get("diagnostico_psiquiatrico_riesgoso", False)
        ) and
        (
            not mujer.get("consumo_sustancias_reciente", False)
        ) and
        (
            not mujer.get("riesgo_suicidio", False)
        ) and
        (
            mujer.get("hijos_menores_14", True)
        )
    )
    
    exclusion = (
        mujer.get("vinculo_delincuencia", False) or
        mujer.get("enfermedad_cronica", False) or
        mujer.get("diagnostico_psiquiatrico_riesgoso", False) or
        mujer.get("consumo_sustancias_reciente", False) or
        mujer.get("riesgo_suicidio", False)
    )
    
    if inclusion and not exclusion:
        return "Ingreso Aprobado"
    else:
        return "Ingreso Denegado"

st.title("Evaluación de Ingreso al Refugio")

situacion_violencia = st.checkbox("Situación de violencia que pone en riesgo la vida")
riesgo_vida_integridad = st.checkbox("Riesgo de vida e integridad física")
mayor_edad = st.checkbox("Mayor de edad")
hijos_menores_14 = st.checkbox("Tiene hijos menores de 14 años")
redes_apoyo = st.checkbox("Cuenta con redes de apoyo")
indigena = st.checkbox("Es indígena")
pleno_ejercicio_derechos = st.checkbox("En pleno ejercicio de sus derechos")
vinculo_delincuencia = st.checkbox("Vinculada a delincuencia organizada o trata")
enfermedad_cronica = st.checkbox("Padece enfermedad crónica o degenerativa")
diagnostico_psiquiatrico_riesgoso = st.checkbox("Diagnóstico psiquiátrico que pone en riesgo su seguridad o la de otros")
consumo_sustancias_reciente = st.checkbox("Consumo reciente de sustancias (menos de un mes)")
riesgo_suicidio = st.checkbox("Riesgo de suicidio (intento en el último año)")

datos_mujer = {
    "situacion_violencia": situacion_violencia,
    "riesgo_vida_integridad": riesgo_vida_integridad,
    "mayor_edad": mayor_edad,
    "hijos_menores_14": hijos_menores_14,
    "redes_apoyo": redes_apoyo,
    "indigena": indigena,
    "pleno_ejercicio_derechos": pleno_ejercicio_derechos,
    "vinculo_delincuencia": vinculo_delincuencia,
    "enfermedad_cronica": enfermedad_cronica,
    "diagnostico_psiquiatrico_riesgoso": diagnostico_psiquiatrico_riesgoso,
    "consumo_sustancias_reciente": consumo_sustancias_reciente,
    "riesgo_suicidio": riesgo_suicidio
}

if st.button("Evaluar Ingreso"):
    resultado = evaluar_ingreso(datos_mujer)
    st.write(f"**Resultado:** {resultado}")

