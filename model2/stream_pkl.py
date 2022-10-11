import joblib
import streamlit as st
import pickle as pkl

loaded_model_pkl = pkl.load(open( "finalized_XGBoost_pickle_model.pkl",'rb'))

#https://github.com/dpakkaushik/Deployment/blob/main/finalized_XGBoost_model.sav

def predict_note_authentication(a, b, c, d, e, f, g, h, i, j, k, l, m):


    prediction = loaded_model_pkl.predict([[a, b, c, d, e, f, g, h, i, j, k, l, m]])
    print(prediction)
    return prediction


#result = predict_note_authentication(0.90983087, 0., 0.64296296, 0.54876413, 0.80851064, 0.24617984,
                                      #0.31174334, 1., 0., 1., 0., 0., 1.)

#print(result)

def main():
    st.title("Rossman Store")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    a = st.number_input("a",min_value=0.,max_value=1.0,step=1e-6,format="%.5f")
    b = st.number_input("b",min_value=0.,max_value=1.0,step=1e-6,format="%.5f")
    c = st.number_input("c",min_value=0.,max_value=1.0,step=1e-6,format="%.5f")
    d = st.number_input("d",min_value=0.,max_value=1.0,step=1e-6,format="%.5f")
    e = st.number_input("e",min_value=0.,max_value=1.0,step=1e-6,format="%.5f")
    f = st.number_input("f",min_value=0.,max_value=1.0,step=1e-6,format="%.5f")
    g = st.number_input("g",min_value=0.,max_value=1.0,step=1e-6,format="%.5f")
    h = st.number_input("h",min_value=0.,max_value=1.0,step=1e-6,format="%.5f")
    i = st.number_input("i",min_value=0.,max_value=1.0,step=1e-6,format="%.5f")
    j = st.number_input("j",min_value=0.,max_value=1.0,step=1e-6,format="%.5f")
    k = st.number_input("k",min_value=0.,max_value=1.0,step=1e-6,format="%.5f")
    l = st.number_input("l",min_value=0.,max_value=1.0,step=1e-6,format="%.5f")
    m = st.number_input("m",min_value=0.,max_value=1.0,step=1e-6,format="%.5f")
    result = ""
    if st.button("Predict"):
        result = predict_note_authentication(a, b, c, d, e, f, g, h, i, j, k, l, m)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")


if __name__ == '__main__':
    main()
