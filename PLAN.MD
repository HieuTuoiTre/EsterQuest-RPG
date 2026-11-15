# Kế Hoạch Triển Khai: Mở Đầu Hoành Tráng, Chương 1 Học Viện Đào Tạo & Thí Nghiệm Ảo, Chiến Dịch 8 Ải RPG (PLAN.MD)

> **Dành cho kỹ sư / Agent triển khai:** BẮT BUỘC SỬ DỤNG SUB-SKILL: `superpowers:subagent-driven-development` (khuyên dùng) hoặc `superpowers:executing-plans` để thực thi từng nhiệm vụ theo thứ tự. Các bước sử dụng cú pháp checkbox (`- [ ]`) để theo dõi tiến độ.

**Mục tiêu (Goal):** 
1. Xây dựng màn mở đầu cốt truyện điện ảnh hoành tráng (Epic Prologue Intro) ngay khi bấm vào trang web.
2. Thiết kế **Chương 1: Học Viện Đào Tạo Chiến Binh Ester** với 5 bài học tương ứng 5 chuyên đề Bí Kíp Ester, tích hợp hệ thống **Phòng Thí Nghiệm Ảo Giả Kim (Interactive Virtual Chemistry Lab)** với 4 mô phỏng tương tác sinh động và mini-game ghép nối mùi hương / ứng dụng thực tế.
3. Mở rộng kho kỹ năng chiến đấu (bao gồm các chiêu AOE diện rộng và chiêu đơn mục tiêu độc đáo) cùng bảng chọn 4 chiêu (Skill Deck).
4. Mở rộng chiến dịch lên **8 Ải Đánh Quái** (với 2 ải nhiều quái) và **Ải 8 Nightmare Super Boss** 2 Giai đoạn độ khó cực cao.

**Kiến trúc (Architecture):**
- **Luồng phân cảnh mới:** `Prologue Cinematic Screen` ➔ `Menu Nhập Tên & Lớp` ➔ `Chương 1: Học Viện Đào Tạo Hiệp Sĩ (5 Bài Học + 4 Thí Nghiệm Ảo + Mini-game Ghép Nối)` ➔ `Trang Bị Kỹ Năng (Deck Loadout)` ➔ `Chiến Trường 8 Ải`.
- **Động cơ thí nghiệm ảo (Virtual Lab Simulation Engine):** Mô phỏng ống nghiệm với cơ chế tách lớp động, tăng/giảm thể tích các pha lỏng, hiệu ứng đun sôi / bốc hơi theo thanh trượt nhiệt độ, phản ứng tráng gương bạc $Ag$, và ghép nối liên kết phân tử $RCO- + -OR'$.
- **Động cơ học tập tương tác (Academy Learning Engine):** Thẻ lý thuyết súc tích, trực quan, mini-game ghép thẻ (match pairs), kiểm tra nhanh mở khóa bài học tiếp theo.
- **Động cơ chiến đấu đa mục tiêu (Multi-Enemy & AOE Engine):** Hỗ trợ dàn 1-3 quái vật trên sàn đấu, cơ chế ngắm bắn click-to-target và sát thương toàn sân.
- **Trùm cuối 2 Phase biến dị:** Tự động hồi sinh, đổi sprite/tên và kích hoạt cuồng nộ ở Phase 2.

**Công nghệ (Tech Stack):** Pure Vanilla JavaScript (ES6+), HTML5, CSS3 (Keyframes Animations, Flexbox/Grid, Pixelated Rendering, CSS Gradients & Clip-path), Web Audio API Synthesizers.

---

## Ràng Buộc Toàn Cục (Global Constraints)

1. **Chuẩn hóa danh pháp tiếng Anh:** Toàn bộ thuật ngữ trong giao diện, cốt truyện, thí nghiệm và kỹ năng sử dụng: `ester`, `acid`, `alcohol`, `glycerol` (chuẩn SGK mới GDPT 2018).
2. **Tên quái vật giản dị, chuẩn RPG:** Quái vật đặt tên ngắn gọn, quen thuộc (`Slime`, `Bầy Slime`, `Sói Băng`, `Thạch Quái`, `Song Quái`, `Hỏa Long`, `Chúa Tể Bóng Tối`, `Đại Ma Vương`).
3. **Tên chiêu thức đậm chất hóa học:** Vừa mang âm hưởng RPG vừa gắn liền với bản chất phản ứng hóa học (`Đòn Acid Chấn Động`, `Hỏa Cầu Ester Hóa`, `Khiên Dung Môi Hữu Cơ`, `Bão Xà Phòng Hóa`, `Sóng Thủy Phân Toàn Diện`, `Bão Nhiệt Phản Ứng`).
4. **Không cài thư viện bên ngoài:** Toàn bộ vận hành trơn tru trong một tệp `index.html` và thư mục `assets/` (thuần CSS/JS DOM, không phụ thuộc canvas/physics nặng nề).
5. **Đáp ứng đa thiết bị (Responsive):** Mọi màn hình từ điện ảnh Prologue, Chương 1 Đào tạo / Thí nghiệm ảo đến Sàn đấu 3 quái đều cân đối trên Mobile (<= 480px), Tablet (768px) và Desktop.

