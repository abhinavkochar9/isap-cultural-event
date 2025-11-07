import streamlit as st
from PIL import Image

# ---------- BASIC PAGE CONFIG ----------
st.set_page_config(
    page_title="ISAO Cultural Event 2026",
    page_icon="🌍",
    layout="wide",
)

# ---------- THEME / CUSTOM CSS ----------
st.markdown(
    """
    <style>
    .stApp {
        background: radial-gradient(circle at top left, #fbe2d4 0, #fdf7f4 40%, #f3d6c4 100%);
        color: #111111;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif;
    }

    .main-block {
        max-width: 1200px;
        margin: 0 auto;
        padding-top: 1.5rem;
        padding-bottom: 2.5rem;
    }

    .hero-title {
        font-family: "Didot", "Playfair Display", Georgia, "Times New Roman", serif;
        font-size: 3rem;
        letter-spacing: 0.22em;
        text-transform: uppercase;
        text-align: center;
        margin-bottom: 0.2rem;
    }

    .hero-subtitle {
        font-family: "Didot", "Playfair Display", Georgia, "Times New Roman", serif;
        font-size: 1.2rem;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        text-align: center;
        margin-bottom: 0.3rem;
    }

    .tagline {
        text-align: center;
        margin-top: 0.2rem;
        font-size: 1rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
    }

    .pill {
        display: inline-block;
        padding: 0.4rem 1.2rem;
        border-radius: 999px;
        border: 1.5px solid #111;
        background-color: #fff7eb;
        font-size: 0.85rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        margin: 0.25rem 0.45rem;
    }

    .section-title {
        font-family: "Didot", "Playfair Display", Georgia, "Times New Roman", serif;
        font-size: 1.2rem;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        margin: 0.3rem 0 0.6rem 0;
        text-align: center;
    }

    .info-text {
        font-size: 0.97rem;
        line-height: 1.6;
        text-align: center;
        margin-bottom: 0.4rem;
    }

    .card {
        background: rgba(255, 250, 244, 0.96);
        border-radius: 18px;
        padding: 1.1rem 1.2rem;
        box-shadow: 0 10px 26px rgba(0, 0, 0, 0.12);
        border: 1px solid rgba(0, 0, 0, 0.06);
        height: 100%;
    }

    .card h3 {
        font-family: "Didot", "Playfair Display", Georgia, "Times New Roman", serif;
        text-transform: uppercase;
        letter-spacing: 0.12em;
        font-size: 0.95rem;
        margin-bottom: 0.4rem;
        text-align: left;
    }

    .card p {
        font-size: 0.9rem;
        line-height: 1.5;
        margin-bottom: 0;
    }

    .footer {
        text-align: center;
        font-size: 0.85rem;
        margin-top: 1.5rem;
        opacity: 0.8;
    }

    .footer a {
        color: inherit;
        text-decoration: none;
        border-bottom: 1px dotted rgba(0,0,0,0.3);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- LOAD IMAGES (match your directory) ----------
hero_img = Image.open("images/Slide1.jpg")   # main collage
booth_img = Image.open("images/Slide2.jpg")  # host a booth
art_img = Image.open("images/Slide3.jpg")    # showcase artistically
bg_soft_1 = Image.open("images/Slide4.jpg")  # soft background
bg_soft_2 = Image.open("images/Slide5.jpg")  # soft background 2 (footer strip)

# ---------- PAGE CONTENT ----------
st.markdown('<div class="main-block">', unsafe_allow_html=True)

# HERO SECTION
st.markdown(
    """
    <p class="hero-subtitle">International Student Ambassadors</p>
    <p class="hero-title">April 18 2026</p>
    <p class="tagline">Our biggest event of the year where culture unites all</p>
    """,
    unsafe_allow_html=True,
)
st.image(hero_img, use_container_width=True)

st.markdown("---")

# WHAT TO EXPECT
st.markdown('<p class="section-title">What to expect</p>', unsafe_allow_html=True)
st.markdown(
    """
    <p class="info-text">
        An open, vibrant celebration of global cultures – with world cuisine, performances,
        community, and connection. Stay tuned for the official event name and full schedule.
    </p>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div style="text-align:center; margin-top: 0.7rem;">
        <span class="pill">World Cuisine</span>
        <span class="pill">Cultural Celebration</span>
        <span class="pill">Community</span>
        <span class="pill">Connection</span>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("")
st.markdown("")

# FEATURED SECTIONS
col1, col2 = st.columns(2, gap="large")

with col1:
    st.image(booth_img, use_container_width=True)
    st.markdown(
        """
        <div class="card" style="margin-top: 0.8rem;">
          <h3>Host an educational booth</h3>
          <p>
            Share the stories, symbols, languages, and traditions that make your culture
            unique. Bring artifacts, games, posters, or interactive activities and turn
            your table into a mini world-tour stop.
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.image(art_img, use_container_width=True)
    st.markdown(
        """
        <div class="card" style="margin-top: 0.8rem;">
          <h3>Showcase your culture artistically</h3>
          <p>
            Dance, music, fashion, poetry, or visual art – every form of expression is
            welcome. Take the stage, curate a display, or collaborate with friends to
            create something unforgettable.
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("")
st.markdown("---")

# SAVE THE DATE
st.markdown('<p class="section-title">Save the date</p>', unsafe_allow_html=True)
st.markdown(
    """
    <p class="info-text">
        <strong>Saturday, April 18, 2026</strong><br>
        University of Missouri–Kansas City<br>
        Open to all students, staff, families, and community members.
    </p>
    """,
    unsafe_allow_html=True,
)

st.image(bg_soft_1, use_container_width=True)

# CONTACT / SOCIAL
st.markdown(
    """
    <p class="info-text" style="margin-top: 1rem;">
        To ask questions, get involved, or propose a performance or booth:<br>
        Follow us on Instagram at <strong>@umkcisao</strong> or email
        <a href="mailto:umkcisap@umkc.edu">umkcisap@umkc.edu</a>.
    </p>
    """,
    unsafe_allow_html=True,
)

# Decorative footer strip
st.image(bg_soft_2, use_container_width=True)

st.markdown(
    """
    <div class="footer">
        &copy; 2026 International Student Ambassadors – UMKC
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("</div>", unsafe_allow_html=True)