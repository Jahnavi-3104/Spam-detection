import pickle
import streamlit as st

model=pickle.load(open("spam.pkl","rb"))
cv=pickle.load(open("vectorizer.pkl", "rb"))

def main():
	st.title("SMS Spam Detection")
	msg=st.text_input("Enter a text: ")
	if st.button("Predict"):
		data=[msg]
		vect=cv.transform(data).toarray()
		prediction=model.predict(vect)
		result=prediction[0]
		if result==1:
			st.error("This is a spam mail")
		else:
			st.success("This is a ham mail")

main()