---

## Tiêu Điểm Đánh Giá Rủi Ro (Review Focus)

1. **Trải nghiệm vào trang mượt mà (Prologue Skipping):** Màn giới thiệu mở đầu phải có nút "Bỏ Qua (Skip) ⏩" để những người chơi quay lại không bị bắt buộc phải xem lại toàn bộ hoạt ảnh chữ chạy.
2. **Lưu tiến độ Chương 1 & Thí Nghiệm Ảo:** Khi người chơi đã hoàn thành Chương 1, lưu `localStorage.setItem("esterQuest_ch1Completed", "true")`. Lần sau vào chơi có thể chọn "Vào Thẳng Chiến Trường" hoặc "Học Lại Chương 1".
3. **Mượt mà trên Mobile đối với Thí Nghiệm Ảo:** Các thao tác kéo/chọn hóa chất, thanh trượt nhiệt độ và ghép nối ứng dụng phải hỗ trợ cảm ứng (touch events & click) mượt mà không bị vỡ bố cục trên màn hình hẹp.
4. **Sát thương AOE trên quái vật đã chết:** Đảm bảo chiêu AOE chỉ trừ máu và hiện hiệu ứng trên các quái còn sống (`hp > 0`).
5. **Chuỗi lượt phản công của bầy quái:** Khi có nhiều quái vật, các đòn phản công diễn ra tuần tự với độ trễ 400ms, không gây xung đột animation hoặc đè âm thanh.
6. **Chuyển giao 2 Phase của Đại Ma Vương:** Khi HP Phase 1 về 0, không được kết thúc game mà phải kích hoạt hiệu ứng sấm sét chớp giật, nạp thanh máu 500 HP và chuyển sang Phase 2.

---

## Sơ Đồ Toàn Bộ Tuyến Nội Dung Trò Chơi

