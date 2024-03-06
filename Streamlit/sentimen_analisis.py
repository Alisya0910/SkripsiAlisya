#mengimport library  yang dibutuhkan
import streamlit as st
import pandas as pd



def main():
    st.title('Analisis sentimen menggunakan data twitter untuk Pemilu Presiden')

    menu = st.sidebar.radio("Pilih tahapan proses",("Hasil Data Crawling","Hasil Data preprocessing","Hasil Klasifikasi Algoritma","Hasil Akhir"))

    if menu == "Hasil Data Crawling":
      st.header("Hasil Data Crawling")
      st.subheader("1. Hasil data Crawling tentang Anies Baswedan")
      data = pd.read_excel('AniesPresidentTweets.xlsx')
      st.write(data)

      st.subheader("2. Hasil data Crawling tentang Ganjar Pranowo")
      data = pd.read_excel('GanjarPresidentTweets.xlsx')
      st.write(data)
      

      st.subheader("3. Hasil data Crawling tentang Prabowo Subianto")
      data = pd.read_excel('PrabowoPresidentTweets.xlsx')
      st.write(data)

    if menu == "Hasil Data preprocessing":
      st.subheader("1. Hasil Data Preprocessing tentang Anies Baswedan")
      data = pd.read_excel('Preprocessed_Anies.xlsx')
      st.write(data)
      st.write('Banyaknya Data Sentimen Anies Baswedan')
      col1,col2 = st.columns(2)
      with col1:
        st.image('SS/SenDis_Anies.png')
      with col2:
        st.image('SS/SenDis_Anies(1).png')

      st.subheader("2. Hasil data Preprocessing tentang Ganjar Pranowo")
      data = pd.read_excel('Preprocessed_Ganjar.xlsx')
      st.write(data)
      st.write('Banyaknya Data Sentimen Ganjar Pranowo')
      col1,col2 = st.columns(2)
      with col1:
        st.image('SS/SenDis_Ganjar.png')
      with col2:
        st.image('SS/SenDis_Ganjar(1).png')

      st.subheader("3. Hasil data Preprocessing tentang Prabowo Subianto)
      data = pd.read_excel('Preprocessed_Prabowo.xlsx')
      st.write(data)
      st.write('Banyaknya Data Sentimen Prabowo Subianto')
      col1,col2 = st.columns(2)
      with col1:
        st.image('SS/SenDis_Prabowo.png')
      with col2:
        st.image('SS/SenDis_Prabowo(1).png')

    if menu == "Hasil Klasifikasi Algoritma":
      st.header('Hasil Klasifikasi Naive Bayes dan Regresi Logistik')
      tab1, tab2, tab3 = st.tabs(["Hasil Klasifikasi Data Anies Baswedan","Hasil Klasifikasi Data Ganjar Pranowo","Hasil Klasifikasi Data Prabowo Subianto"])

      with tab1:
        st.subheader("1. Klasifikasi Naive Bayes")
        st.write()
      
        col1,col2 = st.columns(2)
        with col1:
          st.image('SS/HasilNB_Anies.png')
        with col2:
          st.image('SS/NB_Anies.png')
          
        st.subheader("2. Klasifikasi Regresi Logistik")
        st.write()      
        col1,col2 = st.columns(2)
        with col1:
          st.write()
          st.image('SS/HasilLR_Anies.png')
        with col2:
          st.write()
          st.image('SS/LR_Anies.png')  
      with tab2:
        st.subheader("1. Klasifikasi Naive Bayes")
        st.write()
      
        col1,col2 = st.columns(2)
        with col1:
          st.image('SS/HasilNB_Ganjar.png')
        with col2:
          st.image('SS/NB_Ganjar.png')
          
        st.subheader("2. Klasifikasi Regresi Logistik")
        st.write()      
        col1,col2 = st.columns(2)
        with col1:
          st.write()
          st.image('SS/HasilLR_Ganjar.png')
        with col2:
          st.write()
          st.image('SS/LR_Ganjar.png')  

      with tab3:
        st.subheader("1. Klasifikasi Naive Bayes")
        st.write()
      
        col1,col2 = st.columns(2)
        with col1:
          st.image('SS/HasilNB_Prabowo.png')
        with col2:
          st.image('SS/NB_Prabowo.png')
          
        st.subheader("2. Klasifikasi Regresi Logistik")
        st.write()      
        col1,col2 = st.columns(2)
        with col1:
          st.write()
          st.image('SS/HasilLR_Prabowo.png')
        with col2:
          st.write()
          st.image('SS/LR_Prabowo.png')  

    else:
      st.header("Hasil Akhir")
      st.write('Dari table tersebut kita data mengkonklusikan bahwa Naive Bayes merupakan Permodelan yang memiliki nilai akurasi yang lebih unggul dengan nilai akurasi 63%, 77% dan 44%, dibandingkan Regresi Logistik yang nilai akurasinya 61%, 77%, dan 41%.')
      st.image('SS/HasilAkhir.png')

      
      


# Run the app
if __name__ == '__main__':
    main()