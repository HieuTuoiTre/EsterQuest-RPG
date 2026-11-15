# Kế Hoạch Triển Khai: Mở Đầu Hoành Tráng, Chương 1 Đào Tạo Hiệp Sĩ & Chiến Dịch 8 Ải (PLAN.MD)

> **Dành cho kỹ sư / Agent triển khai:** BẮT BUỘC SỬ DỤNG SUB-SKILL: `superpowers:subagent-driven-development` (khuyên dùng) hoặc `superpowers:executing-plans` để thực thi từng nhiệm vụ theo thứ tự. Các bước sử dụng cú pháp checkbox (`- [ ]`) để theo dõi tiến độ.

**Mục tiêu (Goal):** 
1. Xây dựng màn mở đầu cốt truyện điện ảnh hoành tráng (Epic Prologue Intro) ngay khi bấm vào trang web.
2. Thiết kế **Chương 1: Học Viện Đào Tạo Chiến Binh Ester** với 5 bài học kiến thức tương ứng các mục trong Bí Kíp Ester (Khái niệm, Danh pháp, Lý tính, Hóa tính, Điều chế & Ứng dụng).
3. Mở rộng kho kỹ năng chiến đấu (bao gồm các chiêu AOE diện rộng và chiêu đơn mục tiêu độc đáo) cùng bảng chọn 4 chiêu (Skill Deck).
4. Mở rộng chiến dịch lên **8 Ải Đánh Quái** (với 2 ải nhiều quái) và **Ải 8 Nightmare Super Boss** 2 Giai đoạn độ khó cực cao.

**Kiến trúc (Architecture):**
- **Luồng phân cảnh mới:** `Prologue Cinematic Screen` ➔ `Menu Nhập Tên & Lớp` ➔ `Chương 1: Học Viện Đào Tạo Hiệp Sĩ (5 Bài Học Bí Kíp)` ➔ `Trang Bị Kỹ Năng (Deck Loadout)` ➔ `Chiến Trường 8 Ải`.
- **Động cơ học tập tương tác (Academy Learning Engine):** Mỗi bài học có thẻ lý thuyết rút gọn đẹp mắt kèm 1 câu hỏi kiểm tra nhanh để mở khóa bài tiếp theo.
- **Động cơ chiến đấu đa mục tiêu (Multi-Enemy & AOE Engine):** Hỗ trợ dàn 1-3 quái vật trên sàn đấu, cơ chế ngắm bắn click-to-target và sát thương toàn sân.
- **Trùm cuối 2 Phase biến dị:** Tự động hồi sinh, đổi sprite/tên và kích hoạt cuồng nộ ở Phase 2.

**Công nghệ (Tech Stack):** Pure Vanilla JavaScript (ES6+), HTML5, CSS3 (Keyframes Animations, Flexbox/Grid, Pixelated Rendering), Web Audio API Synthesizers.

---

## Ràng Buộc Toàn Cục (Global Constraints)

1. **Chuẩn hóa danh pháp tiếng Anh:** Toàn bộ thuật ngữ trong giao diện, cốt truyện và kỹ năng sử dụng: `ester`, `acid`, `alcohol`, `glycerol` (chuẩn SGK mới GDPT 2018).
2. **Tên quái vật giản dị, chuẩn RPG:** Quái vật đặt tên ngắn gọn, quen thuộc (`Slime`, `Bầy Slime`, `Sói Băng`, `Thạch Quái`, `Song Quái`, `Hỏa Long`, `Chúa Tể Bóng Tối`, `Đại Ma Vương`).
3. **Tên chiêu thức đậm chất hóa học:** Vừa mang âm hưởng RPG vừa gắn liền với bản chất phản ứng hóa học (`Đòn Acid Chấn Động`, `Hỏa Cầu Ester Hóa`, `Khiên Dung Môi Hữu Cơ`, `Bão Xà Phòng Hóa`, `Sóng Thủy Phân Toàn Diện`, `Bão Nhiệt Phản Ứng`).
4. **Không cài thư viện bên ngoài:** Toàn bộ vận hành trơn tru trong một tệp `index.html` và thư mục `assets/`.
5. **Đáp ứng đa thiết bị (Responsive):** Mọi màn hình từ điện ảnh Prologue, Chương 1 Đào tạo đến Sàn đấu 3 quái đều cân đối trên Mobile (<= 480px) và Tablet (768px).

---

## Tiêu Điểm Đánh Giá Rủi Ro (Review Focus)