```
┌────────────────────────────────────────────────────────────────────────┐
│  MÀN MỞ ĐẦU ĐIỆN ẢNH (PROLOGUE CINEMATIC - CỐT TRUYỆN HOÀNH TRÁNG)     │
│  "Kỷ nguyên Hóa Học năm 2026... Vương Quốc Ester chìm trong bóng tối...│
│   Các liên kết C-O bị xáo trộn, Ma Vật trỗi dậy từ Vực Thẳm..."        │
└───────────────────────────────────┬────────────────────────────────────┘
                                    ↓
┌────────────────────────────────────────────────────────────────────────┐
│  MÀN HÌNH NHẬP THÔNG TIN (CHARACTER CREATION): Tên Hiệp Sĩ & Lớp Học   │
└───────────────────────────────────┬────────────────────────────────────┘
                                    ↓
┌────────────────────────────────────────────────────────────────────────┐
│  CHƯƠNG 1: HỌC VIỆN ĐÀO TẠO CHIẾN BINH ESTER (BẮT BUỘC NHẬP MÔN)       │
├────────────────────────────────────────────────────────────────────────┤
│  Bài 1: Khái Niệm & Cấu Trúc Ester (R-COO-R', CnH2nO2) + Quiz 1        │
│  Bài 2: Danh Pháp Thần Bí (Gốc R' + Gốc Acid -ate) + Quiz 2            │
│  Bài 3: Tính Chất Vật Lý & Thí Nghiệm Ảo Nhiệt Độ Sôi (Boiling Lab)   │
│         ➔ Tương tác trượt nhiệt độ: Ethanol sôi 78°C, Acid 118°C       │
│  Bài 4: Thuật Thủy Phân & Thí Nghiệm Ảo Tách Lớp & Tráng Bạc          │
│         ➔ Ống nghiệm tách lớp, đun nóng lớp ester co lại               │
│         ➔ Thuốc thử AgNO3/NH3 tạo màng bạc lấp lánh (Silver Mirror)    │
│  Bài 5: Bí Thuật Điều Chế Ester & Mini-game Ghép Nối Ứng Dụng          │
│         ➔ Ghép Acid + Alcohol + H2SO4 đặc đun nóng tách lớp ester     │
│         ➔ Mini-game ghép nối mùi hương quả & ứng dụng đời sống        │
│  ➔ Lễ Tốt Nghiệp: Nhận Danh Hiệu "Hiệp Sĩ Ester" + Thưởng Bình Hồi Phục│
└───────────────────────────────────┬────────────────────────────────────┘
                                    ↓
┌────────────────────────────────────────────────────────────────────────┐
│  BẢNG CHỌN 4 KỸ NĂNG RA TRẬN (DECK LOADOUT - CHỌN 4 TRONG 10 CHIÊU)    │
└───────────────────────────────────┬────────────────────────────────────┘
                                    ↓
┌────────────────────────────────────────────────────────────────────────┐
│                        CHIẾN DỊCH 8 ẢI CHIẾN ĐẤU                       │
├────────────────────────────────────────────────────────────────────────┤
│ Ải 1: Slime (Lv.1) - 1 Quái [Khởi động tiền tuyến]                     │
│ Ải 2: Bầy Slime (Lv.1) - 3 QUÁI (Slime Xanh, Đỏ, Vàng) [Tập chiêu AOE!]│
│ Ải 3: Sói Băng (Lv.2) - 1 Quái [Tốc độ & Nhiệt độ sôi]                 │
│ Ải 4: Thạch Quái (Lv.3) - 1 Quái [Thủy phân bền vững]                  │
│ Ải 5: Song Quái (Lv.3) - 2 QUÁI TINH ANH (Chiến Binh Đao & Khiên)      │
│ Ải 6: Hỏa Long (Lv.4) - 1 Quái [Nhiệt lượng bùng nổ]                   │
│ Ải 7: Chúa Tể Bóng Tối (Lv.5) - 1 Boss [Hắc ám áp sát]                 │
│ Ải 8: 👑 ĐẠI MA VƯƠNG [NIGHTMARE SUPER BOSS 2 GIAI ĐOẠN]               │
│       ├── Phase 1: Đại Ma Vương (350 HP, Khiên Giảm Sát Thương 25%)    │
│       └── Phase 2: Đại Ma Vương Thức Tỉnh (500 HP, Cuồng Nộ Sức Mạnh)  │
└────────────────────────────────────────────────────────────────────────┘
```

---

## Chi Tiết Các Nhiệm Vụ Triển Khai (Tasks)

---

### Task 1: Màn Mở Đầu Điện Ảnh Hoành Tráng (Epic Prologue Intro Overlay)

**Mục tiêu:** Tạo màn hình mở đầu đậm chất sử thi viễn tưởng RPG ngay khi tải trang web, tạo cảm xúc hào hùng và bối cảnh lôi cuốn cho người chơi.

**Files:**
- Sửa đổi: `index.html` (Thêm khối `<div id="prologueOverlay">`, CSS hiệu ứng chữ chạy viễn tưởng, nút tiếp tục/bỏ qua).

- [x] **Bước 1: Viết nội dung lời dẫn sử thi**
  - *"Từ thuở sơ khai của thế giới Giả Kim, Vương Quốc Ester ngự trị trong sự cân bằng hoàn mỹ của các liên kết hóa học. Nhưng khi Vực Thẳm Hỗn Mang mở ra, Đại Ma Vương đã làm biến dị các phân tử, giải phóng bầy ma vật tàn phá muôn nơi..."*
  - *"Lời sấm truyền ngàn năm báo trước: Chỉ có một Hiệp Sĩ thấu suốt mọi bí kíp danh pháp, quy luật nhiệt độ sôi và thuật thủy phân xà phòng hóa mới có thể cầm chắc thanh kiếm tri thức để cứu rỗi vương triều!"*
- [x] **Bước 2: Hiệu ứng giao diện Prologue**
  - Khung cảnh vũ trụ u tối với tinh thể ester phát sáng lấp lánh (`box-shadow`, neon glow).
  - Chữ xuất hiện theo phong cách Cinematic từng đoạn uy nghi với chuyển động mượt mà.
  - Âm thanh nền huyền bí mở đầu bằng Web Audio synth.
  - Nút bấm rực sáng: `TIẾP TỤC BƯỚC VÀO THẾ GIỚI ➔` và nút góc `Bỏ Qua ⏩`.
