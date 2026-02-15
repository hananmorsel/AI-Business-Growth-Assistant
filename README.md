
# AI Business Growth Assistant
A Streamlit app using Gemini REST API.

![Image](https://s3-alpha.figma.com/hub/file/2219764181466924094/fe67a5c0-dd57-4bf7-b40a-bce7ef34ecfb-cover.png)

![Image](https://cdn.venngage.com/features/img/Marketing-Plan-Generator-Brand-Kit-3.webp)

![Image](https://theme.bitrixinfotech.com/assets/images/screenshot/screenshot1695197106_3.png)

# **AI Business Growth Assistant**

**AI Business Growth Assistant** is an intelligent marketing tool powered by **Google Gemini 1.5 Flash** (REST API).
It helps businesses instantly generate:

✅ Customer personas
✅ High-impact marketing messages
✅ Platform-specific social media ads
✅ AI-generated ad images
✅ Creative styling options
✅ Ready-to-publish content for Instagram, TikTok, and Facebook

Built using **Python**, **Streamlit**, and **Gemini REST**, this project is perfect for your AI engineering portfolio on GitHub.

---

## 🌟 **Features**

### 🔹 1. **AI Persona Builder**

Generates realistic customer personas based on:

* Product
* Target audience
* Market segment

### 🔹 2. **AI Message Generator**

Creates:

* Platform-specific marketing copy
* Tone-controlled messaging (friendly, bold, professional)
* Short-form social media captions

### 🔹 3. **AI Image Generator**

Produces ad-ready images using:

* Realistic photo style
* Minimalistic graphic
* Bold social media style
* Custom user style

### 🔹 4. **Streamlit Dashboard**

Modern UI with:

* Sections for persona, messaging, images
* Live preview
* Download options

### 🔹 5. **Gemini REST API (No SDK!)**

✔ No `google-generativeai` package
✔ No protobuf conflicts
✔ Works on any machine

---

## 🛠️ **Tech Stack**

* **Python 3.10+**
* **Streamlit**
* **Requests (REST client)**
* **Google Gemini 1.5 Flash**
* **dotenv** (for API keys)

---

# 🚀 **Live Demo (Screenshot Preview)**

![Image](https://images.prismic.io/turing/65a53cdf7a5e8b1120d5887f_image1_11zon_c0821d08b2.webp?auto=format%2Ccompress)

![Image](https://media.licdn.com/dms/image/v2/D4D12AQEJRiFI_A01tQ/article-cover_image-shrink_720_1280/B4DZaB7N4DG8AM-/0/1745936507285?e=2147483647\&t=SKwvRhREFleIiwcLqwth3czDQgJ-ZiEvfd3ZRWOreEQ\&v=beta)

![Image](https://substackcdn.com/image/fetch/%24s_%215lE4%21%2Cw_1456%2Cc_limit%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb5f7afed-a408-4d2f-a6fb-fe5407dc34c4_2190x1710.png)

---

# 📂 **Project Structure**

```
AI-Business-Growth-Assistant/
│
├── app/
│   ├── dashboard.py
│   ├── persona_analyzer.py
│   ├── message_generator.py
│   ├── image_generator.py
│
├── utils/
│   ├── gemini_client.py
│
├── assets/
│   ├── banner.png
│
├── .env.example
├── requirements.txt
├── README.md
```

---

# 🔧 **Installation**

### 1️⃣ Clone the repository

```
git clone https://github.com/YOURNAME/AI-Business-Growth-Assistant.git
cd AI-Business-Growth-Assistant
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Add your Gemini API Key

1. Create a `.env` file
2. Add:

```
GEMINI_API_KEY=your_key_here
```

### 4️⃣ Start the app

```
streamlit run app/dashboard.py
```

---

# 🧠 **How It Works**

## 1. Persona Generation

The app uses a structured prompt:

```
Create a marketing persona for PRODUCT targeting AUDIENCE.
Include motivations, behaviors, and interests.
```

## 2. Marketing Message

```
Create a TONE marketing message for PRODUCT targeting AUDIENCE on PLATFORM.
```

## 3. Image Generation

```
Generate a marketing image for PRODUCT, audience AUDIENCE, style STYLE.
```

Images are returned as base64 and displayed automatically.

---

# 📸 **Image Generation Styles**

![Image](https://mir-s3-cdn-cf.behance.net/project_modules/hd/8ff963104656881.5f82e8c1e47c8.jpg)

![Image](https://cdn.dribbble.com/userupload/26198069/file/original-c4510e81623ee89d46e67ae93a94ae8b.png?resize=400x0)

![Image](https://media.licdn.com/dms/image/v2/D5612AQGxUPRToyfWzQ/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1700115151076?e=2147483647\&t=L0LJ3XK-um74QWL6g52ToKYu7XtVDGuN5d0o3dJ274A\&v=beta)

![Image](https://v.etsystatic.com/video/upload/q_auto/Digital_product_mockup_for_online_marketing_-_branding_mockups_by_studio_schenk_o6jqcs.jpg)

You can choose:

✔ Realistic
✔ Minimalistic
✔ Bold
✔ Custom creative style

---

# 🧪 **Testing**

Run persona generator:

```
python - <<EOF
from app.persona_analyzer import build_persona
print(build_persona("Organic Soap","Young mothers"))
EOF
```

Run message generator:

```
python - <<EOF
from app.message_generator import generate_message
print(generate_message("Organic Soap","Young mothers","Friendly","Instagram"))
EOF
```

---

# 🤝 **Contributing**

Contributions are welcome!
Feel free to open issues or submit PRs on GitHub.

---

# 📜 **License**

MIT License.

---

# 🌟 **Support & Contact**


Just tell me!
