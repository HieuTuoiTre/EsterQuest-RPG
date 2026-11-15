# Kế Hoạch Triển Khai: Làng Tân Thủ, Kỹ Năng AOE & Chiến Dịch 8 Ải Đánh Trùm (PLAN.MD)

> **Dành cho kỹ sư / Agent triển khai:** BẮT BUỘC SỬ DỤNG SUB-SKILL: `superpowers:subagent-driven-development` (khuyên dùng) hoặc `superpowers:executing-plans` để thực thi từng nhiệm vụ theo thứ tự. Các bước sử dụng cú pháp checkbox (`- [ ]`) để theo dõi tiến độ.

**Mục tiêu (Goal):** Xây dựng Làng Tân Thủ bắt buộc học bí kíp & làm nhiệm vụ nhập môn; mở rộng chiến dịch lên **8 Ải**, hỗ trợ **nhiều quái vật trên sân đấu cùng lúc (Multi-Enemy)**; bổ sung **chiêu thức diện rộng (AOE)**; và thiết kế **Màn Đánh Boss Tối Thượng Độ Khó Cực Cao (Nightmare Super Boss)** với cơ chế 2 Phase tiến hóa và câu hỏi Vận Dụng Cao.

**Kiến trúc (Architecture):**
- Màn hình `#villageScreen` làm cổng trung chuyển với 3 nhiệm vụ mở khóa.
- Động cơ chiến đấu (`Battle Engine`) nâng cấp từ đơn mục tiêu (`state.enemy`) sang đa mục tiêu (`state.enemies: Array<Enemy>` và `state.selectedTargetIndex`).
- Hệ thống chiêu thức hỗ trợ gắn nhãn mục tiêu `targetType: 'single' | 'all'`, tự động phân bổ sát thương đơn hoặc AOE diện rộng.
- Cơ chế Boss Tối Thượng 2 Phase: Khi Boss Phase 1 hết máu, tự động kích hoạt hoạt ảnh biến dị sang Phase 2 với bộ chiêu thức và nội tại cuồng nộ mới.

**Công nghệ (Tech Stack):** Pure Vanilla JavaScript (ES6+), HTML5, CSS3 (CSS Grid/Flexbox, Keyframes Animations, Pixelated Rendering), Web Audio API Synthesizers.

**Tài liệu đặc tả (Spec):** 
1. Làng tân thủ bắt buộc học bí kíp & làm nhiệm vụ nhỏ trước khi vào đánh quái.
2. Mở rộng thêm 3 ải chiến đấu mới (nâng tổng số lên 8 ải).
3. Có các màn xuất hiện nhiều quái vật cùng lúc (Multi-enemy).
4. Thêm các chiêu thức có sát thương diện rộng (AOE).
5. Thêm 1 màn Boss tối thượng có độ khó cực cao (Nightmare Super Boss).
6. Ghi toàn bộ kế hoạch vào `PLAN.MD`.

---

## Ràng Buộc Toàn Cục (Global Constraints)

1. **Không cài thư viện bên ngoài:** Toàn bộ game chạy thuần trên tệp `index.html` và tài nguyên trong thư mục `assets/`.
2. **Đáp ứng đa thiết bị (Responsive Design):** Sàn đấu khi có 1, 2, hoặc 3 quái vật đều phải hiển thị cân đối, không tràn màn hình trên Mobile (<= 480px) và Tablet (768px).
3. **Bảo toàn dữ liệu cũ:** Giữ nguyên các câu hỏi trong ngân hàng đề, cơ chế trừ mana khi niệm chiêu và phong cách đồ họa RPG turn-based.
4. **Cơ chế chọn mục tiêu trực quan:** Khi có nhiều quái vật, người chơi có thể click vào quái để đổi mục tiêu đánh đơn; chiêu AOE sẽ tự động đánh trúng toàn bộ quái còn sống.

---

## Tiêu Điểm Đánh Giá Rủi Ro (Review Focus)

