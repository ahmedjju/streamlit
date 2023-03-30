import pickle
import streamlit as st

# loading the trained model
pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)


@st.cache()
# defining the function which will make the prediction using the data which the user inputs
def prediction(Age, Gender, Total_Protiens, Albumin_and_Globulin_Ratio, Albumin):
    # Pre-processing user input
    if Gender == "Male":
        Gender = 3
    else:
        Gender = 0

    Albumin_and_Globulin_Ratio = Albumin_and_Globulin_Ratio / 1000

    # Making predictions 
    prediction = classifier.predict(
        [[Age, Gender, Total_Protiens, Albumin_and_Globulin_Ratio, Albumin]])

    if prediction == 0:
        pred = 'negative'
    else:
        pred = 'positive'
    return pred


# this is the main function in which we define our webpage  
def main():
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit Loan Prediction ML App</h1> 
    </div> 
    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html=True)

    # following lines create boxes in which user can enter data required to make prediction 
    Age = st.number_input("votre age ")
    Gender = st.selectbox('Gender', ("Male", "Female"))

    Total_Protiens = st.number_input("resultats de protiens")
    Albumin_and_Globulin_Ratio = st.number_input("Albumin_and_Globulin_Ratio")
    Albumin = st.number_input("Albumin")
    result = ""

    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"):
        result = prediction(Age, Gender, Total_Protiens, Albumin_and_Globulin_Ratio, Albumin)
        st.success('Your  {}'.format(result))
        print(Albumin_and_Globulin_Ratio)


if __name__ == '__main__':
    main()