- [x] **Bước 3: Kiểm tra và Commit**
  ```bash
  git add index.html
  git commit -m "feat(intro): add epic cinematic prologue storyline overlay"
  ```

---

### Task 2: Chương 1 - Học Viện Đào Tạo Chiến Binh Ester (5 Bài Học & 4 Thí Nghiệm Ảo)

**Mục tiêu:** Xây dựng Chương 1 thành một Học viện đào tạo bài bản với 5 bài học tương ứng 5 chuyên đề cốt lõi trong Bí Kíp Ester, tích hợp trực tiếp **Phòng Thí Nghiệm Ảo (Virtual Chemistry Lab)** với 4 tương tác sinh động và mini-game ghép nối ứng dụng / mùi hương.

**Files:**
- Sửa đổi: `index.html` (Thêm `<section id="academyScreen">`, bộ điều khiển thí nghiệm ảo `virtualLabEngine`, logic chuyển bài học, thanh tiến trình đào tạo).

**Cấu trúc 5 Bài Học & Thí Nghiệm Ảo Trong Chương 1:**

#### 1. Bài 1: Căn Bản Khái Niệm & Cấu Trúc Ester
- *Lý thuyết súc tích:* Khi thay thế nhóm `-OH` ở nhóm carboxyl (`-COOH`) bằng nhóm `-OR'` ta được ester ($RCOOR'$). Công thức no, đơn chức, mạch hở: $C_nH_{2n}O_2$ ($n \ge 2$).
- *Trực quan tương tác:* Mô hình liên kết phân tử 2D nhấp nháy làm nổi bật nhóm chức `-COO-`.
- *Thử thách 1:* Nhận diện nhanh công thức phân tử và nhóm chức ester trong 4 chất cho trước.

#### 2. Bài 2: Danh Pháp Thần Bí (Quy Tắc Gọi Tên Ester)
- *Lý thuyết súc tích:* Tên ester = Tên gốc $R'$ (alcohol) + Tên gốc acid $RCOO^-$ (đuôi *ate*). 
  - Ví dụ: $CH_3COOC_2H_5$ là *ethyl acetate*, $HCOOCH_3$ là *methyl formate*, $CH_2=CH-COOCH_3$ là *methyl acrylate*, $CH_3COOCH=CH_2$ là *vinyl acetate*.
- *Thử thách 2:* Chọn đúng tên gọi quốc tế chuẩn cho $CH_3COOCH_3$ và $HCOOC_2H_5$.

#### 3. Bài 3: Tính Chất Vật Lý & Thí Nghiệm Ảo Nhiệt Độ Sôi (Boiling Point & Volatility Lab)
- *Lý thuyết:* Thể lỏng/rắn ở điều kiện thường, nhẹ hơn nước, không tan trong nước, dễ bay hơi, có mùi thơm đặc trưng.
  - So sánh nhiệt độ sôi: $\text{Acid} > \text{Alcohol} > \text{Ester} > \text{Hydrocarbon}$ (do acid tạo liên kết hydrogen liên phân tử bền dạng dimer, alcohol tạo liên kết H, ester không tạo liên kết H giữa các phân tử với nhau).
- *Thí nghiệm ảo tương tác:*
  - Giao diện có 3 giá đựng hóa chất: Kệ Ester ($CH_3COOC_2H_5$, sôi ở 77°C), Kệ Alcohol ($C_2H_5OH$, sôi ở 78.3°C), Kệ Acid ($CH_3COOH$, sôi ở 118°C).
  - Người chơi chọn 1 hóa chất cho vào ống nghiệm trên giá đỡ có nhiệt kế.
  - Thanh trượt nhiệt độ (Temperature Slider) kéo từ 20°C đến 150°C.
  - Khi người chơi kéo nhiệt độ:
    - Nếu chọn Ethanol ($C_2H_5OH$) và kéo tới ~78°C: Bắt đầu xuất hiện các bọt khí sôi ùng ục và khói bay hơi bốc lên!
    - Nếu chọn Acetic acid ($CH_3COOH$): Kéo tới 78°C ống nghiệm vẫn im lìm, chỉ khi vượt 118°C mới bắt đầu sôi mạnh!
- *Thử thách 3:* Trả lời câu hỏi so sánh nhiệt độ sôi dựa trên thí nghiệm vừa quan sát.

#### 4. Bài 4: Thuật Thủy Phân, Thí Nghiệm Tách Lớp & Tráng Bạc (Hydrolysis & Silver Mirror Lab)
- *Lý thuyết:*
  - Thủy phân môi trường acid: Phản ứng thuận nghịch 2 chiều ($H^+, t^\circ$):
    $$RCOOR' + H_2O \overset{H^+, t^\circ}{\rightleftharpoons} RCOOH + R'OH$$
  - Thủy phân môi trường kiềm (xà phòng hóa): Phản ứng 1 chiều ($NaOH, t^\circ$):
    $$RCOOR' + NaOH \xrightarrow{t^\circ} RCOONa + R'OH$$
  - Phản ứng tráng bạc: Xảy ra với ester của acid formic ($HCOOR'$) hoặc ester thủy phân tạo aldehyde (như vinyl ester $RCOOCH=CH_2$).
- *Thí nghiệm ảo 1 (Tách lớp thủy phân môi trường acid):*
  - Ống nghiệm ban đầu: 2 lớp chất lỏng phân tách rõ rệt. Lớp trên là ester (dày, nhiều do không tan trong nước), lớp dưới là nước và xúc tác acid loãng.
  - Người chơi bấm nút "Đun Nóng" ($t^\circ$).
  - Diễn biến: Sau một thời gian đun, lớp ester ở trên co nhỏ lại (ít dần do phản ứng một phần), lớp dung dịch phía dưới dâng cao hơn.
  - Mũi tên chỉ thị trực quan:
    - Mũi tên trên: *"Lớp ester dư (chưa phản ứng hết)"*
    - Mũi tên dưới: *"Hỗn hợp thu được gồm: acid, alcohol, nước, xúc tác acid $H^+$"*
  - Hiển thị phương trình hóa học thuận nghịch 2 chiều phát sáng ở phía dưới.
- *Thí nghiệm ảo 2 (Phản ứng tráng bạc - Silver Mirror Test):*
  - Cho vinyl ester hoặc formate ester vào ống nghiệm thủy phân.
  - Xuất hiện lọ thuốc thử $AgNO_3 / NH_3$. Người chơi bấm/kéo lọ thuốc thử nhỏ vào ống nghiệm rồi đun nhẹ.
  - Diễn biến thị giác: Thành ống nghiệm sáng rực lên và phủ một lớp gương bạc sáng bóng ($Ag\downarrow$).
  - Hiện phương trình phản ứng tráng bạc: $CH_3CHO + 2[Ag(NH_3)_2]OH \xrightarrow{t^\circ} CH_3COONH_4 + 2Ag\downarrow + 3NH_3 + H_2O$.
- *Thử thách 4:* Dự đoán chất nào cho phản ứng tráng bạc sau khi thủy phân.

#### 5. Bài 5: Xưởng Điều Chế Ester & Mini-Game Ghép Nối Ứng Dụng (Synthesis Lab & Matching Quest)
- *Thí nghiệm ảo 3 (Xưởng điều chế Ester):*
  - Ống nghiệm ở trung tâm kẹp trên giá thí nghiệm, bên dưới có đèn cồn.
  - Khung trái: Danh sách Acid ($CH_3COOH$, $HCOOH$, $C_2H_5COOH$).
  - Khung phải: Danh sách Alcohol ($C_2H_5OH$, $CH_3OH$, $C_5H_{11}OH$).
  - Ở giữa: Lọ xúc tác $H_2SO_4$ đặc và đá bọt.
  - Tương tác: Người chơi chọn 1 Acid + 1 Alcohol nhỏ vào ống nghiệm, thêm xúc tác $H_2SO_4$ đặc, bấm đun nóng.
  - Kết quả: Dung dịch dần dần tách thành 2 lớp và hình thành lớp ester thơm nổi lên trên.
  - Hoạt họa ghép phân tử: Gốc $RCO-$ của acid ghép với $-OR'$ của alcohol $\rightarrow RCOOR' + H_2O$.
  - Phương trình điều chế hiển thị rõ ràng bên dưới.
- *Mini-Game Ghép Nối (Interactive Matching Quests):*
  - **Màn 1: Ghép Ester với Mùi Hương Hoa Quả:**
    - Isoamyl acetate $\leftrightarrow$ Mùi chuối chín
    - Ethyl butyrate / Ethyl propionate $\leftrightarrow$ Mùi dứa chín
    - Benzyl acetate $\leftrightarrow$ Mùi hoa nhài thơm ngát
    - Geranyl acetate $\leftrightarrow$ Mùi hoa hồng
  - **Màn 2: Ghép Ester với Ứng Dụng Đời Sống:**
    - Methyl methacrylate $\leftrightarrow$ Sản xuất thủy tinh hữu cơ Plexiglas (kính chắn gió máy bay, răng giả)
    - Ethyl acetate / Butyl acetate $\leftrightarrow$ Dung môi pha sơn, mực in, tách chiết dược liệu
    - Triacylglycerol (chất béo) $\leftrightarrow$ Sản xuất xà phòng, glycerol, chế biến thực phẩm
    - Methyl salicylate / Aspirin $\leftrightarrow$ Thuốc xoa bóp giảm đau, kháng viêm
- *Lễ Tốt Nghiệp Chương 1:*
  - Phong tước "🎖️ Hiệp Sĩ Ester Chính Thức", thưởng thêm 1 Bình Nước Cất dự trữ, lưu tiến độ vào `localStorage`.
  - Hiển thị nút lớn: `TIẾN VÀO TRANG BỊ KỸ NĂNG ➔`.

- [ ] **Bước 1: Thiết kế giao diện Học Viện Giả Kim (`#academyScreen`) & Bộ Khung Thí Nghiệm Ảo**
  - Khung ống nghiệm CSS với chất lỏng 2 lớp, hiệu ứng bọt khí sôi, khói hơi nước, ngọn lửa đèn cồn.
  - Thanh trượt nhiệt độ 20°C - 150°C và kệ đựng hóa chất.
- [ ] **Bước 2: Xây dựng logic Thí nghiệm Ảo Thủy Phân & Tráng Bạc**
  - Chuyển động co giãn thể tích 2 lớp (ester dư trên, dung dịch hỗn hợp dưới).
  - Hiệu ứng tráng bạc sáng loáng thành ống nghiệm.
- [ ] **Bước 3: Xây dựng logic Thí nghiệm Ảo Điều Chế & Nhiệt Độ Sôi**
  - Lựa chọn Acid + Alcohol + $H_2SO_4$ đặc tạo ester.
  - Đun sôi theo nhiệt độ sôi đặc trưng của từng chất.
- [ ] **Bước 4: Xây dựng Mini-game Ghép Nối Thẻ (Matching Pairs)**
  - Cơ chế kéo thả hoặc bấm chọn 2 thẻ tương ứng để nối mùi hương và ứng dụng thực tế.
- [ ] **Bước 5: Kiểm tra và Commit**
  ```bash
  git add index.html
  git commit -m "feat(academy): implement interactive virtual chemistry lab and matching mini-games in chapter 1"
  ```

---

### Task 3: Bảng Chọn 4 Kỹ Năng Ra Trận (Active Skill Deck Loadout)

**Mục tiêu:** Cho phép người chơi tự do lựa chọn 4 trong số 10 chiêu thức để trang bị vào thanh chiến đấu (Deck building chiến thuật).

**Files:**
- Sửa đổi: `index.html` (Thêm modal / panel chọn kỹ năng, lưu cấu hình vào `state.activeSkills`).

**Danh sách 10 Chiêu Thức Hóa Học Hoàn Chỉnh:**

| ID | Tên Chiêu Thức | Kiểu Đánh | MP | Sát Thương | Hiệu Ứng RPG Đặc Biệt | Mức Câu Hỏi |
|:---:|:---|:---:|:---:|:---:|:---|:---:|
| **1** | 🗡️ **Đòn Acid Chấn Động** | Đơn | 0 | 35 ST | Hồi 10 MP nếu trả lời đúng | ⭐ Nhận Biết |
| **2** | 🔥 **Hỏa Cầu Ester Hóa** | Đơn | 20 | 75 ST | Đòn nhiệt năng công phá đơn mục tiêu | ⭐⭐ Thông Hiểu |
| **3** | 🛡️ **Khiên Dung Môi Hữu Cơ** | Hỗ trợ | 15 | +35 HP | Tạo màng bọc chặn hoàn toàn đòn đánh kế tiếp | ⭐⭐ Thông Hiểu |
| **4** | ⚡ **Bão Xà Phòng Hóa** | Đơn | 35 | 150 ST | Thủy phân cực đại & Choáng quái 1 lượt | ⭐⭐⭐ Vận Dụng |
| **5** | 🌸 **Độc Khí Ester Thơm** | Đơn | 18 | 40 ST | **Gây độc (DoT):** Quái mất 15 HP/lượt trong 3 lượt | ⭐⭐ Thông Hiểu |
| **6** | 🧪 **Chiết Tách Dung Môi** | Đơn | 12 | 45 ST | **Hút máu:** Tách chiết hồi phục 25 HP cho người chơi | ⭐⭐ Thông Hiểu |
| **7** | 🪞 **Gương Bạc Lóa Mắt** | Đơn | 22 | 65 ST | **Gây mù (Blind):** Phản xạ chói lòa, đòn quái trượt 70% | ⭐⭐ Thông Hiểu |
| **8** | 💥 **Bộc Phá Oxi Hóa** | Đơn | Toàn bộ | $MP \times 3.5$ | **Mana Burst:** Đốt cháy toàn bộ MP dứt điểm đối thủ | ⭐⭐⭐ Vận Dụng |
| **9** | 🌊 **Sóng Thủy Phân Toàn Diện** | **AOE** | 28 | 60 ST/quái | **Sát thương diện rộng:** Quét sạch TẤT CẢ quái vật trên sân | ⭐⭐ Thông Hiểu |
| **10**| 🌪️ **Bão Nhiệt Phản Ứng** | **AOE** | 42 | 95 ST/quái | **AOE Cực Đại:** Quét sạch toàn bộ quái & giảm 25% công | ⭐⭐⭐ Vận Dụng |

- [ ] **Bước 1: Giao diện Thư Viện Kỹ Năng (Grimoire)**
  - Hiển thị 10 thẻ chiêu thức với thông số rõ ràng.
  - Khung 4 ô kích hoạt (Active Slots) cho phép click chọn linh hoạt.
- [ ] **Bước 2: Đồng bộ hóa vào Dashboard chiến đấu**
  - Render đúng 4 chiêu mà người chơi đã trang bị lên màn hình trận chiến.
- [ ] **Bước 3: Kiểm tra và Commit**
  ```bash
  git add index.html
  git commit -m "feat(deck): implement 10-skill grimoire and 4-slot tactical deck loadout"
  ```

---

### Task 4: Nâng Cấp Động Cơ Chiến Đấu Đa Quái Vật & Kỹ Năng AOE

**Mục tiêu:** Nâng cấp sàn đấu hỗ trợ xuất hiện từ 1 đến 3 quái vật đồng thời, hỗ trợ chọn mục tiêu ngắm bắn và thi triển đòn đánh diện rộng AOE.

**Files:**
- Sửa đổi: `index.html` (CSS `.enemies-container`, JS `state.enemies`, `resolveTurnAction` phân nhánh AOE).

- [ ] **Bước 1: Cấu trúc hiển thị nhiều quái vật**
  - Hỗ trợ dàn 1, 2 hoặc 3 quái trên cùng một hàng ngang với thanh máu và sprite độc lập.
  - Vòng tròn ngắm bắn neon (`target-indicator`) hiển thị quái đang được chọn.
- [ ] **Bước 2: Logic thi triển chiêu AOE (`targetType === 'all'`)**
  - Gây sát thương đồng loạt lên tất cả quái vật có `hp > 0`.
  - Hiệu ứng chớp sáng toàn sàn đấu và số nổi sát thương hiển thị trên từng quái.
- [ ] **Bước 3: Chuỗi phản công của bầy quái**
  - Từng quái vật còn sống sẽ lần lượt lao lên tấn công người chơi cách nhau 400ms.
- [ ] **Bước 4: Kiểm tra và Commit**
  ```bash
  git add index.html
  git commit -m "feat(combat): implement multi-enemy targeting and AOE spell execution engine"
  ```

---

### Task 5: Cấu Hình Chiến Dịch 8 Ải Đánh Quái & Boss Tối Thượng 2 Giai Đoạn

**Mục tiêu:** Xây dựng trọn vẹn 8 Ải chiến đấu với tên gọi quái vật đơn giản chuẩn RPG, bao gồm 2 ải nhiều quái và Ải 8 Nightmare Boss.

**Files:**
- Sửa đổi: `index.html` (Mảng `STAGES`, hàm `loadStage`, `triggerBossPhase2`).

**Danh sách 8 Ải Chi Tiết:**
1. **Ải 1: Rừng Ẩm Ướt** — 1 Quái: `Slime` (`Lv.1`, HP: 100).
2. **Ải 2: Đầm Lầy Bầy Nhầy (MỚI - 3 QUÁI):** `Bầy Slime` (`Slime Xanh` HP 60, `Slime Đỏ` HP 70, `Slime Vàng` HP 80). *Màn tập luyện chiêu AOE!*
3. **Ải 3: Thung Lũng Băng** — 1 Quái: `Sói Băng` (`Lv.2`, HP: 160).
4. **Ải 4: Hầm Ngục Thạch** — 1 Quái: `Thạch Quái` (`Lv.3`, HP: 220).
5. **Ải 5: Tháp Canh Đôi (MỚI - 2 QUÁI TINH ANH):** `Song Quái` (`Chiến Binh Đao` HP 150, `Chiến Binh Khiên` HP 150).
6. **Ải 6: Tháp Địa Ngục** — 1 Quái: `Hỏa Long` (`Lv.4`, HP: 280).
7. **Ải 7: Điện Thờ Hắc Ám** — 1 Quái: `Chúa Tể Bóng Tối` (`Lv.5`, HP: 360).
8. **Ải 8: VỰC THẲM HỖN MANG - ĐẠI CHIẾN ĐẠI MA VƯƠNG (NIGHTMARE SUPER BOSS):**
   - **Phase 1:** `Đại Ma Vương` (HP: 350, ATK: 45) — Giảm 25% sát thương nhận vào.
   - **Phase 2:** `Đại Ma Vương Thức Tỉnh` 👑 (HP: 500, ATK: 55) — Kích hoạt Cuồng nộ tăng 15% ATK mỗi 2 lượt.
   - **Bộ câu hỏi:** Chuyên dụng 38 câu hỏi Vận Dụng Cao.

- [ ] **Bước 1: Cập nhật cấu hình 8 Ải trong `STAGES`**
- [ ] **Bước 2: Xây dựng cơ chế chuyển Phase cho Đại Ma Vương**
  - Màn hình rung chuyển dữ dội, sân đấu chuyển đỏ rực u tối, nạp cây máu Phase 2.
- [ ] **Bước 3: Kiểm tra và Commit**
  ```bash
  git add index.html
  git commit -m "feat(stages): configure 8 classic RPG stages with 2-phase nightmare boss"
  ```

---

### Task 6: Kiểm Thử Toàn Diện, Responsive & Hoàn Thiện

**Mục tiêu:** Kiểm tra toàn bộ hành trình: Prologue -> Nhập Tên -> Chương 1 (5 Bài + 4 Thí Nghiệm Ảo + Ghép Nối) -> Chọn Deck -> 8 Ải -> Chiến Thắng.

**Files:**
- Sửa đổi: `index.html`, `README.md`.
- Script kiểm tra: `tests/verify_full_flow.py`.

- [ ] **Bước 1: Viết script Python tự động kiểm tra toàn bộ DOM, hàm JavaScript và cú pháp**
- [ ] **Bước 2: Kiểm tra Responsive trên Mobile và Desktop**
- [ ] **Bước 3: Cập nhật `README.md` đầy đủ hướng dẫn**
- [ ] **Bước 4: Commit và đẩy lên GitHub**
  ```bash
  git add .
  git commit -m "docs: finalize complete game design with prologue, virtual lab academy, and 8 stages"
  git push origin main
  ```

---

## Xác Nhận Sẵn Sàng Triển Khai

Kế hoạch này đã kết hợp hài hòa và trọn vẹn:
1. **Phần mở đầu hoành tráng (Epic Prologue Intro)** ngay khi truy cập web.
2. **Chương 1: Học Viện Đào Tạo Chiến Binh Ester** với 5 bài học tương ứng 5 mục Bí Kíp Ester và **Phòng Thí Nghiệm Ảo Giả Kim** (Thủy phân tách lớp, tráng bạc, điều chế ester, đo nhiệt độ sôi, mini-game ghép ứng dụng/mùi hương).
3. **Kho 10 Chiêu Thức Giả Kim** (bao gồm 2 chiêu AOE diện rộng và các hiệu ứng RPG đặc sắc).
4. **Chiến Dịch 8 Ải Đánh Quái** với tên gọi quái vật đơn giản, 2 màn bầy quái, và **Ải 8 Đại Ma Vương 2 Giai Đoạn**.
5. **Kho 162 câu hỏi chuẩn hóa** không trùng lặp, chia đều theo 3 cấp độ.

Khi bạn đồng ý, chúng ta sẽ bắt đầu triển khai code từng nhiệm vụ một cách chuẩn xác nhất!
