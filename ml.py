st.sidebar.subheader('Training Dataset')
status, df = file_upload('Please upload a training dataset')

if status == True:
    col_names = list(df)

    st.title('Training')
    st.subheader('Parameters')
    col1, col2, col3 = st.columns((3,3,2))

    with col1:
        feature_cols = st.multiselect('Please select features',col_names)
    with col2:
        label_col = st.selectbox('Please select label',col_names)
    with col3:
        test_size = st.number_input('Please enter test size',0.01,0.99,0.25,0.05)

  