1. **Sát thương AOE trên quái đã tử trận:** Khi tung chiêu AOE, sát thương và hiệu ứng nổi chỉ được hiển thị trên các quái vật còn sống (`hp > 0`), không tạo hiệu ứng rác trên quái đã chết.
2. **Lượt phản công của bầy quái (Multi-enemy turn queue):** Nếu có 3 quái cùng sống, chúng sẽ lần lượt tấn công theo chuỗi nhịp nhàng (có độ trễ 400ms giữa các đòn) kèm âm thanh riêng biệt, tránh xung đột animation.
3. **Chuyển giao 2 Phase của Boss Tối Thượng:** Khi HP Boss Phase 1 về 0, không được kích hoạt hàm `handleEnemyDefeated()`, mà phải kích hoạt hoạt ảnh chuyển Phase (`transformBossPhase2()`), nạp thanh máu Phase 2 và đổi sprite/tên quái.
4. **Kiểm tra kết thúc ải bầy quái:** Ải chỉ được xem là hoàn thành khi TẤT CẢ quái vật trong mảng `state.enemies` đều có `hp <= 0`.
5. **Cân bằng năng lượng Mana đối với chiêu AOE:** Chiêu AOE có uy lực quét bầy quái lớn nên chi phí MP và độ khó câu hỏi phải tương xứng để tránh người chơi spam chiêu lạm dụng.

---

## Sơ Đồ Cấu Trúc Toàn Bộ Chiến Dịch 8 Ải

```
[Màn Hình Menu]
      ↓
[Làng Tân Thủ Giả Kim] ➔ Hoàn thành 3 Nhiệm vụ ➔ [Chọn 4 Kỹ Năng / Deck]
      ↓
┌────────────────────────────────────────────────────────────────────────┐
│                        CHIẾN DỊCH 8 ẢI CHIẾN ĐẤU                      │
├────────────────────────────────────────────────────────────────────────┤
│ Ải 1: Slime Nhựa (Lv.1) - 1 Quái [Khởi động]                           │
│ Ải 2: Bầy Tiểu Slime Este (Lv.1) - 3 QUÁI [Tập luyện chiêu AOE!]      │
│ Ải 3: Sói Băng Dung Môi (Lv.2) - 1 Quái                                │
│ Ải 4: Thạch Quái Tráng Bạc (Lv.3) - 1 Quái                             │
│ Ải 5: Song Thủ Vệ Este (Lv.3) - 2 QUÁI TINH ANH [Hộ Vệ Axit & Ancol]  │
│ Ải 6: Hỏa Long Nhiệt Độ (Lv.4) - 1 Quái                                │
│ Ải 7: Chúa Tể Bóng Tối (Lv.5) - 1 Boss                                 │
│ Ải 8: 👑 ĐẠI MA VƯƠNG TRIGLYCERIDE [NIGHTMARE BOSS 2 GIAI ĐOẠN]        │
│       ├── Phase 1: Thân Thể Este Đa Chức (350 HP, Khiên Phản Sát)      │
│       └── Phase 2: Đại Ma Vương Biến Dị (500 HP, Cuồng Nộ + Vận Dụng) │
└────────────────────────────────────────────────────────────────────────┘
```

---

## Chi Tiết Các Nhiệm Vụ Triển Khai (Tasks)

---

### Task 1: Thiết Kế Giao Diện & Luồng Trạng Thái Làng Tân Thủ (`#villageScreen`)

**Mục tiêu:** Tạo giao diện Làng Tân Thủ với NPC Giáo Sư Hóa Học, bảng danh sách 3 nhiệm vụ nhập môn và nút tiến vào chiến trường.

**Files:**
- Sửa đổi: `index.html` (Thêm khối `<section id="villageScreen">` và CSS phong cách RPG làng cổ).
- Kiểm tra: Mở trình duyệt xem giao diện Làng Tân Thủ hiển thị đúng khi nhấn "Bắt Đầu" từ Menu.

**Interfaces:**
- Consumes: `state.playerName`, `state.playerClass`.
- Produces: `state.villageQuests = { readCodex: false, dummyDefeated: false, craftedEster: false }`, hàm `openVillageScreen()`, `checkVillageCompletion()`.

