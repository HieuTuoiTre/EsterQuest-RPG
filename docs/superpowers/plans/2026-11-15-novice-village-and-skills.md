# Kế Hoạch Triển Khai: Làng Tân Thủ & Hệ Thống Kỹ Năng Mới (PLAN.MD)

> **Dành cho kỹ sư / Agent triển khai:** BẮT BUỘC SỬ DỤNG SUB-SKILL: `superpowers:subagent-driven-development` (khuyên dùng) hoặc `superpowers:executing-plans` để thực thi từng nhiệm vụ theo thứ tự. Các bước sử dụng cú pháp checkbox (`- [ ]`) để theo dõi tiến độ.

**Mục tiêu (Goal):** Xây dựng phân đoạn "Làng Tân Thủ Giả Kim" (Novice Village / Academy) bắt buộc người chơi phải tìm hiểu Bí Kíp Ester và hoàn thành các thử thách nhập môn trước khi ra trận, đồng thời mở rộng kho chiêu thức chiến đấu với các cơ chế RPG turn-based độc đáo (Độc dược DoT, Hút sinh lực Drain, Gây mù Blind, Nổ tung Mana Burst).

**Kiến trúc (Architecture):** Bổ sung màn hình trung gian `#villageScreen` giữa `#menuScreen` và `#battleScreen`; tích hợp cơ chế theo dõi tiến độ nhiệm vụ tân thủ lưu vào `localStorage`; mở rộng động cơ kỹ năng chiến đấu (`SKILL_REGISTRY`) hỗ trợ hiệu ứng trạng thái (Status Effects: DoT, Blind, Stun) và bộ chọn kỹ năng (Skill Loadout Deck 4 ô).

**Công nghệ (Tech Stack):** Pure Vanilla JavaScript (ES6+), HTML5, CSS3 (CSS Grid/Flexbox, Keyframe Animations, Pixelated Rendering), Web Audio API Synthesizers.

**Tài liệu đặc tả (Spec):** Yêu cầu từ người dùng: (1) Bắt buộc học bí kíp & làm nhiệm vụ nhỏ tại Làng Tân Thủ trước khi vào đánh quái; (2) Thiết kế các chiêu thức mới lạ, đậm chất RPG và kiến thức hóa học; (3) Lưu kế hoạch vào `PLAN.MD`.

---

## Ràng Buộc Toàn Cục (Global Constraints)

1. **Không cài thêm thư viện bên ngoài:** Toàn bộ ứng dụng chạy thuần trên một trang duy nhất (`index.html`) kèm tài nguyên ảnh trong thư mục `assets/`.
2. **Đáp ứng đa thiết bị (Responsive Design):** Màn hình Làng Tân Thủ và các bảng kỹ năng mới phải hoạt động chuẩn trên Desktop, Tablet (768px) và Mobile (<= 480px, chạm tối thiểu 44x44px).
3. **Bảo toàn dữ liệu cũ:** Giữ nguyên ngân hàng 68 câu hỏi trắc nghiệm, 5 Ải chiến đấu và cơ chế âm thanh Web Audio API hiện tại.
4. **Cơ chế lưu trạng thái thông minh:** Người chơi đã hoàn thành Làng Tân Thủ một lần sẽ có tùy chọn "Vào Thẳng Chiến Trường" ở các lần chơi sau, hoặc có thể chọn "Học Lại Tân Thủ" bất kỳ lúc nào.

---

## Tiêu Điểm Đánh Giá Rủi Ro (Review Focus)

1. **Hiệu ứng Trúng Độc (DoT) kết liễu quái:** Khi sát thương độc rút hết HP của quái vật vào đầu hoặc cuối lượt, hệ thống phải kích hoạt chiến thắng ải ngay lập tức, không để quái vật phản công trong trạng thái 0 HP.
2. **Hút Máu / Hút Mana vượt ngưỡng (Over-drain):** Chiêu thức hút máu/mana từ quái vật phải được chặn chặn trên bằng `Math.min(maxVal, currentVal + gain)` để không gây lỗi vỡ thanh hiển thị UI.
3. **Thời gian tồn tại của trạng thái Mù (Blind):** Khi quái vật bị mù, đòn đánh kế tiếp của quái có tỉ lệ trượt 70%. Dù đánh trúng hay trượt, trạng thái Mù phải được giải trừ sau lượt đó, không kéo dài vĩnh viễn.
4. **Bỏ qua nhiệm vụ bằng console / DOM:** Nút "Xuất Quân Ra Chiến Trường" phải bị vô hiệu hóa (`disabled`) cả về giao diện lẫn logic chặn trong hàm `startBattleFromVillage()`, ngăn người chơi vượt ải tân thủ khi chưa hoàn thành 3 nhiệm vụ.
5. **Đồng bộ hóa 4 ô kỹ năng kích hoạt (Skill Deck):** Khi người chơi đổi chiêu thức trong Làng Tân Thủ, thanh kỹ năng chiến đấu trong trận phải cập nhật đúng icon, tên chiêu, lượng MP và độ khó câu hỏi tương ứng.

