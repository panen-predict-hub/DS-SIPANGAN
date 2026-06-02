import os
import streamlit as st
import pandas as pd
import plotly.express as px


# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="SIPangan Analytics",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# CSS
# =========================================================
st.markdown("""
<style>
.block-container {
    max-width: 1220px;
    padding-top: 1.3rem;
    padding-bottom: 1.5rem;
}

h1 {
    font-size: 1.85rem !important;
    font-weight: 700 !important;
    color: #1f2937;
    margin-bottom: 0.15rem !important;
}

h2, h3 {
    color: #1f2937;
    font-weight: 650 !important;
}

p, label, span {
    color: #374151;
}

[data-testid="stMetric"] {
    background-color: #ffffff;
    border: 1px solid #e5e7eb;
    padding: 0.85rem 1rem;
    border-radius: 14px;
}

[data-testid="stMetricLabel"] {
    font-size: 0.78rem !important;
    color: #6b7280 !important;
}

[data-testid="stMetricValue"] {
    font-size: 1.18rem !important;
    font-weight: 700 !important;
    color: #111827 !important;
}

.stTabs [data-baseweb="tab-list"] {
    gap: 0.5rem;
    border-bottom: 1px solid #e5e7eb;
}

.stTabs [data-baseweb="tab"] {
    height: 40px;
    padding-left: 0.9rem;
    padding-right: 0.9rem;
    font-weight: 600;
}

.stTabs [aria-selected="true"] {
    color: #2563eb !important;
}

div[data-testid="stVerticalBlock"] {
    gap: 0.65rem;
}

.small-caption {
    font-size: 0.92rem;
    color: #6b7280;
    margin-bottom: 0.7rem;
}

.insight-box {
    background-color: #f8fafc;
    border: 1px solid #e5e7eb;
    border-left: 4px solid #2563eb;
    padding: 0.85rem 1rem;
    border-radius: 12px;
    font-size: 0.92rem;
    color: #1f2937;
    line-height: 1.55;
}

hr {
    margin-top: 0.3rem;
    margin-bottom: 0.7rem;
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# LOAD DATA
# =========================================================
@st.cache_data
def load_data():
    BASE_DIR = os.path.dirname(__file__)
    DATA_PATH = os.path.join(BASE_DIR, "data", "data_final.csv")

    if not os.path.exists(DATA_PATH):
        st.error(f"File data tidak ditemukan: {DATA_PATH}")
        st.stop()

    data = pd.read_csv(DATA_PATH)

    data["periode_update"] = pd.to_datetime(data["periode_update"])
    data["tahun"] = data["periode_update"].dt.year
    data["bulan"] = data["periode_update"].dt.month
    data["tahun_bulan"] = data["periode_update"].dt.to_period("M").astype(str)

    if "series_id" not in data.columns:
        data["series_id"] = (
            data["nama_kabupaten_kota"].astype(str)
            + " | "
            + data["kategori"].astype(str)
        )

    return data


data = load_data()

daftar_komoditas = sorted(data["kategori"].unique())
daftar_wilayah = sorted(data["nama_kabupaten_kota"].unique())
tahun_min = int(data["tahun"].min())
tahun_max = int(data["tahun"].max())

plotly_config = {
    "displayModeBar": False,
    "responsive": True
}

COLORS = ["#2563eb", "#60a5fa", "#ef4444", "#0f766e", "#f97316"]


# =========================================================
# HELPER
# =========================================================
def rupiah(nilai):
    if pd.isna(nilai):
        return "Rp0"
    return f"Rp{int(round(nilai, 0)):,}".replace(",", ".")


def filter_tahun(df, tahun_range):
    return df[df["tahun"].between(tahun_range[0], tahun_range[1])].copy()


def clean_layout(fig, height=335, legend=True):
    fig.update_layout(
        template="plotly_white",
        height=height,
        margin=dict(l=25, r=25, t=50, b=60),
        font=dict(size=12, color="#374151"),
        title_font=dict(size=16, color="#1f2937"),
        plot_bgcolor="white",
        paper_bgcolor="white",
        legend_title_text=""
    )

    if legend:
        fig.update_layout(
            legend=dict(
                orientation="h",
                yanchor="top",
                y=-0.18,
                xanchor="center",
                x=0.5
            )
        )
    else:
        fig.update_layout(showlegend=False)

    fig.update_xaxes(showgrid=False, zeroline=False)
    fig.update_yaxes(gridcolor="#e5e7eb", zeroline=False)
    return fig


def make_line_chart(df, x, y, title, color=None, height=350):
    fig = px.line(
        df,
        x=x,
        y=y,
        color=color,
        markers=True,
        title=title,
        color_discrete_sequence=COLORS
    )

    fig.update_traces(line=dict(width=2.6), marker=dict(size=5))
    fig = clean_layout(fig, height=height, legend=color is not None)
    fig.update_xaxes(title="")
    fig.update_yaxes(title="Harga")

    return fig


def make_bar_chart(df, x, y, title, color="#2563eb", height=360):
    fig = px.bar(
        df,
        x=x,
        y=y,
        orientation="h",
        text=x,
        title=title
    )

    fig.update_traces(
        marker_color=color,
        texttemplate="%{text:,.0f}",
        textposition="outside",
        cliponaxis=False
    )

    fig = clean_layout(fig, height=height, legend=False)
    fig.update_layout(margin=dict(l=25, r=110, t=50, b=30))
    fig.update_xaxes(title="")
    fig.update_yaxes(title="", autorange="reversed")

    return fig


def make_scatter_chart(df, title):
    fig = px.scatter(
        df,
        x="rata_rata_harga",
        y="fluktuasi_harga",
        size="fluktuasi_harga",
        text="kategori",
        hover_name="kategori",
        hover_data={
            "rata_rata_harga": ":,.0f",
            "fluktuasi_harga": ":,.0f"
        },
        title=title,
        color_discrete_sequence=["#2563eb"]
    )

    fig.update_traces(
        textposition="top center",
        textfont=dict(size=11),
        marker=dict(opacity=0.82),
        cliponaxis=False
    )

    fig = clean_layout(fig, height=360, legend=False)
    fig.update_layout(margin=dict(l=35, r=45, t=55, b=55))

    x_min = df["rata_rata_harga"].min()
    x_max = df["rata_rata_harga"].max()
    y_min = df["fluktuasi_harga"].min()
    y_max = df["fluktuasi_harga"].max()

    x_pad = (x_max - x_min) * 0.18 if x_max != x_min else x_max * 0.1
    y_pad = (y_max - y_min) * 0.22 if y_max != y_min else y_max * 0.1

    fig.update_xaxes(
        title="Rata-rata Harga",
        range=[x_min - x_pad, x_max + x_pad]
    )
    fig.update_yaxes(
        title="Fluktuasi Harga",
        range=[max(0, y_min - y_pad), y_max + y_pad]
    )

    return fig


# =========================================================
# HEADER
# =========================================================
st.title("SIPangan Analytics")
st.markdown(
    '<div class="small-caption">Analisis interaktif harga pangan Jawa Timur untuk membaca tren komoditas, membandingkan wilayah, dan memperkirakan arah harga.</div>',
    unsafe_allow_html=True
)


# =========================================================
# TABS
# =========================================================
tab_overview, tab_wilayah, tab_tren, tab_data = st.tabs([
    "Overview",
    "Perbandingan Wilayah",
    "Tren & Estimasi",
    "Data"
])


# =========================================================
# TAB 1: OVERVIEW
# =========================================================
with tab_overview:
    st.subheader("Overview Harga Pangan")

    tahun_overview = st.slider(
        "Rentang Tahun",
        min_value=tahun_min,
        max_value=tahun_max,
        value=(tahun_min, tahun_max),
        key="tahun_overview"
    )

    overview_data = filter_tahun(data, tahun_overview)

    periode_awal = overview_data["tahun_bulan"].min()
    periode_akhir = overview_data["tahun_bulan"].max()

    k1, k2, k3, k4, k5 = st.columns(5)

    k1.metric("Jumlah Data", f"{len(overview_data):,}")
    k2.metric("Wilayah", overview_data["nama_kabupaten_kota"].nunique())
    k3.metric("Komoditas", overview_data["kategori"].nunique())
    k4.metric("Rata-rata Harga", rupiah(overview_data["jumlah"].mean()))
    k5.metric("Periode", f"{periode_awal} - {periode_akhir}")

    ringkasan_komoditas = (
        overview_data
        .groupby("kategori", as_index=False)
        .agg(
            rata_rata_harga=("jumlah", "mean"),
            fluktuasi_harga=("jumlah", "std")
        )
    )

    tren_semua = (
        overview_data
        .groupby(["periode_update", "kategori"], as_index=False)["jumlah"]
        .mean()
        .sort_values("periode_update")
    )

    tren_semua["rata_rata_3_bulan"] = (
        tren_semua
        .groupby("kategori")["jumlah"]
        .transform(lambda x: x.rolling(window=3, min_periods=1).mean())
    )

    c1, c2 = st.columns(2)

    with c1:
        fig_prioritas = make_scatter_chart(
            ringkasan_komoditas,
            title="Prioritas Pemantauan Komoditas"
        )
        st.plotly_chart(fig_prioritas, use_container_width=True, config=plotly_config)

    with c2:
        fig_tren = make_line_chart(
            tren_semua,
            x="periode_update",
            y="rata_rata_3_bulan",
            color="kategori",
            title="Tren Rata-rata Harga Semua Komoditas",
            height=360
        )
        st.plotly_chart(fig_tren, use_container_width=True, config=plotly_config)

    komoditas_termahal = ringkasan_komoditas.sort_values(
        "rata_rata_harga",
        ascending=False
    ).iloc[0]

    komoditas_fluktuatif = ringkasan_komoditas.sort_values(
        "fluktuasi_harga",
        ascending=False
    ).iloc[0]

    st.markdown(
        f"""
        <div class="insight-box">
        <b>Ringkasan:</b> Pada periode {tahun_overview[0]}–{tahun_overview[1]},
        komoditas dengan rata-rata harga tertinggi adalah <b>{komoditas_termahal['kategori']}</b>
        sekitar <b>{rupiah(komoditas_termahal['rata_rata_harga'])}</b>.
        Komoditas dengan fluktuasi harga tertinggi adalah <b>{komoditas_fluktuatif['kategori']}</b>
        dengan deviasi sekitar <b>{rupiah(komoditas_fluktuatif['fluktuasi_harga'])}</b>.
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# TAB 2: PERBANDINGAN WILAYAH
# =========================================================
with tab_wilayah:
    st.subheader("Perbandingan Wilayah")
    st.caption("Bagian ini membandingkan seluruh wilayah sehingga tidak membutuhkan filter wilayah tertentu.")

    f1, f2, f3 = st.columns([1.05, 1.05, 0.9])

    with f1:
        komoditas_wilayah = st.selectbox(
            "Komoditas",
            daftar_komoditas,
            index=daftar_komoditas.index("Beras Medium") if "Beras Medium" in daftar_komoditas else 0,
            key="komoditas_wilayah"
        )

    with f2:
        tahun_wilayah = st.slider(
            "Rentang Tahun",
            min_value=tahun_min,
            max_value=tahun_max,
            value=(tahun_min, tahun_max),
            key="tahun_wilayah"
        )

    with f3:
        top_n = st.slider(
            "Jumlah Wilayah",
            min_value=5,
            max_value=15,
            value=10,
            key="top_n"
        )

    data_wilayah = data[
        (data["kategori"] == komoditas_wilayah)
        & (data["tahun"].between(tahun_wilayah[0], tahun_wilayah[1]))
    ].copy()

    rata_wilayah = (
        data_wilayah
        .groupby("nama_kabupaten_kota", as_index=False)["jumlah"]
        .mean()
        .sort_values("jumlah", ascending=False)
        .head(top_n)
        .sort_values("jumlah", ascending=True)
    )

    fluktuasi_wilayah = (
        data_wilayah
        .groupby("nama_kabupaten_kota", as_index=False)
        .agg(
            harga_minimum=("jumlah", "min"),
            harga_maksimum=("jumlah", "max")
        )
    )

    fluktuasi_wilayah["rentang_harga"] = (
        fluktuasi_wilayah["harga_maksimum"] - fluktuasi_wilayah["harga_minimum"]
    )

    fluktuasi_wilayah = (
        fluktuasi_wilayah
        .sort_values("rentang_harga", ascending=False)
        .head(top_n)
        .sort_values("rentang_harga", ascending=True)
    )

    c1, c2 = st.columns(2)

    with c1:
        fig_rata_wilayah = make_bar_chart(
            rata_wilayah,
            x="jumlah",
            y="nama_kabupaten_kota",
            title="Wilayah dengan Harga Tertinggi",
            color="#2563eb",
            height=370
        )
        st.plotly_chart(fig_rata_wilayah, use_container_width=True, config=plotly_config)

    with c2:
        fig_fluktuasi_wilayah = make_bar_chart(
            fluktuasi_wilayah,
            x="rentang_harga",
            y="nama_kabupaten_kota",
            title="Wilayah dengan Fluktuasi Tertinggi",
            color="#0f766e",
            height=370
        )
        st.plotly_chart(fig_fluktuasi_wilayah, use_container_width=True, config=plotly_config)

    if not rata_wilayah.empty and not fluktuasi_wilayah.empty:
        wilayah_tertinggi = rata_wilayah.sort_values("jumlah", ascending=False).iloc[0]
        wilayah_fluktuatif = fluktuasi_wilayah.sort_values("rentang_harga", ascending=False).iloc[0]

        st.markdown(
            f"""
            <div class="insight-box">
            <b>Ringkasan:</b> Untuk komoditas <b>{komoditas_wilayah}</b> pada periode {tahun_wilayah[0]}–{tahun_wilayah[1]},
            wilayah dengan rata-rata harga tertinggi adalah <b>{wilayah_tertinggi['nama_kabupaten_kota']}</b>
            sekitar <b>{rupiah(wilayah_tertinggi['jumlah'])}</b>. Wilayah dengan fluktuasi tertinggi adalah
            <b>{wilayah_fluktuatif['nama_kabupaten_kota']}</b> dengan rentang harga sekitar
            <b>{rupiah(wilayah_fluktuatif['rentang_harga'])}</b>.
            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# TAB 3: TREN & ESTIMASI
# =========================================================
with tab_tren:
    st.subheader("Tren & Estimasi Harga")

    f1, f2, f3 = st.columns([1.05, 1.05, 1.1])

    with f1:
        komoditas_tren = st.selectbox(
            "Komoditas",
            daftar_komoditas,
            index=daftar_komoditas.index("Beras Medium") if "Beras Medium" in daftar_komoditas else 0,
            key="komoditas_tren"
        )

    with f2:
        wilayah_tren = st.selectbox(
            "Wilayah",
            daftar_wilayah,
            key="wilayah_tren"
        )

    with f3:
        tahun_tren = st.slider(
            "Rentang Tahun",
            min_value=tahun_min,
            max_value=tahun_max,
            value=(tahun_min, tahun_max),
            key="tahun_tren"
        )

    data_tren = data[
        (data["kategori"] == komoditas_tren)
        & (data["nama_kabupaten_kota"] == wilayah_tren)
        & (data["tahun"].between(tahun_tren[0], tahun_tren[1]))
    ].copy().sort_values("periode_update")

    if data_tren.empty:
        st.warning("Data tidak tersedia untuk filter yang dipilih.")
    else:
        harga_terakhir = data_tren["jumlah"].iloc[-1]
        estimasi = data_tren["jumlah"].tail(3).mean()
        selisih = estimasi - harga_terakhir

        if selisih > 0:
            arah = "Naik"
        elif selisih < 0:
            arah = "Turun"
        else:
            arah = "Stabil"

        c1, c2 = st.columns([2.2, 1])

        with c1:
            fig_tren = make_line_chart(
                data_tren,
                x="periode_update",
                y="jumlah",
                color=None,
                title=f"Tren Harga {komoditas_tren} di {wilayah_tren}",
                height=380
            )
            fig_tren.update_traces(line=dict(color="#2563eb", width=2.8))
            st.plotly_chart(fig_tren, use_container_width=True, config=plotly_config)

        with c2:
            st.metric("Harga Terakhir", rupiah(harga_terakhir))
            st.metric("Estimasi Bulan Berikutnya", rupiah(estimasi), delta=rupiah(selisih))
            st.metric("Arah Harga", arah)

        st.markdown(
            f"""
            <div class="insight-box">
            <b>Ringkasan:</b> Pada periode {tahun_tren[0]}–{tahun_tren[1]}, harga <b>{komoditas_tren}</b>
            di <b>{wilayah_tren}</b> berubah dari sekitar <b>{rupiah(data_tren['jumlah'].iloc[0])}</b>
            menjadi <b>{rupiah(data_tren['jumlah'].iloc[-1])}</b>. Estimasi bulan berikutnya sekitar
            <b>{rupiah(estimasi)}</b> dengan arah harga <b>{arah.lower()}</b>.
            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# TAB 4: DATA
# =========================================================
with tab_data:
    st.subheader("Data Hasil Filter")

    f1, f2, f3 = st.columns([1.05, 1.05, 1.1])

    with f1:
        komoditas_data = st.selectbox(
            "Komoditas",
            daftar_komoditas,
            key="komoditas_data"
        )

    with f2:
        wilayah_data = st.selectbox(
            "Wilayah",
            daftar_wilayah,
            key="wilayah_data"
        )

    with f3:
        tahun_data = st.slider(
            "Rentang Tahun",
            min_value=tahun_min,
            max_value=tahun_max,
            value=(tahun_min, tahun_max),
            key="tahun_data"
        )

    data_tabel = data[
        (data["kategori"] == komoditas_data)
        & (data["nama_kabupaten_kota"] == wilayah_data)
        & (data["tahun"].between(tahun_data[0], tahun_data[1]))
    ].copy().sort_values("periode_update", ascending=False)

    kolom_tampil = [
        "series_id",
        "nama_kabupaten_kota",
        "periode_update",
        "kategori",
        "jumlah",
        "tahun",
        "tahun_bulan"
    ]

    kolom_tampil = [kolom for kolom in kolom_tampil if kolom in data_tabel.columns]

    st.dataframe(
        data_tabel[kolom_tampil],
        use_container_width=True,
        hide_index=True,
        height=390
    )

    csv = data_tabel[kolom_tampil].to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download Data Hasil Filter",
        data=csv,
        file_name="data_hasil_filter_SIPangan.csv",
        mime="text/csv"
    )