- [ ] **Bước 1: Viết mã HTML cho `#villageScreen`**
  - Khung hội thoại NPC: Đại Pháp Svr Lavoisier / Mendeleev chào đón tân thủ.
  - Bảng 3 nhiệm vụ tân thủ dạng thẻ (Quest Cards) với icon, mô tả và trạng thái (Chưa hoàn thành / Đã xong).
  - Nút "Xuất Quân Ra Tiền Tuyến" (mặc định mờ/disabled cho đến khi cả 3 nhiệm vụ đều có tick xanh).
- [ ] **Bước 2: Viết CSS cho Làng Tân Thủ**
  - Màu nền làng tân thủ ấm áp (màu gỗ cổ tích, ánh hoàng hôn giả kim: `radial-gradient(...)`).
  - Hiệu ứng huy hiệu nhiệm vụ lấp lánh khi hoàn thành.
  - Responsive mượt mà trên Mobile (1 cột thẻ) và Desktop (3 cột thẻ nằm ngang).
- [ ] **Bước 3: Cập nhật hàm chuyển cảnh**
  - Khi bấm `btnStartGame` ở Menu -> Chuyển sang `villageScreen` thay vì vào thẳng `battleScreen`.
  - Nếu người chơi đã từng vượt qua Làng Tân Thủ trong phiên trước (`localStorage.getItem("esterQuest_tutorialDone") === "true"`), hiển thị thêm nút phụ "Bỏ qua & Vào Thẳng Trận Đấu ➔".
- [ ] **Bước 4: Kiểm tra và Commit**
  ```bash
  git add index.html
  git commit -m "feat(village): scaffold novice village UI and transition logic"
  ```

---

### Task 2: Nhiệm Vụ 1 - Thụ Đắc Bí Kíp (Bắt Buộc Học Sổ Tay Ester)

**Mục tiêu:** Buộc người chơi phải mở Sổ Tay Bí Kíp và xem qua các mục cốt lõi (Khái niệm, Danh pháp, Lý tính, Hóa tính, Điều chế) để hoàn thành nhiệm vụ đầu tiên.

**Files:**
- Sửa đổi: `index.html` (Logic hàm `switchCodexTab`, `closeCodex`).

**Interfaces:**
- Consumes: Mảng các tab trong `#codexModal` (`overview`, `naming`, `physical`, `chemical`, `application`).
- Produces: `state.codexTabsViewed = Set<string>`, sự kiện hoàn thành `villageQuests.readCodex = true`.

- [ ] **Bước 1: Cơ chế ghi nhận tiến trình đọc Bí kíp**
  - Khởi tạo `state.codexTabsViewed = new Set()`.
  - Mỗi khi người chơi click chuyển qua một tab trong Codex, thêm ID tab đó vào Set.
  - Thêm thanh tiến trình nhỏ trên đầu modal Bí Kíp: `Tiến độ lĩnh hội: X / 5 mục`.
- [ ] **Bước 2: Hoàn thành nhiệm vụ khi đọc đủ 5 mục**
  - Khi `state.codexTabsViewed.size >= 5`, phát âm thanh `SFX.levelUp()` và hiện thông báo: "🎉 Bạn đã thấu suốt Bí Kíp Ester!".
  - Đánh dấu `state.villageQuests.readCodex = true`.
  - Thẻ Nhiệm Vụ 1 trong Làng Tân Thủ chuyển sang trạng thái "✅ ĐÃ LĨNH HỘI".
- [ ] **Bước 3: Tích hợp nút "Mở Bí Kíp Học Ngay" trực tiếp từ thẻ nhiệm vụ**
- [ ] **Bước 4: Kiểm tra và Commit**
  ```bash
  git add index.html
  git commit -m "feat(village): implement mandatory codex reading quest with tab tracking"
  ```

---

### Task 3: Nhiệm Vụ 2 - Thao Trường Ma Nơ Canh (Thực Hành Tấn Công Thử Nghiệm)

**Mục tiêu:** Tạo một trận đấu tập nhỏ với "Bù Nhìn Rơm Giả Kim" (Training Dummy) trong làng để người chơi làm quen với việc chọn chiêu thức và trả lời câu hỏi trắc nghiệm không áp lực mất máu.

**Files:**
- Sửa đổi: `index.html` (Thêm chế độ đấu tập Dummy trong `#dummyModal` hoặc arena thu nhỏ).

