import streamlit as st

def render_header():
    st.markdown("""
        <style>
        /* Sticky Header Styling - Adjusted Height */
        .sticky-header {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background-color: #1f77b4;
            color: white;
            z-index: 9999;
            box-shadow: 0 4px 6px rgba(0,0,0,0.3);
            padding-top: 50px;
            padding-bottom: 10px;  
            text-align: center;

            /* Flexbox untuk centering konten */
            display: flex;
            flex-direction: column;
            justify-content: center;  /* Center secara vertikal */
            align-items: center;      /* Center secara horizontal */
        }

        .sticky-header h2 {
            margin: 0;
            font-size: 40px;
        }

        .sticky-header h4 {
            margin: 1px 1 5 10;
            font-weight: normal;
            color: #ecf0f1;
            font-size: 16px;
        }

        /* Spacer untuk menyesuaikan konten di bawah header */
        .spacer {
            margin-top: 120px;  /* Menyesuaikan dengan tinggi header */
        }

        @media screen and (max-width: 480px) {
            .sticky-header h2 {
                font-size: 22px;
            }

            .sticky-header h4 {
                font-size: 14px;
            }

            .spacer {
                margin-top: 55px;
            }
        }
        </style>

        <div class="sticky-header">
            <h2>📸 NeuraScope 🔍</h2>
            <h4>Sistem Cerdas Berbasis AI untuk Deteksi Gambar Otomatis</h4>
        </div>
        <div class="spacer"></div>
    """, unsafe_allow_html=True) 
