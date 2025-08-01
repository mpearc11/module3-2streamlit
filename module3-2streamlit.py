from Bio.Seq import Seq
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import streamlit as st

st.title('Module 3-2')

dna_seq = st.text_input('paste your dna sequence')
dna_seq = Seq(dna_seq)

if st.button('translate dna sequence'):
    translation = dna_seq.translate()
    st.write('protein sequence: ' + str(translation))

unprocessed_seq = st.text_input('paste your unprocessed protein sequence')

if st.button('analyze unprocessed sequence'):
    unprocessed_param = ProteinAnalysis(unprocessed_seq)
    st.subheader('UNPROCESSED')
    st.write('number of amino acids = ' + str(len(unprocessed_seq)))
    st.write('molecular weight = ' + str(unprocessed_param.molecular_weight()) + ' daltons')
    st.write('pI = ' + str(unprocessed_param.isoelectric_point()))
    st.markdown('extinction coefficient = ' + str(unprocessed_param.molar_extinction_coefficient()[1]) + ' M<sup>-1</sup> cm<sup>-1</sup>')

processed_seq = st.text_input('paste your processed protein sequence')

if st.button('analyze processed sequence'):
    processed_param = ProteinAnalysis(processed_seq)
    st.subheader('PROCESSED')
    st.write('number of amino acids = ' + str(len(processed_seq)))
    st.write('molecular weight = ' + str(processed_param.molecular_weight()) + ' daltons')
    st.write('pI = ' + str(processed_param.isoelectric_point()))
    st.write('extinction coefficient = ' + str(processed_param.molar_extinction_coefficient()[1]) + ' M<sup>-1</sup> cm<sup>-1</sup>')

#tag_seq = Seq("MGSSHHHHHHSSGDYKDDDKLEVLFQGP")
#unprocessed_seq = tag_seq + prot_seq[1:]
#processed_seq = prot_seq[1:]