1. **Trải nghiệm vào trang mượt mà (Prologue Skipping):** Màn giới thiệu mở đầu phải có nút "Bỏ Qua (Skip) ⏩" để những người chơi quay lại không bị bắt buộc phải xem lại toàn bộ hoạt ảnh chữ chạy.
2. **Lưu tiến độ Chương 1 Đào Tạo:** Khi người chơi đã hoàn thành Chương 1, lưu `localStorage.setItem("esterQuest_ch1Completed", "true")`. Lần sau vào chơi có thể chọn "Vào Thẳng Chiến Trường" hoặc "Học Lại Chương 1".
3. **Sát thương AOE trên quái vật đã chết:** Đảm bảo chiêu AOE chỉ trừ máu và hiện hiệu ứng trên các quái còn sống (`hp > 0`).
4. **Chuỗi lượt phản công của bầy quái:** Khi có nhiều quái vật, các đòn phản công diễn ra tuần tự với độ trễ 400ms, không gây xung đột animation hoặc đè âm thanh.
5. **Chuyển giao 2 Phase của Đại Ma Vương:** Khi HP Phase 1 về 0, không được kết thúc game mà phải kích hoạt hiệu ứng sấm sét chớp giật, nạp thanh máu 500 HP và chuyển sang Phase 2.

---

## Sơ Đồ Toàn Bộ Tuyến Nội Dung Trò Chơi

```
┌────────────────────────────────────────────────────────────────────────┐
│  MÀN MỞ ĐẦU ĐIỆN ẢNH (PROLOGUE CINEMATIC - CỐT TRUYỆN HOÀNH TRÁNG)     │
│  "Kỷ nguyên Hóa Học năm 2026... Vương Quốc Ester chìm trong bóng tối...│
│   Các liên kết C-O bị xáo trộn, Ma Vật trỗi dậy từ Vực Thẳm..."       │
└───────────────────────────────────┬────────────────────────────────────┘
                                    ↓
┌────────────────────────────────────────────────────────────────────────┐
│  MÀN HÌNH NHẬP THÔNG TIN (CHARACTER CREATION): Tên Hiệp Sĩ & Lớp Học   │
└───────────────────────────────────┬────────────────────────────────────┘
                                    ↓
┌────────────────────────────────────────────────────────────────────────┐
│  CHƯƠNG 1: HỌC VIỆN ĐÀO TẠO CHIẾN BINH ESTER (BẮT BUỘC NHẬP MÔN)     │
├────────────────────────────────────────────────────────────────────────┤
│  Bài 1: Khái Niệm & Nhóm Chức Ester (Cấu trúc R-COO-R', CnH2nO2)       │
│  Bài 2: Danh Pháp Thần Bí (Quy tắc gọi tên: Gốc R' + Gốc Acid -ate)    │
│  Bài 3: Vật Lý & Mùi Hương Hoa Quả (Nhiệt độ sôi, mùi chuối, dứa, nhài)│
│  Bài 4: Thuật Thủy Phân & Xà Phòng Hóa (MT Acid 2 chiều, MT Base 1 chiều│
│  Bài 5: Điều Chế & Ứng Dụng Đời Sống (Xúc tác H2SO4 đặc, thủy tinh hữu cơ│
│  ➔ Lễ Tốt Nghiệp: Nhận Danh Hiệu "Hiệp Sĩ Ester" + Thưởng Bình Hồi Phục│
└───────────────────────────────────┬────────────────────────────────────┘
                                    ↓
┌────────────────────────────────────────────────────────────────────────┐
│  BẢNG CHỌN 4 KỸ NĂNG RA TRẬN (DECK LOADOUT - CHỌN 4 TRONG 10 CHIÊU)    │
└───────────────────────────────────┬────────────────────────────────────┘
                                    ↓
┌────────────────────────────────────────────────────────────────────────┐
│                        CHIẾN DỊCH 8 ẢI CHIẾN ĐẤU                      │
├────────────────────────────────────────────────────────────────────────┤
│ Ải 1: Slime (Lv.1) - 1 Quái [Khởi động tiền tuyến]                     │
│ Ải 2: Bầy Slime (Lv.1) - 3 QUÁI (Slime Xanh, Đỏ, Vàng) [Tập chiêu AOE!]│
│ Ải 3: Sói Băng (Lv.2) - 1 Quái [Tốc độ & Nhiệt độ sôi]                │
│ Ải 4: Thạch Quái (Lv.3) - 1 Quái [Thủy phân bền vững]                  │
│ Ải 5: Song Quái (Lv.3) - 2 QUÁI TINH ANH (Chiến Binh Đao & Khiên)     │
│ Ải 6: Hỏa Long (Lv.4) - 1 Quái [Nhiệt lượng bùng nổ]                   │
│ Ải 7: Chúa Tể Bóng Tối (Lv.5) - 1 Boss [Hắc ám áp sát]                 │
│ Ải 8: 👑 ĐẠI MA VƯƠNG [NIGHTMARE SUPER BOSS 2 GIAI ĐOẠN]               │
│       ├── Phase 1: Đại Ma Vương (350 HP, Khiên Giảm Sát Thương 25%)    │
│       └── Phase 2: Đại Ma Vương Thức Tỉnh (500 HP, Cuồng Nộ Sức Mạnh) │
└────────────────────────────────────────────────────────────────────────┘
```