---

## Chi Tiết Các Nhiệm Vụ Triển Khai (Tasks)

```
[Màn Hình Menu] ➔ [Làng Tân Thủ Giả Kim] ➔ [Chọn 4 Kỹ Năng] ➔ [Chiến Trường 5 Ải]
                      ├── Nhiệm vụ 1: Thụ Đắc Bí Kíp (Đọc 5 tab)
                      ├── Nhiệm vụ 2: Thao Trường Ma Nơ Canh (Tập đánh 2 câu)
                      └── Nhiệm vụ 3: Pha Chế Este Chuối (Thí nghiệm mini)
```

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
  - Khung hội thoại NPC: Đại Pháp Sư Lavoisier / Mendeleev chào đón tân thủ.
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
  - Chạy lệnh kiểm tra cú pháp và commit:
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
  - Giúp người chơi mới không phải tự mò nút trên thanh Header mà có thể bấm trực tiếp từ bảng nhiệm vụ làng.
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
  - Hướng dẫn tương tác nổi bật: "Hãy thử dùng Đòn Axit Cơ Bản hoặc Hỏa Cầu để tấn công Bù Nhìn!".
- [ ] **Bước 2: Cơ chế chiến đấu tập sự**
  - Người chơi chọn chiêu thức -> Hiện câu hỏi trắc nghiệm mức độ Nhận Biết.
  - Nếu trả lời đúng: Gây sát thương lên bù nhìn, cộng điểm và tạo hiệu ứng âm thanh sống động.
  - Nếu trả lời sai: Bù nhìn nhắc nhở lời giải chi tiết, không trừ máu người chơi và cho phép thử lại.
- [ ] **Bước 3: Kết thúc huấn luyện**
  - Khi HP Bù Nhìn về 0 -> Bù nhìn vỡ tung hoa tuyết, hoàn thành Nhiệm vụ 2.
  - Cập nhật thẻ Nhiệm Vụ 2: "✅ THAO TRƯỜNG TỐT NGHIỆP".
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
  - Hiển thị 1 ống nghiệm / bình cầu đáy tròn và 4 nhóm lựa chọn:
    1. Axit hữu cơ: $CH_3COOH$ (Axit axetic) vs $HCOOH$ vs $HCl$.
    2. Ancol: Ancol isoamylic vs Ancol etylic vs Glixerol.
    3. Chất xúc tác: $H_2SO_4$ đặc vs $HCl$ loãng vs $NaOH$.
    4. Điều kiện nhiệt độ: Đun cách thủy / Đun sôi nhẹ vs Làm lạnh đá.
- [ ] **Bước 2: Xử lý phản ứng và hiển thị kết quả**
  - Khi người chơi chọn đúng ($CH_3COOH$ + Ancol isoamylic + $H_2SO_4$ đặc + Đun nóng nhẹ):
    - Ống nghiệm phát sáng hiệu ứng sủi bọt, tỏa hương chuối chín ngọt ngào!
    - Hoàn thành nhiệm vụ 3.
  - Nếu chọn sai: Hiện phản hồi giải thích tại sao cần $H_2SO_4$ đặc (vừa làm xúc tác vừa hút nước chuyển dịch cân bằng) và cho chọn lại.
- [ ] **Bước 3: Lễ Tốt Nghiệp Làng Tân Thủ**
  - Khi hoàn thành cả 3 nhiệm vụ:
    - Kích hoạt nút "XUẤT QUÂN RA CHIẾN TRƯỜNG ➔".
    - Mở khóa danh hiệu: "🎖️ Giả Kim Sĩ Chính Thức".
    - Tặng thêm 1 Bình Nước Cất khởi đầu (tổng cộng có 3 bình).
    - Lưu `localStorage.setItem("esterQuest_tutorialDone", "true")`.
- [ ] **Bước 4: Kiểm tra và Commit**
  ```bash
  git add index.html
  git commit -m "feat(village): add ester synthesis mini-lab quest and graduation reward"
  ```

---

### Task 5: Thiết Kế & Xây Dựng 4 Chiêu Thức Mới Lạ (Combat Spells Expansion)

