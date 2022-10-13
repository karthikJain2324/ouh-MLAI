import joblib
import streamlit as st
import pickle as pkl

loaded_model_pkl = pkl.load(open( "model_rossmann.pkl",'rb'))

Store,DayOfWeek,Date,Open,Promo,StateHoliday,SchoolHoliday,StoreType,Assortment,CompetitionDistance ,CompetitionOpenSinceMonth,CompetitionOpenSinceYear,Promo2,Promo2SinceWeek ,Promo2SinceYear ,PromoInterval

def predict_note_authentication(Store,DayOfWeek,Date,Open,Promo,StateHoliday,SchoolHoliday,StoreType,Assortment,CompetitionDistance ,CompetitionOpenSinceMonth,CompetitionOpenSinceYear,Promo2,Promo2SinceWeek ,Promo2SinceYear ,PromoInterval):


    prediction = loaded_model_pkl.predict([[Store,DayOfWeek,Date,Open,Promo,StateHoliday,SchoolHoliday,StoreType,Assortment,CompetitionDistance ,CompetitionOpenSinceMonth,CompetitionOpenSinceYear,Promo2,Promo2SinceWeek ,Promo2SinceYear ,PromoInterval]])
    print(prediction)
    return prediction


#result = predict_note_authentication(0.90983087, 0., 0.64296296, 0.54876413, 0.80851064, 0.24617984,
                                      #0.31174334, 1., 0., 1., 0., 0., 1.)

def main():
    st.title("Rossman Store Sales Data prediction")
    html_temp = """
    <div style="background-color:blue;padding:10px">
    <h2 style="color:white;text-align:center;">Customer Data Entry </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    a = st.number_input("Store",min_value=0.,max_value=1.0,step=1e-6,format="%.5f")
    b = st.number_input("DayOfWeek",min_value=0.,max_value=1.0,step=1e-6,format="%.5f")
    c = st.number_input("Date",min_value=0.,max_value=1.0,step=1e-6,format="%.5f")
    d = st.number_input("Open",min_value=0.,max_value=1.0,step=1e-6,format="%.5f")
    e = st.number_input("Promo",min_value=0.,max_value=1.0,step=1e-6,format="%.5f")
    f = st.number_input("StateHoliday",min_value=0.,max_value=1.0,step=1e-6,format="%.5f")
    g = st.number_input("SchoolHoliday",min_value=0.,max_value=1.0,step=1e-6,format="%.5f")
    h = st.number_input("StoreType",min_value=0.,max_value=1.0,step=1e-6,format="%.5f")
    i = st.number_input("Assortment",min_value=0.,max_value=1.0,step=1e-6,format="%.5f")
    j = st.number_input("CompetitionDistance",min_value=0.,max_value=1.0,step=1e-6,format="%.5f")
    k = st.number_input("CompetitionOpenSinceMonth",min_value=0.,max_value=1.0,step=1e-6,format="%.5f")
    l = st.number_input("Promo2",min_value=0.,max_value=1.0,step=1e-6,format="%.5f")
    m = st.number_input("Promo2SinceWeek",min_value=0.,max_value=1.0,step=1e-6,format="%.5f")
    n = st.number_input("Promo2SinceYear",min_value=0.,max_value=1.0,step=1e-6,format="%.5f")
    o = st.number_input("Promo2SinceWeek",min_value=0.,max_value=1.0,step=1e-6,format="%.5f")

    result = ""
    if st.button("Predict"):
        result = predict_note_authentication(a, b, c, d, e, f, g, h, i, j, k, l, m)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")


if __name__ == '__main__':
    main()