**Interfaces:**
- Consumes: Câu hỏi mức độ Nhận biết (Level 1) từ `QUESTION_BANK`.
- Produces: `state.villageQuests.dummyDefeated = true`.

- [ ] **Bước 1: Thiết kế giao diện Thao Trường Tập Luyện**
  - Đối thủ: 🎯 Bù Nhìn Rơm Giả Kim (HP: 60/60, Sát thương: 0, không đánh trả).
- [ ] **Bước 2: Cơ chế chiến đấu tập sự**
  - Người chơi chọn chiêu thức -> Trả lời câu hỏi -> Nếu đúng gây sát thương; nếu sai không bị trừ HP và được xem lời giải.
- [ ] **Bước 3: Kết thúc huấn luyện**
  - Khi HP Bù Nhìn về 0 -> Hoàn thành Nhiệm vụ 2, cập nhật huy hiệu thẻ nhiệm vụ.
- [ ] **Bước 4: Kiểm tra và Commit**
  ```bash
  git add index.html
  git commit -m "feat(village): add training dummy practice battle quest"
  ```

---

### Task 4: Nhiệm Vụ 3 - Thí Nghiệm Mini Điều Chế Este Chuối ($Isoamyl\ acetate$)

**Mục tiêu:** Cho người chơi tự tay thao tác thí nghiệm pha chế este đơn giản thông qua mini-game tương tác chọn hóa chất và điều kiện phản ứng.

**Files:**
- Sửa đổi: `index.html` (Thêm widget thí nghiệm mini `#labQuestModal`).

**Interfaces:**
- Consumes: Kiến thức phản ứng ester hóa $CH_3COOH + (CH_3)_2CHCH_2CH_2OH \overset{H_2SO_4\text{ đặc, } t^\circ}{\rightleftharpoons} CH_3COOCH_2CH_2CH(CH_3)_2 + H_2O$.
- Produces: `state.villageQuests.craftedEster = true`, thưởng thêm 1 Bình Nước Cất khởi đầu.

- [ ] **Bước 1: Giao diện Bàn Thí Nghiệm Giả Kim**
  - Hiển thị 1 ống nghiệm và 4 nhóm chọn: Axit ($CH_3COOH$), Ancol (Isoamylic), Xúc tác ($H_2SO_4$ đặc), Nhiệt độ ($t^\circ$).
- [ ] **Bước 2: Xử lý phản ứng và hiển thị kết quả**
  - Chọn đúng: Ống nghiệm tỏa bọt phát sáng, hoàn thành nhiệm vụ 3.
  - Chọn sai: Hiện lời giải thích hóa học và cho phép chọn lại.
- [ ] **Bước 3: Tốt Nghiệp Làng Tân Thủ**
  - Mở khóa nút "XUẤT QUÂN RA CHIẾN TRƯỜNG ➔", tặng thêm 1 Bình Nước Cất.
- [ ] **Bước 4: Kiểm tra và Commit**
  ```bash
  git add index.html
  git commit -m "feat(village): add ester synthesis mini-lab quest and graduation reward"
  ```

---

### Task 5: Nâng Cấp Động Cơ Chiến Đấu Đa Quái Vật (Multi-Enemy Battle Engine)

**Mục tiêu:** Nâng cấp sàn đấu hỗ trợ xuất hiện từ 1 đến 3 quái vật cùng lúc trên màn hình, hỗ trợ click chọn mục tiêu (`selectedTargetIndex`) và cơ chế lượt đánh của bầy quái.

**Files:**
- Sửa đổi: `index.html` (Cấu trúc HTML `.arena-container`, CSS `.enemy-group`, JavaScript `state.enemies`).

**Interfaces:**
- Consumes: Mảng `stage.enemies: Array<Enemy>` trong cấu hình Ải.
- Produces: `state.enemies`, `state.selectedTargetIndex`, hàm `selectTarget(idx)`, `renderEnemyGroup()`.

