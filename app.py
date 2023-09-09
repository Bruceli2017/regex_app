import exrex
import streamlit as st
from streamlit_extras.buy_me_a_coffee import button
from tdda import rexpy

st.set_page_config(
    page_title='Data to Regex',
    layout='wide',
)


def main():

    cs_body()


def cs_body():

    with st.container():
        st.header('Data to Regex')
        col1, col2 = st.columns(2)
        # Data to regex
        col1.subheader('Input data')
        corpus = col1.text_area(label='input', placeholder='Paste your data', value='',
            label_visibility='collapsed', height=50)
        # print(corpus)
        corpus = corpus.split('\n')
        col2.subheader('Output regex')
        regex_output = data2regex(corpus)
        for regex in regex_output:
            col2.code(regex)
    
    with st.container():
        col1, col2 = st.columns(2)
        col1.subheader('Example input:')
        col1.code("""
            EH1 3LH
            BB2 5NR
        """)
        col2.subheader('Example output:')
        col2.code("^[A-Z]{2}[0-9] [0-9][A-Z]{2}$")

    # Regex to data
    with st.container():
        st.header('Regex to Data')
        col1, col2 = st.columns(2)
        
        col1.subheader('Input regex')
        regex_input = col1.text_input('Enter the regex')
        
        col2.subheader('Output data')
        count = col2.number_input('How many data?', value=20)
        output_list = []
        for _ in range(count):
            # exrex.getone(regex_input.encode('unicode_escape'))
            output_list.append(exrex.getone(r'{}'.format(regex_input)))
        if output_list:
            col2.code('\n'.join(output_list))

    st.markdown('The website will not store any input or output data. Wish it could help you')
    st.markdown('[Contact author](mailto:abraver@livemail.tw)')
    button(username="abraverE", floating=False, width=250)


def data2regex(corpus:list[str]) -> list:
    result = rexpy.extract(corpus)
    return result


if __name__ == '__main__':
    main()