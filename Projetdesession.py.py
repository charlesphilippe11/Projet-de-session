import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


st.markdown('<p class="font3"> Travail de session FIN30521 par Charles-Philippe</p>', unsafe_allow_html=True)


st.markdown(""" <style> 
.font1 {
        font-size:35px ;
        font-family: 'Cooper Black';
        color: #FF9633;
        text-align: center;
        border: 3px solid green;
       
        } 

.font2 {
        font-size:25px ;
        font-family: 'Cooper Black';
        color: gold;
        text-align: center;
        border: 3px solid blue;

        }

.font3 {
        font-size:25px ;
        font-family: 'Cooper Black';
        color: lightskyblue;
        text-align: center;
        border: 3px solid lightgreen;

        } 
</style> """,
unsafe_allow_html=True)


st.markdown('<p class="font1"> Ce programme calcule la VAN de deux projets de quatre ans de durée et décide lequel est accepté et lequel est rejeté</p>', unsafe_allow_html=True)


c1, c2 = st.columns(2)
VA_A = []
with c1:
    st.subheader("Projet A:")
    
    i_a = st.number_input('Quel est le rendement exigé sur le projet A ?: ', value = 0.12)
    
    FM0_A = st.number_input("Entrez l'investissent initial (postif)", value = 500_000)
    FM1_A = st.number_input('Entrez le FM1_A', value = 400_000)
    FM2_A = st.number_input('Entrez le FM2_A', value = 200_000)
    FM3_A = st.number_input('Entrez le FM3_A', value = 100_000)
    FM4_A = st.number_input('Entrez le FM4_A', value = 120_000)
    va_1A = FM1_A/(1+i_a)
    va_2A = FM2_A/(1+i_a)**2
    va_3A = FM3_A/(1+i_a)**3
    va_4A = FM4_A/(1+i_a)**4
    VA_A = [- FM0_A, va_1A, va_2A, va_3A, va_4A]
    VAN_A = sum(VA_A)
    
    st.markdown(f'<p class="font2"> La VAN du projet A est: {sum(VA_A):,.2f} $</p>', unsafe_allow_html=True)

VA_B = []
with c2:
    st.subheader("Projet B:")

    i_b = st.number_input('Quel est le rendement exigé sur le projet B ?: ', value = 0.14)
    
    FM0_B = st.number_input("Entrez l'investissent initial (positif)", value = 500_000)
    FM1_B = st.number_input('Entrez le FM1_B', value = 20_000)
    FM2_B = st.number_input('Entrez le FM2_B', value = 300_000)
    FM3_B = st.number_input('Entrez le FM3_B', value = 500_000)
    FM4_B = st.number_input('Entrez le FM4_B', value = 110_000)
    va_1B = FM1_B/(1+i_b)
    va_2B = FM2_B/(1+i_b)**2
    va_3B = FM3_B/(1+i_b)**3
    va_4B = FM4_B/(1+i_b)**4
    VA_B = [-FM0_B, va_1B, va_2B, va_3B, va_4B]
    VAN_B = sum(VA_B)
    st.markdown(f'<p class="font2"> La VAN du projet B est: {sum(VA_B):,.2f} $</p>', unsafe_allow_html=True)

    


   
VAN_A = sum(VA_A)
VAN_B = sum(VA_B)






if VAN_A < 0 and VAN_B < 0:
    st.markdown('<p class="font1"> Les deux projets A et B sont rejetés</p>', unsafe_allow_html=True)
elif VAN_A < VAN_B:
    st.markdown('<p class="font1"> Le projet B sera choisit et on rejette le projet A</p>', unsafe_allow_html=True)
elif VAN_A == VAN_B:
    st.markdown('<p class="font1"> Les deux projets ont la même VAN</p>', unsafe_allow_html=True)
elif VAN_A > VAN_B:
    st.markdown('<p class="font1"> Le projet A est accepté et on rejette le projet B</p>', unsafe_allow_html=True)

R = np.arange(0.01, 0.50, 0.02)
VAN_A_list = []
VAN_B_list = []

for r in R: 
    VAN_A = FM0_A + FM1_A/(1+r) + FM2_A/(1+r)**2 + FM3_A/(1+r)**3 + FM4_A/(1+r)**4
    VAN_B = FM0_B + FM1_B/(1+r) + FM2_B/(1+r)**2 + FM3_B/(1+r)**3 + FM4_B/(1+r)**4
    VAN_A_list.append(VAN_A)
    VAN_B_list.append(VAN_B)

st.markdown("""
Ce graphique présente l'évolution des VAN en fonction du taux exigé:
""")
fig1, ax1 = plt.subplots(facecolor = 'skyblue')


ax1.plot(R, VAN_A_list, color = 'purple',label = "projet A")
ax1.plot(R, VAN_B_list, color = 'darkolivegreen',label = "Projet B")

# titre et nom des axes ( x,y ) du graphique 
ax1.set_title(' VAN des deux projets ')
ax1.set_xlabel('Taux exigé', color = 'k')
ax1.set_ylabel('VAN', color = 'k')
ax1.legend()
ax1.grid(color='lightgrey', linestyle='--', linewidth=0.5)
st.pyplot(fig1)