- [ ] **Bước 1: Cấu trúc dữ liệu và giao diện Nhóm Quái Vật (Enemy Group)**
  - Thay thế 1 thẻ quái đơn bằng container `<div class="enemies-container" id="enemiesContainer"></div>`.
  - Mỗi quái trong bầy có: Khung sprite riêng, thanh HP riêng, tên riêng và vòng tròn ngắm bắn (`target-reticle`) khi được chọn.
- [ ] **Bước 2: Cơ chế click đổi mục tiêu đánh đơn**
  - Người chơi click vào bất kỳ quái vật nào để đặt làm mục tiêu chính (`state.selectedTargetIndex = idx`).
  - Quái được chọn sẽ có viền sáng neon nhấp nháy. Mặc định tự động chọn quái đầu tiên còn sống.
- [ ] **Bước 3: Chuỗi phản công của bầy quái (`multiEnemyTurn`)**
  - Khi đến lượt đối thủ, các quái còn sống (`hp > 0`) sẽ lần lượt thi triển đòn đánh với độ trễ ngắn, tạo cảm giác bị bao vây chân thực.
  - Khiên Dung Môi của người chơi chặn được 1 đòn tấn công đầu tiên của bầy quái.
- [ ] **Bước 4: Kiểm tra và Commit**
  ```bash
  git add index.html
  git commit -m "feat(combat): implement multi-enemy group rendering and targeting system"
  ```

---

### Task 6: Kho Kỹ Năng Mới & Kỹ Năng Diện Rộng (AOE Spells System)

**Mục tiêu:** Mở rộng hệ thống chiêu thức với cả chiêu thức Đơn Mục Tiêu độc đáo (DoT, Hút sinh lực, Làm mù, Mana Burst) và **Chiêu Thức Diện Rộng (AOE)** để quét sạch bầy quái.

**Files:**
- Sửa đổi: `index.html` (`SKILL_DATABASE`, `resolveTurnAction`).

**Bảng Tổng Hợp Chiêu Thức Mở Rộng:**

| ID | Tên Chiêu Thức | Kiểu Đánh | MP | Sát Thương | Hiệu Ứng RPG Đặc Biệt | Mức Câu Hỏi |
|:---:|:---|:---:|:---:|:---:|:---|:---:|
| **1** | 🗡️ **Đòn Axit Cơ Bản** | Đơn | 0 | 35 ST | Hồi 10 MP nếu trả lời đúng | ⭐ Nhận Biết |
| **2** | 🔥 **Hỏa Cầu Este Hóa** | Đơn | 20 | 75 ST | Đòn phép công phá đơn mục tiêu | ⭐⭐ Thông Hiểu |
| **3** | 🛡️ **Khiên Dung Môi** | Hỗ trợ | 15 | +35 HP | Tạo khiên chặn đòn đánh tiếp theo | ⭐⭐ Thông Hiểu |
| **4** | ⚡ **Bão Xà Phòng Hóa** | Đơn | 35 | 150 ST | Gây sát thương cực lớn & Choáng quái 1 lượt | ⭐⭐⭐ Vận Dụng |
| **5** | 🌸 **Hương Hoa Độc Tố** | Đơn | 18 | 40 ST | **Gây độc (DoT):** Quái mất 15 HP/lượt trong 3 lượt | ⭐⭐ Thông Hiểu |
| **6** | 🧪 **Chiết Tách Dung Môi** | Đơn | 12 | 45 ST | **Hút máu:** Hồi phục 25 HP cho người chơi | ⭐⭐ Thông Hiểu |
| **7** | 🪞 **Tráng Bạc Quý Tộc** | Đơn | 22 | 65 ST | **Gây mù (Blind):** Đòn đánh kế tiếp của quái trượt 70% | ⭐⭐ Thông Hiểu |
| **8** | 💥 **Bùng Nổ Oxi Hóa** | Đơn | Toàn bộ | $MP \times 3.5$ | **Mana Burst:** Đốt toàn bộ MP gây sát thương dứt điểm | ⭐⭐⭐ Vận Dụng |
| **9** | 🌊 **Sóng Thủy Phân Toàn Thể** | **AOE** | 28 | 60 ST/quái | **Sát thương diện rộng:** Tấn công TẤT CẢ quái vật trên sân | ⭐⭐ Thông Hiểu |
| **10**| 🌪️ **Lốc Bão Nhiệt Đốt Cháy** | **AOE** | 42 | 95 ST/quái | **AOE Cực Đại:** Quét sạch toàn bộ quái & giảm 25% công của chúng | ⭐⭐⭐ Vận Dụng |

