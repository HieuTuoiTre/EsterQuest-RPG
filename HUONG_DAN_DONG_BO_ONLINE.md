# ☁️ HƯỚNG DẪN KẾT NỐI BẢNG XẾP HẠNG ONLINE (GOOGLE SHEETS)

> **Mục tiêu:** Giúp học sinh dù chơi game trên bất kỳ điện thoại hay máy tính nào cũng đồng bộ chung một Bảng Xếp Hạng toàn trường, và toàn bộ điểm số sẽ tự động lưu về một file **Google Sheet** của bạn để dễ dàng theo dõi, thống kê.
>
> 💡 **Ưu điểm:** Miễn phí 100%, không cần thuê máy chủ hay mua tên miền, chạy vĩnh viễn trên hạ tầng của Google.

---

## 🛠️ CÁCH THIẾT LẬP (CHỈ MẤT 2 PHÚT)

### Bước 1: Tạo Google Sheet mới
1. Mở [Google Sheets (Trang tính)](https://sheets.new) trên trình duyệt của bạn.
2. Đặt tên bảng tính là: `Dữ Liệu Điểm - Ester Quest`.
3. Ở hàng đầu tiên (Dòng 1), đặt tên các cột lần lượt như sau:
   * **Cột A:** `Thời gian`
   * **Cột B:** `Tên Hiệp Sĩ`
   * **Cột C:** `Lớp`
   * **Cột D:** `Điểm Số`
   * **Cột E:** `Số Câu Đúng`
   * **Cột F:** `Tổng Số Câu`
   * **Cột G:** `Độ Chính Xác (%)`
   * **Cột H:** `Tiến Trình Ải`

---

### Bước 2: Dán mã Google Apps Script
1. Trên thanh công cụ của Google Sheet, chọn: **Tiện ích mở rộng** (Extensions) ➔ **Apps Script**.
2. Xóa hết tất cả code mặc định đang có, và **dán toàn bộ đoạn code dưới đây** vào:

```javascript
function doPost(e) {
  try {
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    var data = JSON.parse(e.postData.contents);
    sheet.appendRow([
      new Date(),
      data.name || "Ẩn danh",
      data.lop || "12A",
      Number(data.score) || 0,
      Number(data.correct) || 0,
      Number(data.total) || 0,
      Number(data.accuracy) || 0,
      data.stage || ""
    ]);
    return ContentService.createTextOutput(JSON.stringify({ ok: true }))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({ ok: false, error: err.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

function doGet(e) {
  try {
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    var rows = sheet.getDataRange().getValues();
    var list = [];
    for (var i = 1; i < rows.length; i++) {
      if (!rows[i][1]) continue;
      list.push({
        date: Utilities.formatDate(new Date(rows[i][0]), "GMT+7", "HH:mm dd/MM"),
        name: String(rows[i][1]),
        lop: String(rows[i][2]),
        score: Number(rows[i][3]) || 0,
        correct: Number(rows[i][4]) || 0,
        total: Number(rows[i][5]) || 0,
        accuracy: Number(rows[i][6]) || 0,
        stage: String(rows[i][7]),
        isWin: String(rows[i][7]).indexOf("Phá Đảo") !== -1
      });
    }
    // Sắp xếp điểm cao nhất lên đầu
    list.sort(function(a, b) { return b.score - a.score; });
    return ContentService.createTextOutput(JSON.stringify({ ok: true, list: list }))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({ ok: false, list: [] }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}
```

3. Nhấn biểu tượng 💾 **Lưu dự án** (Ctrl + S).

---

### Bước 3: Xuất bản Web App (Lấy đường dẫn URL)
1. Ở góc trên bên phải màn hình Apps Script, bấm vào nút màu xanh **Triển khai** (Deploy) ➔ Chọn **Tùy chọn triển khai mới** (New deployment).
2. Nhấn vào biểu tượng bánh răng ⚙️ bên cạnh "Chọn loại", chọn **Ứng dụng web** (Web app).
3. Thiết lập 3 mục sau:
   * **Mô tả:** `Ester Quest Leaderboard API`
   * **Thực thi dưới dạng (Execute as):** `Tôi (email của bạn)`
   * **Ai có quyền truy cập (Who has access):** Chọn **Bất kỳ ai (Anyone)** *(Rất quan trọng để học sinh gửi điểm không cần đăng nhập Google!)*
4. Nhấn **Triển khai** (Deploy) ➔ Nếu Google hỏi cấp quyền (Authorize access), hãy chọn tài khoản của bạn ➔ Chọn *Nâng cao (Advanced)* ➔ Chọn *Đi tới dự án (Go to project)* ➔ Bấm *Cho phép (Allow)*.
5. Sau khi triển khai xong, bạn sẽ nhận được một đường link **URL của ứng dụng web** có dạng:
   ```text
   https://script.google.com/macros/s/AKfycbx.../exec
   ```
6. Bấm **Sao chép** đường link này!

---

### Bước 4: Dán đường link vào Game

Bạn có 2 cách cực kỳ đơn giản để kích hoạt:

#### Cách 1: Thao tác trực tiếp ngay trên giao diện Web Game (Khuyên dùng)
1. Mở file `index.html` trên trình duyệt.
2. Bấm vào nút **🏆 Bảng Xếp Hạng & Lịch Sử**.
3. Bấm vào nút **⚙️ Kết nối Online**.
4. Dán link Google Apps Script bạn vừa sao chép vào ô và bấm **LƯU LINK**.
5. Đèn trạng thái sẽ chuyển thành `🟢 Online (x lượt chơi toàn trường)`.

#### Cách 2: Gắn vĩnh viễn vào mã nguồn để học sinh mở web lên là có sẵn
* Mở file `index.html` bằng Notepad/VS Code, tìm dòng code số ~550:
  ```javascript
  let GOOGLE_SHEET_API = "";
  ```
* Dán link vào giữa cặp dấu `""`, ví dụ:
  ```javascript
  let GOOGLE_SHEET_API = "https://script.google.com/macros/s/AKfycbx.../exec";
  ```
* Lưu file lại. Giờ đây khi bạn đưa web lên Netlify hoặc GitHub Pages, tất cả máy tính và điện thoại của học sinh sẽ tự động kết nối chung một máy chủ bảng xếp hạng!
