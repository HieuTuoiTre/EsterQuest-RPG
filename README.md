# ⚔️ Ester Quest: Hiệp Sĩ Giả Kim & Đại Chiến Thủy Phân

[![Standard: GDPT 2018](https://img.shields.io/badge/Standard-GDPT%202018-blue.svg)](https://moet.gov.vn)
[![Tech: Pure HTML5/CSS3/Vanilla JS](https://img.shields.io/badge/Tech-Vanilla%20JS%20%7C%20CSS3%20%7C%20HTML5-orange.svg)](https://developer.mozilla.org)
[![Responsive: Mobile & Desktop](https://img.shields.io/badge/Responsive-Mobile%20%7C%20Tablet%20%7C%20Desktop-green.svg)](https://developer.mozilla.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-purple.svg)](./LICENSE)

**Ester Quest** là web game nhập vai chiến thuật theo lượt (Turn-based RPG) lồng ghép 100% kiến thức trọng tâm **Hóa học Lớp 12 - Chuyên đề Ester (Chuẩn GDPT 2018)**. Người chơi hóa thân thành Hiệp Sĩ Giả Kim, vượt qua 5 bài huấn luyện thực nghiệm tại Học Viện Đào Tạo, sở hữu bộ Grimoire 10 chiêu thức hóa học, xây dựng Tactical Skill Deck 4 ô và chinh phục Chiến dịch 8 Ải Đánh Quái khốc liệt chống lại Đại Ma Vương Thức Tỉnh 2 Giai Đoạn.

---

## 📜 Cốt Truyện Sử Thi (Epic Prologue Storyline)

> *"Từ thuở sơ khai của thế giới Giả Kim, Vương Quốc Ester ngự trị trong sự cân bằng hoàn mỹ của các liên kết hóa học. Dưới vòm trời lấp lánh tinh thể ester, muôn loài sống hòa thuận trong hương thơm thanh khiết của hoa cỏ, trái chín ngào ngạt và nguồn năng lượng trù phú từ tự nhiên.*
>
> *Thế nhưng, khi Vực Thẳm Hỗn Mang mở ra, Đại Ma Vương đã làm biến dị các liên kết C—O, giải phóng bầy ma vật tàn phá muôn nơi. Vương triều đứng trước bờ vực diệt vong.*
>
> *Lời sấm truyền ngàn năm báo trước: Chỉ có một Hiệp Sĩ thấu suốt mọi bí kíp danh pháp, quy luật nhiệt độ sôi và thuật thủy phân xà phòng hóa mới có thể cầm chắc thanh kiếm tri thức để dẹp tan ma vật, khôi phục lại vinh quang cho thế giới Giả Kim!"*

Game mở đầu bằng phân cảnh điện ảnh chữ chạy viễn tưởng, tinh thể hóa học lơ lửng không gian và âm thanh synth huyền bí. Người chơi có thể bấm **Tiếp Tục Bước Vào Thế Giới ➔** hoặc bấm **Bỏ Qua ⏩** để vào thẳng màn hình khởi tạo.

---

## 🎮 Hướng Dẫn Khởi Chạy Game (Quick Start)

Trò chơi được đóng gói hoàn toàn trong file duy nhất `index.html` (thuần Vanilla JavaScript, CSS3 Keyframe Animations và Web Audio API synth — không cần cài đặt Node.js hay server trung gian).

### Cách 1: Chơi trực tiếp trên máy tính / điện thoại (Offline)
1. Tải về hoặc clone repository:
   ```bash
   git clone https://github.com/hieu8/EsterQuest-RPG.git
   ```
2. Nhấp đúp trực tiếp vào file [`index.html`](./index.html) để mở trên mọi trình duyệt hiện đại (Chrome, Edge, Safari, Firefox, Cốc Cốc).
3. Hoạt động 100% mượt mà ngay cả khi ngắt kết nối Internet!

### Cách 2: Triển khai trực tuyến miễn phí (Deploy Online)
* **GitHub Pages:** Đẩy repository lên GitHub, vào *Settings ➔ Pages* chọn branch `main` và thư mục `/ (root)` để kích hoạt link chơi trực tiếp.
* **Netlify:** Kéo thả thư mục dự án vào [Netlify Drop](https://app.netlify.com/drop) để có ngay tên miền web chia sẻ cho học sinh.
* **Vercel:** Kết nối repo GitHub với Vercel để triển khai tự động.

---

## 🎓 Chương 1: Học Viện Đào Tạo Chiến Binh Ester (5 Bài Học & 4 Thí Nghiệm Ảo)

Trước khi ra tiền tuyến, hiệp sĩ bắt buộc phải tham gia khóa huấn luyện tại Học Viện Giả Kim (`#academyScreen`) với Stepper 5 bước trực quan và hệ thống phòng thí nghiệm mô phỏng động học:

```
[Bài 1: Khái Niệm] ➔ [Bài 2: Danh Pháp] ➔ [Bài 3: Nhiệt Độ Sôi] ➔ [Bài 4: Thủy Phân & Tráng Bạc] ➔ [Bài 5: Điều Chế & Ghép Nối]
```

### 1. Bài 1: Cấu Trúc & Bản Chất Phân Tử
* **Lý thuyết:** Khi thay nhóm $-OH$ ở nhóm carboxyl ($-COOH$) bằng nhóm $-OR'$ ta thu được ester ($RCOOR'$). Công thức no, đơn chức, mạch hở: $C_nH_{2n}O_2$ ($n \ge 2$).
* **Mô phỏng 2D:** Khung trực quan hóa phân tử động làm nổi bật cầu nối ester $-COO-$ nhấp nháy ánh sáng neon.
* **Mini-quiz:** Kiểm tra nhận diện nhóm chức để mở khóa bài học kế tiếp.

### 2. Bài 2: Danh Pháp Thần Bí (Naming Rules)
* **Quy tắc quốc tế:** $\text{Tên Ester} = \text{Tên gốc alcohol } R' + \text{Tên gốc acid } RCOO^- \text{ (đuôi -ate)}$.
* **Bảng tương tác:** Bấm chọn các gốc acid ($CH_3COO^-$, $HCOO^-$, $CH_2=CHCOO^-$) và alcohol ($C_2H_5-$, $CH_3-$, $CH_2=CH-$) để sinh công thức và tên gọi chuẩn (ethyl acetate, methyl formate, vinyl acetate...).

### 3. Bài 3: Tính Chất Vật Lý & Thí Nghiệm Ảo Nhiệt Độ Sôi (Boiling Lab)
* **Quy luật:** $\text{Acid} > \text{Alcohol} > \text{Ester} > \text{Hydrocarbon}$ (do acid tạo liên kết hydrogen dạng dimer bền vững, alcohol tạo liên kết H, ester không tạo liên kết H liên phân tử).
* **Tương tác Thí nghiệm ảo:**
  - Kệ 3 hóa chất: Ester ($CH_3COOC_2H_5$ - 77°C), Alcohol ($C_2H_5OH$ - 78.3°C), Acid ($CH_3COOH$ - 118°C).
  - Thanh trượt nhiệt độ kéo từ **20°C đến 150°C**.
  - Đèn cồn rực lửa, cột thủy ngân nhiệt kế dâng cao, bọt khí sôi ùng ục và khói bốc lên khi đạt đúng ngưỡng nhiệt độ sôi của từng chất.

### 4. Bài 4: Thuật Thủy Phân, Tách Lớp & Tráng Bạc (Hydrolysis & Silver Mirror Lab)
* **Thí nghiệm tách lớp động:**
  - Ống nghiệm ban đầu tách thành 2 lớp rõ rệt: lớp ester nhẹ nổi lên trên, lớp nước & xúc tác acid phía dưới.
  - Bấm nút **"Đun Nóng"**: Lớp ester co nhỏ dần do tham gia phản ứng thuận nghịch, hỗn hợp dung dịch dâng cao.
* **Thí nghiệm tráng bạc lấp lánh (Silver Mirror Test):**
  - Nhỏ thuốc thử $AgNO_3 / NH_3$ vào sản phẩm thủy phân của vinyl ester hoặc formate ester.
  - Thành ống nghiệm chuyển từ trong suốt sang màng bạc kim loại sáng loáng ($Ag\downarrow$).

### 5. Bài 5: Xưởng Điều Chế Ester & Mini-Game Ghép Nối Ứng Dụng (Synthesis Lab & Matching Quest)
* **Xưởng điều chế:** Chọn 1 Acid + 1 Alcohol + Xúc tác $H_2SO_4$ đặc, đun nóng để tạo màng ester thơm ngào ngạt tách lớp.
* **Mini-Game Ghép Nối Thẻ (Interactive Matching Quests):**
  - **Màn 1 - Mùi Hương Hoa Quả:**
    * *Isoamyl acetate* $\leftrightarrow$ Mùi chuối chín
    * *Ethyl butyrate / Ethyl propionate* $\leftrightarrow$ Mùi dứa chín
    * *Benzyl acetate* $\leftrightarrow$ Mùi hoa nhài thơm ngát
    * *Geranyl acetate* $\leftrightarrow$ Mùi hoa hồng
  - **Màn 2 - Ứng Dụng Đời Sống:**
    * *Methyl methacrylate* $\leftrightarrow$ Kính hữu cơ Plexiglas (kính máy bay, răng giả)
    * *Ethyl acetate / Butyl acetate* $\leftrightarrow$ Dung môi pha sơn, mực in, tách chiết dược liệu
    * *Triacylglycerol (chất béo)* $\leftrightarrow$ Sản xuất xà phòng, glycerol, thực phẩm
    * *Methyl salicylate / Aspirin* $\leftrightarrow$ Dược phẩm giảm đau, cao xoa bóp kháng viêm
* **Lễ tốt nghiệp Học Viện:** Phong danh hiệu *"🎖️ Hiệp Sĩ Ester Chính Thức"*, thưởng thêm 1 Bình Hồi Phục và lưu tiến độ vào `localStorage`.

---

## 🔮 Grimoire: Bảng 10 Kỹ Năng Hóa Học & Tactical Deck 4 Ô

Người chơi có thể bấm **⚔️ Trang Bị Kỹ Năng** để mở Grimoire và chọn 4 chiêu thức đem vào trận đấu (hỗ trợ phím tắt số **1, 2, 3, 4** trên bàn phím).

| ID | Biểu Tượng & Tên Kỹ Năng | Phân Loại | MP | Hiệu Quả Sát Thương | Hiệu Ứng RPG Chiến Thuật Đặc Biệt |
|:---:|:---|:---:|:---:|:---:|:---|
| **1** | 🗡️ **Đòn Acid Chấn Động** | Đơn | 0 | 35 ST | **Hồi MP:** Hồi ngay 10 MP nếu trả lời đúng |
| **2** | 🔥 **Hỏa Cầu Ester Hóa** | Đơn | 20 | 75 ST | **Nhiệt năng:** Công phá mạnh mẽ đơn mục tiêu |
| **3** | 🛡️ **Khiên Dung Môi Hữu Cơ** | Hỗ trợ | 15 | +35 HP | **Bảo hộ:** Tạo khiên chặn 100% đòn đánh kế tiếp của quái |
| **4** | ⚡ **Bão Xà Phòng Hóa** | Đơn | 35 | 150 ST | **Khống chế:** Thủy phân cực đại & Choáng quái 1 lượt |
| **5** | 🌸 **Độc Khí Ester Thơm** | Đơn | 18 | 40 ST | **Trúng độc (DoT):** Quái mất 15 HP/lượt trong 3 lượt liên tiếp |
| **6** | 🧪 **Chiết Tách Dung Môi** | Đơn | 12 | 45 ST | **Hút máu:** Tách chiết dung môi, hồi phục 25 HP cho người chơi |
| **7** | 🪞 **Gương Bạc Lóa Mắt** | Đơn | 22 | 65 ST | **Gây mù (Blind):** Ánh bạc chói lòa, đòn quái đánh trượt 70% |
| **8** | 💥 **Bộc Phá Oxi Hóa** | Đơn | Toàn bộ | $MP \times 3.5$ | **Mana Burst:** Đốt cháy toàn bộ MP để tung đòn dứt điểm chí mạng |
| **9** | 🌊 **Sóng Thủy Phân Toàn Diện** | **AOE** | 28 | 60 ST/quái | **Sát thương diện rộng:** Quét sạch TẤT CẢ quái vật trên sân |
| **10**| 🌪️ **Bão Nhiệt Phản Ứng** | **AOE** | 42 | 95 ST/quái | **AOE Cực Đại:** Quét sạch toàn bộ bầy quái & Giảm 25% công của chúng |

### 💡 Gợi Ý Phối Deck Chiến Thuật
* **Deck Cân Bằng Toàn Diện (Khuyên dùng):** `[1] Đòn Acid` + `[3] Khiên Dung Môi` + `[4] Bão Xà Phòng Hóa` + `[9] Sóng Thủy Phân AOE`.
* **Deck Đánh Nhanh Quét Bầy Quái (Ải 2 & Ải 5):** `[1] Đòn Acid` + `[6] Chiết Tách Dung Môi` + `[9] Sóng Thủy Phân` + `[10] Bão Nhiệt Phản Ứng`.
* **Deck Khắc Chế Nightmare Boss (Ải 8):** `[1] Đòn Acid` + `[3] Khiên Dung Môi` + `[7] Gương Bạc Lóa Mắt` + `[8] Bộc Phá Oxi Hóa`.

---

## 🗺️ Chiến Dịch 8 Ải Đánh Quái & Động Cơ Đa Mục Tiêu

Hệ thống chiến đấu hỗ trợ dàn **1 đến 3 quái vật đồng thời** trên sàn đấu với cơ chế ngắm bắn nhấp chuột (`click-to-target`), vòng hào quang neon chỉ thị mục tiêu và chuỗi quái vật phản công lần lượt cách nhau 400ms:

```
[Ải 1: Slime] ➔ [Ải 2: Bầy Slime (3 Quái)] ➔ [Ải 3: Sói Băng] ➔ [Ải 4: Thạch Quái]
      ➔ [Ải 5: Song Quái (2 Quái)] ➔ [Ải 6: Hỏa Long] ➔ [Ải 7: Chúa Tể Bóng Tối] ➔ [Ải 8: ĐẠI MA VƯƠNG (2 Phase)]
```

### Chi Tiết 8 Ải Thử Thách
1. **Ải 1: Rừng Ẩm Ướt** — 1 Quái: `Slime` (Lv.1, HP: 100). Khởi động tiền tuyến, làm quen cơ chế cast chiêu và trả lời câu hỏi.
2. **Ải 2: Đầm Lầy Bầy Nhầy (MÀN 3 QUÁI):** `Bầy Slime` (`Slime Xanh` HP 60, `Slime Đỏ` HP 70, `Slime Vàng` HP 80). *Sân tập lý tưởng cho các chiêu AOE!*
3. **Ải 3: Thung Lũng Băng** — 1 Quái: `Sói Băng` (Lv.2, HP: 160). Tốc độ cao, thử thách kiến thức về nhiệt độ sôi và độ tan.
4. **Ải 4: Hầm Ngục Thạch** — 1 Quái: `Thạch Quái` (Lv.3, HP: 220). Thủy phân bền vững, đòi hỏi combo sát thương dồn dập.
5. **Ải 5: Tháp Canh Đôi (MÀN 2 QUÁI TINH ANH):** `Song Quái` (`Chiến Binh Đao` HP 150, `Chiến Binh Khiên` HP 150). Phối hợp công thủ, cần ngắm bắn tập trung diệt từng con hoặc dùng bão nhiệt AOE.
6. **Ải 6: Tháp Địa Ngục** — 1 Quái: `Hỏa Long` (Lv.4, HP: 280). Lượng sát thương lớn, kiểm tra bài toán hiệu suất ester hóa và tính háo nước của $H_2SO_4$.
7. **Ải 7: Điện Thờ Hắc Ám** — 1 Boss: `Chúa Tể Bóng Tối` (Lv.5, HP: 360). Sát khí áp đảo, bài tập este của phenol phản ứng NaOH tỉ lệ 1:2.
8. **Ải 8: Vực Thẳm Hỗn Mang (👑 NIGHTMARE SUPER BOSS 2 GIAI ĐOẠN):**
   * **Phase 1: Đại Ma Vương (HP: 350, ATK: 45):** Được bảo hộ bởi *Khiên Hỗn Mang*, giảm 25% mọi sát thương nhận vào (`dmgReduction: 0.25`).
   * **Phase 2 Thức Tỉnh Cuồng Nộ: Đại Ma Vương Thức Tỉnh (HP: 500, ATK: 55):** Khi Phase 1 cạn máu, sấm sét chớp giật rực trời, âm thanh gầm thét vang dội. Boss hồi sinh với 500 HP và kích hoạt nội tại Cuồng Nộ: tăng 15% ATK mỗi 2 lượt đấu!
   * **Kho câu hỏi:** Chuyên dụng 38 câu hỏi Vận Dụng Cao chuẩn đề thi Tốt nghiệp THPT.

---

## 🎒 Trang Bị Trợ Giúp Trong Trận Đấu

* 🧪 **Bình Nước Cất:** Hồi ngay 45 HP mà không cần trả lời câu hỏi (phím tắt `H`).
* 💧 **Xúc Tác H2SO4 Đặc:** Mở gợi ý tư duy hóa học và loại bỏ 50% phương án sai (trợ giúp 50/50).
* 📖 **Sổ Tay Bí Kíp (Codex):** Mở bảng tra cứu tóm tắt toàn bộ lý thuyết và phản ứng ngay trong trận đánh.
* 📝 **Nhật Ký Đấu Trí (Review):** Xem lại toàn bộ câu trả lời đúng/sai kèm lời giải chi tiết sau trận đấu.

---

## 🏆 Bảng Xếp Hạng & Đồng Bộ Dữ Liệu Giáo Viên (Leaderboard)

* **Lưu trữ Offline (LocalStorage):** Tự động lưu tên học sinh, lớp, điểm số, tỉ lệ chính xác, số ải vượt qua và mốc thời gian thi đấu. Hỗ trợ lọc theo từng Lớp học.
* **Đồng bộ toàn trường (Online Google Sheets API):**
  - Mở file `index.html`, tìm biến:
    ```javascript
    const GOOGLE_SHEET_API = "";
    ```
  - Dán URL Google Apps Script Web App của giáo viên vào biến này. Khi học sinh hoàn thành trận đấu hoặc phá đảo 8 Ải, kết quả sẽ tự động gửi thẳng về Google Sheets của giáo viên để thống kê xếp hạng toàn khối!

---

## 📱 Thiết Kế Đáp Ứng Đa Thiết Bị (Responsive Design)

Game được tối ưu hóa giao diện hoàn hảo trên mọi kích thước màn hình:
* **Mobile siêu nhỏ (<= 360px & <= 380px):** Co giãn linh hoạt các ống nghiệm thí nghiệm ảo, thu nhỏ thanh máu bầy quái 3 con, giữ vững bố cục không bị tràn ngang (`overflow-x: hidden`).
* **Mobile tiêu chuẩn (<= 480px & <= 600px):** Nút bấm đảm bảo kích thước chạm tối thiểu chuẩn công thái học ($\ge 44\text{px} \times 44\text{px}$), lưới chọn chiêu thức tự động chuyển thành 2 cột hoặc 1 cột dễ thao tác.
* **Tablet (768px - 960px) & Desktop (1200px+):** Hiển thị sàn đấu rộng rãi, hiệu ứng đồ họa neon pixelated chân thực và trải nghiệm điện ảnh toàn màn hình.

---

## 🔬 Chuẩn Hóa Danh Pháp Hóa Học (GDPT 2018)

Dự án tuân thủ 100% quy chuẩn danh pháp IUPAC theo chương trình Giáo dục Phổ thông 2018 của Bộ Giáo dục và Đào tạo:
* Dùng **`ester`** (không dùng *este*).
* Dùng **`acid`** (không dùng *axit*).
* Dùng **`alcohol`** (không dùng *ancol*).
* Dùng **`glycerol`** (không dùng *glixerol*).

---

## 🧪 Hệ Thống Kiểm Thử Tự Động (Automated Test Suite)

Dự án đi kèm bộ 5 script kiểm thử tự động toàn diện trong thư mục `tests/`:

```bash
# Kiểm tra Màn mở đầu Prologue & SFX
python tests/verify_task1.py

# Kiểm tra Chương 1 Học Viện, 4 Thí Nghiệm Ảo & Mini-Games
python tests/verify_task2.py

# Kiểm tra Grimoire 10 Kỹ Năng, 4-Deck Loadout & Động cơ Đa Quái AOE
python tests/verify_task3_4.py

# Kiểm tra Chiến dịch 8 Ải & Super Boss 2 Phase
python tests/verify_task5.py

# Kiểm tra Toàn Diện Toàn Bộ Luồng Game, Cú Pháp JS & Responsive
python tests/verify_full_flow.py
```

---

## 📄 Bản Quyền & Giấy Phép

Phát triển bởi đội ngũ **EsterQuest Team** phục vụ mục đích đổi mới phương pháp giảng dạy Hóa học theo định hướng Gamification & Chuyển đổi số giáo dục. Phát hành theo giấy phép [MIT License](./LICENSE).