- [ ] **Bước 1: Tích hợp logic xử lý AOE trong `resolveTurnAction`**
  - Kiểm tra `skill.targetType === 'all'`:
    - Duyệt qua tất cả `state.enemies.filter(e => e.hp > 0)`.
    - Gây sát thương và hiển thị số nổi sát thương đồng loạt trên từng quái vật.
    - Phát hiệu ứng chớp sáng toàn sàn đấu (`arena-flash-aoe`).
- [ ] **Bước 2: Xử lý hiệu ứng trạng thái (DoT, Blind)**
  - Tích hợp đếm lượt độc và tính tỉ lệ trượt 70% khi quái bị mù.
- [ ] **Bước 3: Bảng Chọn 4 Kỹ Năng Ra Trận (Deck Loadout)**
  - Cho phép người chơi tự chọn 4 trong 10 chiêu thức để mang vào chiến trường.
- [ ] **Bước 4: Kiểm tra và Commit**
  ```bash
  git add index.html
  git commit -m "feat(skills): add AOE mass spells and expand skill registry to 10 chemical abilities"
  ```

---

### Task 7: Mở Rộng 8 Ải Chiến Đấu & Thiết Kế Boss Tối Thượng (Nightmare Super Boss)

**Mục tiêu:** Cấu hình chi tiết 8 Ải chiến đấu (bao gồm 2 ải nhiều quái) và thiết kế Màn 8 với Boss Tối Thượng 2 Phase có độ khó cực cao.

**Files:**
- Sửa đổi: `index.html` (Mảng `STAGES`, hàm `loadStage`, `transformBossPhase2`).

**Cấu hình chi tiết 8 Ải:**

1. **Ải 1: Rừng Ẩm Ướt** — 1 Quái: Slime Nhựa (`Lv.1`, HP: 100, ATK: 15).
2. **Ải 2: Đầm Lầy Bầy Nhầy (MỚI - 3 QUÁI):**
   - 3 Tiểu Slime: *Slime Formate* (HP: 60), *Slime Acetate* (HP: 70), *Slime Propionate* (HP: 80).
   - *Chiến thuật gợi ý:* Dùng chiêu AOE 🌊 **Sóng Thủy Phân** để quét sạch nhanh chóng!
3. **Ải 3: Thung Lũng Băng** — 1 Quái: Sói Băng (`Lv.2`, HP: 160, ATK: 24).
4. **Ải 4: Hầm Ngục Thạch** — 1 Quái: Thạch Quái Tráng Bạc (`Lv.3`, HP: 220, ATK: 30).
5. **Ải 5: Tháp Canh Đôi (MỚI - 2 QUÁI TINH ANH):**
   - 2 Quái: *Hộ Vệ Axit Carboxylic* (HP: 150, ATK: 22) & *Hộ Vệ Ancol Đơn Chức* (HP: 150, ATK: 22).
   - Hai hộ vệ tương trợ nhau nếu không diệt đồng thời!
6. **Ải 6: Tháp Địa Ngục** — 1 Quái: Hỏa Long Nhiệt Độ (`Lv.4`, HP: 280, ATK: 36).
7. **Ải 7: Điện Thờ Hắc Ám** — 1 Quái: Chúa Tể Bóng Tối (`Lv.5`, HP: 360, ATK: 42).
8. **Ải 8: VỰC THẲM HỖN MANG - ĐẠI CHIẾN ĐẠI MA VƯƠNG TRIGLYCERIDE (NIGHTMARE SUPER BOSS):**
   - **Giai Đoạn 1 (Phase 1):** *Thân Thể Este Đa Chức* (HP: 350, ATK: 45).
     - *Nội tại:* **Khiên Este Chắn Sát Thương** (Giảm 25% sát thương nhận vào).
     - Khi HP về 0: Màn hình rung chuyển dữ dội, âm thanh gầm rú, kích hoạt chuyển Phase!
   - **Giai Đoạn 2 (Phase 2):** *Đại Ma Vương Biến Dị Triglyceride* (HP: 500, ATK: 55).
     - *Nội tại:* **Cuồng Nộ Thủy Phân** (Cứ mỗi 2 lượt tăng 15% sức tấn công).
     - *Bộ câu hỏi:* Chỉ rút các câu hỏi thuộc mức độ **Vận Dụng Cao** (tính toán bảo toàn khối lượng este/chất béo, este phenol, phản ứng xà phòng hóa hỗn hợp).
     - Người chơi phải tính toán kỹ từng giọt Mana và từng bình hồi máu để chiến thắng!

