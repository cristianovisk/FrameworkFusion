import os
from opencre_lib.compare import Map
import streamlit as st
import pandas as pd
from uuid import uuid4


st.image(image="images/logo_frameworkfusion_ai.svg")
st.echo("Test")
bases = Map(primary="CWE", secundary="ASVS").bases
primary = st.selectbox(label="Primary", options=bases)
secundary = st.selectbox(label="Secundary", options=bases)

if st.button(label="Generate"):
    output = f"{uuid4()}.xlsx"
    try:
        map = Map(primary=primary, secundary=secundary).generate_table()
        df = pd.DataFrame(map)
        df.to_excel(output, sheet_name="COMPARE", index=False)
        st.success(f"Finded {len(df)} correlations between '{primary}' and '{secundary}'", icon="✅")
        with open(output, "rb") as file:
            btn = st.download_button(
                label="Download Spreedsheet",
                data=file,
                file_name=output
            )
        st.balloons()
        st.toast(f"**File generated**: *{output}* 📁")
        os.remove(output)
    except:
        st.error(f"Error to compare {primary} -> {secundary}")
        
    