**Mục tiêu:** Mở rộng kho kỹ năng chiến đấu từ 4 chiêu lên 8 chiêu độc đáo, kết hợp sâu sắc giữa tính chất hóa học và cơ chế RPG (DoT, Hút sinh lực, Làm mù, Mana Burst).

**Files:**
- Sửa đổi: `index.html` (Mở rộng cấu trúc `SKILL_DATABASE`, logic hàm `resolveTurnAction`, hiệu ứng trạng thái trong `enemyTurn`).

**Danh sách 4 chiêu thức mới:**

| STT | Tên Chiêu Thức | MP | Sát Thương | Hiệu Ứng RPG Đặc Biệt | Cơ Sở Hóa Học | Mức Độ |
|:---:|:---|:---:|:---:|:---|:---|:---:|
| **5** | 🌸 **Hương Hoa Độc Tố** *(Aroma Poison)* | 18 | 40 ST | **Gây độc (DoT):** Quái mất 15 HP mỗi lượt trong 3 lượt tiếp theo. | Este có mùi thơm hoa quả nhưng nồng độ cao gây ngạt/choáng | ⭐⭐ Thông Hiểu |
| **6** | 🧪 **Chiết Tách Dung Môi** *(Solvent Drain)* | 12 | 45 ST | **Hút tài nguyên:** Hút 25 HP hoặc 15 MP từ quái vật về cho bản thân. | Chiết este nhẹ hơn nước nổi lên trên dung dịch muối ăn | ⭐⭐ Thông Hiểu |
| **7** | 🪞 **Tráng Bạc Quý Tộc** *(Silver Mirror)* | 22 | 65 ST | **Gây Mù (Blind):** Đòn đánh kế tiếp của quái vật có **70% tỉ lệ trượt** (Miss). | Phản ứng tráng bạc của este fomic ($HCOOR$) tạo gương sáng chói | ⭐⭐ Thông Hiểu |
| **8** | 💥 **Bùng Nổ Oxi Hóa** *(Combustion Burst)* | Toàn bộ (min 30) | $MP \times 3.5$ ST | **Mana Burst:** Đốt sạch toàn bộ Mana hiện có để gây sát thương hủy diệt ($50\text{ MP} \rightarrow 175\text{ ST}$). | Phản ứng đốt cháy hoàn toàn este tỏa lượng nhiệt cực lớn | ⭐⭐⭐ Vận Dụng |

- [ ] **Bước 1: Mở rộng State lưu trữ hiệu ứng chiến đấu**
  - Bổ sung vào `state`:
    ```javascript
    state.enemyStatusEffects = {
      poisonDuration: 0, // số lượt độc còn lại
      poisonDmg: 0,      // sát thương độc mỗi lượt
      blind: false       // có đang bị lóa mắt/mù không
    };
    ```
- [ ] **Bước 2: Cập nhật hàm giải quyết chiêu thức (`resolveTurnAction`)**
  - Chiêu 5 (Hương Hoa Độc Tố): Trừ 18 MP, gây 40 ST, kích hoạt `poisonDuration = 3`, `poisonDmg = 15`.
  - Chiêu 6 (Chiết Tách Dung Môi): Trừ 12 MP, gây 45 ST, hồi `Math.min(playerMaxHp, playerHp + 25)`.
  - Chiêu 7 (Tráng Bạc Quý Tộc): Trừ 22 MP, gây 65 ST, kích hoạt `state.enemyStatusEffects.blind = true`.
  - Chiêu 8 (Bùng Nổ Oxi Hóa): Tiêu hao toàn bộ `state.playerMana`, tính sát thương $= \text{spentMana} \times 3.5$.
- [ ] **Bước 3: Xử lý hiệu ứng trong lượt của quái vật (`enemyTurn`)**
  - **Xử lý Độc (DoT):** Đầu lượt quái, nếu `poisonDuration > 0`: Trừ máu quái, hiện số nổi xanh lục `-15 HP (Độc 🧪)`. Nếu quái chết vì độc -> Gọi `handleEnemyDefeated()`.
  - **Xử lý Mù (Blind):** Khi quái tấn công, nếu `blind === true`: Quay số ngẫu nhiên 70%. Nếu trượt: Hiện chữ nổi `TRƯỢT (MISS)! 💨`, người chơi không nhận sát thương, sau đó giải trừ trạng thái mù `blind = false`.
- [ ] **Bước 4: Kiểm tra và Commit**
  ```bash
  git add index.html
  git commit -m "feat(combat): implement 4 new chemical spells with DoT, drain, blind, and burst mechanics"
  ```

