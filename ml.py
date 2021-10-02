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

    with st.expander('Advanced Parameters'):
        col2_1, col2_2 = st.columns(2)
        with col2_1:
            penalty = st.selectbox('Penalty',['l2','l1','elasticnet','none'])
            tol = st.number_input('Tolerance (1e-4)',value=1)/10000
            fit_intercept = st.radio('Intercept',[True,False])
            class_weight = st.radio('Class weight',[None,'balanced'])
            solver = st.selectbox('Solver',['lbfgs','newton-cg','liblinear','sag','saga'])
            multi_class = st.selectbox('Multi class',['auto','ovr','multinomial'])
            warm_start = st.radio('Warm start',[False,True]) 
         with col2_2:
            dual = st.radio('Dual or primal formulation',[False,True])
            C = st.number_input('Inverse regularization strength',0.0,99.0,1.0,0.1)
            intercept_scaling = st.number_input('Intercept scaling',0.0,99.0,1.0,0.1)
            random_state = st.radio('Random state',[None,'Custom'])
            if random_state == 'Custom':
random_state = st.number_input('Custom random state',0,99,1,1)
            max_iter = st.number_input('Maximum iterations',0,100,100,1)
            verbose = st.number_input('Verbose',0,99,0,1)
            l1_ratio = st.radio('L1 ratio',[None,'Custom'])
            if l1_ratio == 'Custom':
                l1_ratio = st.number_input('Custom l1 ratio',0.0,1.0,1.0,0.01)