- [ ] **Bước 1: Cập nhật mảng `STAGES` chứa đủ 8 Ải**
  - Cấu trúc hỗ trợ cả ải đơn mục tiêu lẫn ải nhiều quái `enemies: [...]`.
- [ ] **Bước 2: Xây dựng cơ chế chuyển Phase cho Boss Ải 8**
  - Viết hàm `triggerBossPhase2()`:
    - Hiệu ứng rung lắc màn hình cực mạnh, đổi màu nền arena sang đỏ rực u ám.
    - Đổi tên Boss thành "👑 ĐẠI MA VƯƠNG TRIGLYCERIDE BIẾN DỊ (PHASE 2)".
    - Đổi icon/sprite sang hình tượng quái vật hung hãn và nạp đầy cây máu 500 HP.
- [ ] **Bước 3: Ngân hàng đề riêng cho Boss Ải 8**
  - Đảm bảo các câu hỏi của Ải 8 đều là câu hỏi Vận Dụng mang tính thách thức cao.
- [ ] **Bước 4: Kiểm tra và Commit**
  ```bash
  git add index.html
  git commit -m "feat(stages): expand to 8 stages with multi-mob encounters and 2-phase nightmare super boss"
  ```

---

### Task 8: Kiểm Thử Toàn Diện, Responsive & Hoàn Thiện Tài Liệu

**Mục tiêu:** Kiểm tra toàn diện mọi tính năng từ Làng Tân Thủ, Chiêu AOE, Ải Bầy Quái đến Boss 2 Phase trên cả Desktop, Tablet và Mobile.

**Files:**
- Sửa đổi: `index.html`, `README.md`.
- Script kiểm tra: `tests/verify_full_features.py`.

- [ ] **Bước 1: Viết script Python tự động kiểm tra logic**
  - Kiểm tra tính toán sát thương AOE, danh sách 8 ải, logic 2 Phase của Boss.
- [ ] **Bước 2: Kiểm tra Responsive sàn đấu bầy quái**
  - Đảm bảo 3 quái vật trên điện thoại di động hiển thị ngay ngắn, không bị che khuất thanh kỹ năng hoặc HUD máu.
- [ ] **Bước 3: Cập nhật `README.md`**
  - Hướng dẫn chế độ Làng Tân Thủ, danh sách 10 chiêu thức (bao gồm chiêu AOE), và chiến thuật vượt Boss Ải 8.
- [ ] **Bước 4: Commit và đẩy lên GitHub**
  ```bash
  git add .
  git commit -m "docs: complete implementation plan with multi-enemy AOE combat and nightmare boss"
  git push origin main
  ```

---

## Trạng Thái & Xác Nhận Bắt Đầu

Kế hoạch toàn diện đã bao gồm:
1. **Làng Tân Thủ** bắt buộc học bí kíp & làm 3 nhiệm vụ nhập môn.
2. **Chiến Dịch 8 Ải**, trong đó có 2 ải xuất hiện nhiều quái vật (Ải 2 có 3 quái, Ải 5 có 2 quái).
3. **2 Chiêu Thức Diện Rộng (AOE)** công phá toàn bộ đối thủ (`targetType: 'all'`).
4. **Màn Boss Tối Thượng (Ải 8)** độ khó cực cao với 2 Phase biến dị và câu hỏi Vận Dụng Cao.

Khi bạn xem qua và cảm thấy hài lòng, hãy phản hồi để chúng ta bắt đầu tiến hành code theo kế hoạch này!
