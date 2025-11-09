import streamlit as st
from PIL import Image, ImageChops

# ============================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================
st.set_page_config(
    page_title="AI Universal Studio PRO++ — Sistema Multimodal",
    layout="wide"
)

# ============================================================
# ESTILO VISUAL — MINIMALISTA E COLORIDO
# ============================================================
st.markdown("""
<style>
body {
    background-color: #f8f9fb;
    color: #222;
    font-family: 'Poppins', sans-serif;
}
header, [data-testid="stHeader"] {
    display: none;
}
h1, h2, h3, h4 {
    font-weight: 600;
}
a {
    color: #FF5B6A !important;
    text-decoration: none;
    font-weight: 500;
}
a:hover {
    text-decoration: underline;
}
img {
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    margin-top: 0.8rem;
    margin-bottom: 1.2rem;
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# FUNÇÃO AUXILIAR — REMOVER BORDAS BRANCAS
# ============================================================
def crop_white_borders(img_path):
    try:
        img = Image.open(img_path)
        bg = Image.new(img.mode, img.size, img.getpixel((0, 0)))
        diff = ImageChops.difference(img, bg)
        bbox = diff.getbbox()
        if bbox:
            img = img.crop(bbox)
        return img
    except FileNotFoundError:
        st.warning(f"Imagem não encontrada: {img_path}")
        return None


# ============================================================
# CABEÇALHO
# ============================================================
st.markdown("<h1 style='text-align:center; color:#4B7BE5;'>AI Universal Studio PRO++</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center; color:#FF5B6A;'>Sistema Multimodal de Aprendizado com Texto e Imagem</h4>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#666;'>Um estúdio de inteligência artificial que aprende com múltiplas modalidades — texto, imagem e som — para gerar previsões inteligentes e explicáveis.</p>", unsafe_allow_html=True)

# ============================================================
# SOBRE O PROJETO
# ============================================================
st.markdown("## <span style='color:#6C63FF;'>O que é o AI Universal Studio?</span>", unsafe_allow_html=True)
st.markdown("""
O **AI Universal Studio PRO++** é um **sistema multimodal educacional** criado para demonstrar como  
**modelos de IA modernos** podem aprender com diferentes tipos de dados (texto, imagem e áudio) simultaneamente.

Este aplicativo simula o funcionamento de um **modelo híbrido de aprendizado**,  
onde o usuário pode criar uma base personalizada e ensinar a IA a reconhecer padrões —  
desde cores e emoções até níveis de risco e contexto ambiental.

O projeto tem como objetivo **educar e inspirar** estudantes e desenvolvedores sobre o uso prático de:
- **Embeddings semânticos** (Sentence Transformers)  
- **Modelos de visão** (BLIP / Transformers)  
- **Classificadores inteligentes** (Random Forest ou Logistic Regression)
""")

# ============================================================
# DEMONSTRAÇÃO DAS ETAPAS
# ============================================================
st.markdown("## <span style='color:#6C63FF;'>Etapas de Funcionamento</span>", unsafe_allow_html=True)
st.markdown("""
O sistema segue três etapas principais:
1. **Base de Aprendizado** — O usuário fornece exemplos de texto e categorias.  
2. **Treinamento da IA** — O modelo aprende a distinguir padrões semânticos.  
3. **Previsão Multimodal** — A IA analisa novas imagens e textos para prever resultados.
""")

col1, col2, col3 = st.columns(3)
train_img = crop_white_borders("ai_universal_train.png")
model_img = crop_white_borders("ai_universal_model.png")
predict_img = crop_white_borders("ai_universal_predict.png")

with col1:
    if train_img:
        st.image(train_img, caption="Etapa 1 — Base de Treinamento", use_column_width=True)
with col2:
    if model_img:
        st.image(model_img, caption="Etapa 2 — Treinar Modelo", use_column_width=True)
with col3:
    if predict_img:
        st.image(predict_img, caption="Etapa 3 — Fazer Previsão", use_column_width=True)

# ============================================================
# APLICAÇÕES PRÁTICAS
# ============================================================
st.markdown("## <span style='color:#FF5B6A;'>Aplicações Reais</span>", unsafe_allow_html=True)
st.markdown("""
O **AI Universal Studio** pode ser aplicado em diferentes contextos:
- **Educação em IA** — demonstração de modelos multimodais em aulas e workshops.  
- **Análise de imagens e texto** — interpretação conjunta de dados visuais e linguísticos.  
- **Prototipagem de modelos inteligentes** — experimentação com embeddings e classificadores.  
- **Exploração criativa** — unir descrição visual e semântica para construir modelos interpretáveis.
""")

# ============================================================
# EXEMPLO DE RESULTADO
# ============================================================
st.markdown("## <span style='color:#2ECC71;'>Exemplo de Previsão</span>", unsafe_allow_html=True)
st.markdown("""
**Entrada da IA:**  
> “Uma casa verde com uma planta crescendo. O ambiente está calmo e equilibrado.”

**Resultado da previsão:**  
*Baixo* — situação tranquila, estável e controlada.  

Agora, se o sistema receber uma imagem de **fogo ou caos** e a frase  
> “O sistema apresentou falhas críticas e o alerta vermelho foi acionado.”  

O resultado esperado será:  
**Alto** — situação crítica e de risco elevado.
""")

# ============================================================
# CONTATO / PORTFÓLIO
# ============================================================
st.markdown("## <span style='color:#4B7BE5;'>Sobre o Desenvolvedor</span>", unsafe_allow_html=True)
st.markdown("""
**Autor:** *Claudio Hideki Yoshida*  
**Função:** *Desenvolvedor de Machine Learning e Criador de Soluções em IA Aplicada*  

**Contato:**  
📧 [claudio.y@hotmail.com](mailto:claudio.y@hotmail.com)  
📱 [WhatsApp: (11) 98636-4794](https://wa.me/5511986364794)

Apaixonado por **IA, Educação e Prototipagem Rápida**, cria projetos que unem  
**tecnologia, design e aprendizado** para tornar a inteligência artificial mais **acessível e visual**.
""")

st.caption("© 2025 AI Universal Studio PRO++ — Sistema Multimodal Educacional | Desenvolvido por Claudio Hideki Yoshida 💡")