---

### Task 6: Hệ Thống Chọn 4 Kỹ Năng Ra Trận (Active Skill Deck Loadout)

**Mục tiêu:** Cho phép người chơi tự do lựa chọn 4 trong số 8 chiêu thức để mang vào trận đấu (Deck Building RPG).

**Files:**
- Sửa đổi: `index.html` (Modal / Panel chọn kỹ năng trong Làng Tân Thủ và trước mỗi Ải đấu).

**Interfaces:**
- Consumes: Danh sách 8 kỹ năng từ `SKILL_DATABASE`.
- Produces: `state.activeSkills = [id1, id2, id3, id4]`, hàm `renderActiveSkills()`.

- [ ] **Bước 1: Giao diện Bảng Kỹ Năng (Grimoire Deck)**
  - Hiển thị kho 8 thẻ kỹ năng với đầy đủ thông số: Tên, icon, lượng MP, mô tả hiệu ứng, độ khó câu hỏi tương ứng.
  - Khung 4 ô kích hoạt (Active Slots): Người chơi có thể bấm vào thẻ để trang bị hoặc tháo gỡ.
- [ ] **Bước 2: Thiết lập cấu hình mặc định & Lưu trữ**
  - Mặc định khởi đầu: 4 chiêu truyền thống (Đòn Axit, Hỏa Cầu, Khiên Dung Môi, Bão Xà Phòng).
  - Có nút "Đổi Chiêu Nhanh" ngay trước khi vào trận chiến.
- [ ] **Bước 3: Hiển thị động 4 chiêu trên Dashboard giao chiến**
  - Thay thế 4 nút cứng cũ bằng vòng lặp `state.activeSkills.map(...)` để render đúng 4 chiêu mà người chơi đã trang bị.
- [ ] **Bước 4: Kiểm tra và Commit**
  ```bash
  git add index.html
  git commit -m "feat(loadout): implement 4-slot skill loadout system for tactical customization"
  ```

---

### Task 7: Kiểm Thử Toàn Diện, Responsive & Hoàn Thiện

**Mục tiêu:** Kiểm tra trơn tru toàn bộ luồng chơi từ Menu -> Làng Tân Thủ -> 3 Nhiệm vụ -> Chọn Chiêu -> Chiến Đấu 5 Ải -> Chiến Thắng.

**Files:**
- Sửa đổi: `index.html`, `README.md`.
- Kiểm thử tự động: `tests/verify_gameplay.py` (Script python mô phỏng logic và kiểm tra DOM/cú pháp JS).

- [ ] **Bước 1: Viết script Python xác thực logic cú pháp**
  - Đảm bảo không có lỗi cú pháp JS, regex trích xuất đầy đủ 8 kỹ năng, 3 nhiệm vụ làng tân thủ, và các hàm điều hướng.
- [ ] **Bước 2: Kiểm tra Responsive trên các độ phân giải**
  - Màn hình Desktop (1920x1080 & 1366x768).
  - Màn hình Tablet iPad (768px - 1024px).
  - Màn hình Mobile iPhone / Android (375px - 414px - 480px).
- [ ] **Bước 3: Cập nhật tài liệu hướng dẫn (`README.md`)**
  - Giới thiệu khu vực Làng Tân Thủ.
  - Bảng tra cứu 8 chiêu thức giả kim thuật và mẹo phối hợp chiêu (Combo chiến thuật: Mù + Bão Xà Phòng; Độc DoT + Khiên phòng thủ).
- [ ] **Bước 4: Commit và đẩy lên GitHub**
  ```bash
  git add .
  git commit -m "docs: finalize novice village tutorial and new combat mechanics documentation"
  git push origin main
  ```

---

## Tóm Tắt Kế Hoạch & Các Bước Tiếp Theo

Kế hoạch này phân tách công việc thành **7 nhiệm vụ độc lập, tuần tự và khép kín**:
1. **Nhiệm vụ 1-4:** Xây dựng trọn vẹn Làng Tân Thủ & 3 thử thách học bí kíp thực hành.
2. **Nhiệm vụ 5-6:** Mở rộng hệ thống chiến đấu với 4 chiêu thức độc đáo và cơ chế chọn 4 chiêu mang vào trận.
3. **Nhiệm vụ 7:** Kiểm thử toàn diện và cập nhật tài liệu.

File kế hoạch đã được ghi lại tại `PLAN.MD`. Bạn hãy xem qua và cho biết các ý tưởng bổ sung tiếp theo để hoàn thiện kế hoạch trước khi bắt tay vào code nhé!