---

## Chi Tiết Các Nhiệm Vụ Triển Khai (Tasks)

---

### Task 1: Màn Mở Đầu Điện Ảnh Hoành Tráng (Epic Prologue Intro Overlay)

**Mục tiêu:** Tạo màn hình mở đầu đậm chất sử thi viễn tưởng RPG ngay khi tải trang web, tạo cảm xúc hào hùng và bối cảnh lôi cuốn cho người chơi.

**Files:**
- Sửa đổi: `index.html` (Thêm khối `<div id="prologueOverlay">`, CSS hiệu ứng chữ chạy viễn tưởng, nút tiếp tục/bỏ qua).

- [ ] **Bước 1: Viết nội dung lời dẫn sử thi**
  - *"Từ thuở sơ khai của thế giới Giả Kim, Vương Quốc Ester ngự trị trong sự cân bằng hoàn mỹ của các liên kết hóa học. Nhưng khi Vực Thẳm Hỗn Mang mở ra, Đại Ma Vương đã làm biến dị các phân tử, giải phóng bầy ma vật tàn phá muôn nơi..."*
  - *"Lời sấm truyền ngàn năm báo trước: Chỉ có một Hiệp Sĩ thấu suốt mọi bí kíp danh pháp và quy luật phản ứng xà phòng hóa mới có thể cầm chắc thanh kiếm tri thức để cứu rỗi vương triều!"*
- [ ] **Bước 2: Hiệu ứng giao diện Prologue**
  - Khung cảnh vũ trụ u tối với tinh thể ester phát sáng lấp lánh.
  - Chữ xuất hiện theo phong cách Cinematic từng đoạn uy nghi.
  - Âm thanh nền huyền bí mở đầu (nếu bật âm thanh).
  - Nút bấm rực sáng: `TIẾP TỤC BƯỚC VÀO THẾ GIỚI ➔` và nút góc `Bỏ Qua ⏩`.
- [ ] **Bước 3: Kiểm tra và Commit**
  ```bash
  git add index.html
  git commit -m "feat(intro): add epic cinematic prologue storyline overlay"
  ```

---

### Task 2: Chương 1 - Học Viện Đào Tạo Chiến Binh Ester (5 Bài Học Nhập Môn)

**Mục tiêu:** Xây dựng Chương 1 thành một Học viện đào tạo bài bản với 5 bài học tương ứng 5 chuyên đề cốt lõi trong Bí Kíp Ester, mỗi bài có 1 thử thách kiểm tra nhanh để mở khóa bài tiếp theo.

**Files:**
- Sửa đổi: `index.html` (Thêm `<section id="academyScreen">`, logic chuyển bài học, thanh tiến trình đào tạo).

**Cấu trúc 5 Bài Học Trong Chương 1:**

