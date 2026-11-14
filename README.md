# ⚔️ Ester Quest: Hiệp Sĩ Giả Kim & Đại Chiến Thủy Phân

Web game nhập vai chiến thuật theo lượt (Turn-based RPG) lồng ghép 100% kiến thức trọng tâm **Hóa học Lớp 12 - Chuyên đề 1: ESTER**.

---

## 🎮 Cách Khởi Chạy Game

Game được đóng gói hoàn toàn trong file `index.html` (chạy độc lập, không cần cài đặt Node.js hay bất kỳ server nào).

### Cách 1: Chơi trực tiếp trên máy (Offline)
* Click đúp trực tiếp vào file [`index.html`](./index.html) để mở trên trình duyệt (Google Chrome, Microsoft Edge, Cốc Cốc, Safari...).
* Hoạt động 100% mượt mà ngay cả khi không có kết nối Internet!

### Cách 2: Đưa lên mạng miễn phí (Netlify / GitHub Pages / Vercel)
* **Netlify:** Kéo thả thư mục `EsterQuest-RPG` vào [Netlify Drop](https://app.netlify.com/drop) là có ngay link web chia sẻ cho học sinh chơi.
* **GitHub Pages:** Đẩy thư mục này lên GitHub Repo và bật *Settings -> Pages*.

---

## 🛡️ Hệ Thống Trò Chơi (Gameplay Mechanics)

### 1. Điều Hướng Nhanh (Navigation)
* **Về Trang Chủ:** Nhấp trực tiếp vào biểu tượng/dòng chữ **⚔️ ESTER QUEST** ở góc trên bên trái bất kỳ lúc nào để quay về màn hình chính.
* **🏆 Bảng Xếp Hạng & Lịch Sử:** Nút ở thanh điều hướng trên cùng cho phép mở bảng vinh danh và lịch sử thi đấu bất kỳ lúc nào.

### 2. Hệ Thống Lưu Trữ Lịch Sử & Bảng Xếp Hạng (Leaderboard)
Game hỗ trợ 2 cơ chế lưu trữ giống hệt trang mẫu:
* **Mặc định (Offline / LocalStorage):** Tự động lưu trữ tên, lớp, điểm số, tỉ lệ đúng và thời gian thi đấu vào trình duyệt của học sinh. Dù tắt máy hay tải lại trang, lịch sử vẫn được giữ nguyên. Có bộ lọc theo từng Lớp học.
* **Đồng bộ toàn trường (Online qua Google Sheets - Dành cho Giáo viên):**
  * Trong file `index.html` có biến:
    ```javascript
    const GOOGLE_SHEET_API = "";
    ```
  * Giáo viên chỉ cần tạo 1 Google Apps Script kết nối Google Sheet và dán URL vào biến này. Khi học sinh hoàn thành trận đấu, điểm số sẽ tự động gửi thẳng về Google Sheet của giáo viên để thống kê và xếp hạng tự động!

### 3. Cốt truyện & 5 Ải Thử Thách
1. **Ải 1: Rừng Danh Pháp & Mùi Hương** - Quái vật: *Slime Formate* (Thử thách công thức este no đơn hở, danh pháp gốc R-COO-R', các mùi chuối/nhài/dứa).
2. **Ải 2: Thung Lũng Nhiệt Độ & Liên Kết** - Quái vật: *Sói Băng Hydrogen* (So sánh nhiệt độ sôi Acid > Alcohol > Ester, độ tan trong nước).
3. **Ải 3: Hầm Ngục Thủy Phân & Đồng Phân** - Quái vật: *Thạch Quái NaOH Kiềm* (Phản ứng thủy phân 1 chiều, số đồng phân C3H6O2, C4H8O2, este sinh aldehyde).
4. **Ải 4: Tháp Điều Chế & Hiệu Suất** - Quái vật: *Hỏa Long H2SO4 Đặc* (Phản ứng este hóa, tính háo nước, bài toán hiệu suất phản ứng).
5. **Ải 5 (TRÙM CUỐI): Bạo Chúa Ester Đa Chức** - Ma Vương: *Chúa Tể PolyEster Vận Dụng* (Este của phenol tác dụng NaOH tỉ lệ 1:2 sinh 2 muối, este đa chức, bài toán tổng hợp).

### 4. Bộ Chiêu Thức Nhập Vai (Gắn liền với độ khó câu hỏi)
* 🗡️ **Đòn Axit Cơ Bản (0 MP):** Câu hỏi mức độ **Nhận biết**. Đúng gây 35 Sát thương + Hồi 10 MP.
* 🔥 **Hỏa Cầu Este Hóa (20 MP):** Câu hỏi mức độ **Thông hiểu**. Đúng gây 75 Sát thương thiêu đốt.
* 🛡️ **Khiên Dung Môi (15 MP):** Câu hỏi mức độ **Thông hiểu**. Đúng tạo khiên chặn đòn đánh tiếp theo của quái và hồi 35 HP.
* ⚡ **Bão Xà Phòng Hóa (35 MP):** Câu hỏi mức độ **Vận dụng**. Đúng gây 150 Sát thương cực lớn và làm **Choáng (Stun)** quái vật 1 lượt!

### 5. Trang Bị & Trợ Giúp Trong Trận
* 🧪 **Bình Nước Cất:** Hồi 45 HP ngay lập tức không cần trả lời câu hỏi.
* 💧 **Xúc Tác H2SO4 Đặc:** Dùng trong câu hỏi để mở gợi ý tư duy và loại bỏ phương án sai (trợ giúp 50/50).
* 📖 **Sổ Tay Bí Kíp (Codex):** Mở ra tra cứu tóm tắt toàn bộ lý thuyết Este ngay trong trận đấu.
* 📝 **Nhật Ký Đấu Trí (Review):** Sau trận đấu có thể xem lại chi tiết tất cả câu đúng/sai kèm lời giải tường tận.