1. **Bài 1: Căn Bản Khái Niệm & Cấu Trúc Ester**
   - *Kiến thức:* Khi thay thế nhóm `-OH` ở nhóm carboxyl (`-COOH`) bằng nhóm `-OR'` ta được ester ($RCOOR'$). Công thức no, đơn chức, mạch hở: $C_nH_{2n}O_2$ ($n \ge 2$).
   - *Thử thách 1:* Nhận diện công thức ester trong 4 chất cho trước.
2. **Bài 2: Danh Pháp Thần Bí (Quy Tắc Gọi Tên Ester)**
   - *Kiến thức:* Tên ester = Tên gốc $R'$ + Tên gốc acid $RCOO^-$ (đuôi *ate*). Ví dụ: $CH_3COOC_2H_5$ là ethyl acetate, $HCOOCH_3$ là methyl formate.
   - *Thử thách 2:* Gọi tên đúng chất $CH_3COOCH_3$.
3. **Bài 3: Tính Chất Vật Lý & Mùi Hương Hoa Quả**
   - *Kiến thức:* Nhiệt độ sôi: Acid > Alcohol > Ester > Hydrocarbon. Mùi hương: Isoamyl acetate (mùi chuối chín), Ethyl propionate (mùi dứa), Benzyl acetate (hoa nhài).
   - *Thử thách 3:* Nối đúng ester với mùi hương tương ứng.
4. **Bài 4: Thuật Thủy Phân & Phản Ứng Xà Phòng Hóa**
   - *Kiến thức:* Thủy phân môi trường acid (thuận nghịch $H^+, t^\circ$ tạo acid + alcohol). Thủy phân môi trường kiềm (xà phòng hóa 1 chiều tạo muối + alcohol/aldehyde/phenol).
   - *Thử thách 4:* Dự đoán sản phẩm khi thủy phân $CH_3COOC_2H_5 + NaOH$.
5. **Bài 5: Bí Thuật Điều Chế & Ứng Dụng Thực Tiễn**
   - *Kiến thức:* Phản ứng ester hóa dùng $H_2SO_4$ đặc làm xúc tác và hút nước để chuyển dịch cân bằng. Trùng hợp methyl methacrylate làm thủy tinh hữu cơ plexiglas.
   - *Thử thách 5:* Thao tác tương tác chọn hóa chất và điều kiện phản ứng ester hóa.

- [ ] **Bước 1: Giao diện Học Viện Giả Kim (`#academyScreen`)**
  - Lộ trình 5 bước huấn luyện (Step-by-step Training Stepper).
  - Khung nội dung bài học súc tích, chữ to rõ, công thức định dạng chuẩn.
- [ ] **Bước 2: Cơ chế mở khóa bài học tuần tự**
  - Người chơi đọc lý thuyết -> Bấm "Làm Bài Kiểm Tra Lĩnh Hội" -> Trả lời đúng sẽ mở khóa bài học tiếp theo và nhận huy hiệu sao.
- [ ] **Bước 3: Lễ Tốt Nghiệp Chương 1**
  - Khi hoàn thành cả 5 bài: Phong tước "🎖️ Hiệp Sĩ Ester Chính Thức", thưởng thêm 1 Bình Nước Cất dự trữ, lưu `localStorage`.
  - Hiển thị nút lớn: `TIẾN VÀO TRANG BỊ KỸ NĂNG ➔`.
- [ ] **Bước 4: Kiểm tra và Commit**
  ```bash
  git add index.html
  git commit -m "feat(ch1): build chapter 1 knight training academy with 5 interactive lessons"
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
  - Khung 4 ô kích hoạt (Active Slots) cho phép kéo/chọn linh hoạt.
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

**Mục tiêu:** Kiểm tra toàn bộ hành trình: Prologue -> Nhập Tên -> Chương 1 (5 Bài) -> Chọn Deck -> 8 Ải -> Chiến Thắng.

**Files:**
- Sửa đổi: `index.html`, `README.md`.
- Script kiểm tra: `tests/verify_full_flow.py`.

- [ ] **Bước 1: Viết script Python tự động kiểm tra toàn bộ DOM và cú pháp**
- [ ] **Bước 2: Kiểm tra Responsive trên Mobile và Desktop**
- [ ] **Bước 3: Cập nhật `README.md` đầy đủ hướng dẫn**
- [ ] **Bước 4: Commit và đẩy lên GitHub**
  ```bash
  git add .
  git commit -m "docs: finalize complete game design with prologue, training academy, and 8 stages"
  git push origin main
  ```

---

## Xác Nhận Sẵn Sàng Triển Khai

Kế hoạch này đã kết hợp hài hòa và trọn vẹn:
1. **Phần mở đầu hoành tráng (Epic Prologue Intro)** ngay khi truy cập web.
2. **Chương 1: Học Viện Đào Tạo Chiến Binh Ester** với 5 bài học tương ứng 5 mục Bí Kíp Ester.
3. **Kho 10 Chiêu Thức Giả Kim** (bao gồm 2 chiêu AOE diện rộng và các hiệu ứng RPG đặc sắc).
4. **Chiến Dịch 8 Ải Đánh Quái** với tên gọi quái vật đơn giản, 2 màn bầy quái, và **Ải 8 Đại Ma Vương 2 Giai Đoạn**.
5. **Kho 162 câu hỏi chuẩn hóa** không trùng lặp, chia đều theo 3 cấp độ.

Khi bạn đồng ý, chúng ta sẽ bắt đầu triển khai code từng nhiệm vụ một cách chuẩn xác nhất!
