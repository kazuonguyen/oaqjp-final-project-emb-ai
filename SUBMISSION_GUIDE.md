# Hướng dẫn nộp Final project — Emotion Detector

Đã hoàn thành mã nguồn và thu đủ bằng chứng cho 16 mục trong rubric.

## Kết quả đã xác minh

- Fork công khai: https://github.com/kazuonguyen/oaqjp-final-project-emb-ai
- README có đúng tên `Final project` theo hướng dẫn khóa học.
- Tasks 2–4: đã chạy với Watson thật trong Skills Network Theia Lab.
- Task 5: cả 5 bài kiểm thử gọi Watson thật đều pass (0.631 giây).
- Kiểm thử bổ sung: 11 kiểm thử logic/Flask offline đều pass.
- Task 8: Pylint đạt **10.00/10** trong Theia, không tắt kiểm tra.
- Task 6: đã chụp `6b_deployment_test.png` với đúng câu
  `I think I am having fun`, kết quả cảm xúc trội `joy`.
- Task 7: đã chụp `7c_error_handling_interface.png` trong Theia,
  hiển thị `Invalid text! Please try again!` sau khi phân tích input trống.
- Các log giữ nguyên đầu ra thực tế, kèm thời gian và exit status.

## Cách nộp

1. Mở `SUBMISSION_ANSWERS.md`. Từng mục đã được sắp theo rubric.
2. Dán URL/code/terminal output vào câu hỏi tương ứng trên Mark.
3. Upload hai ảnh PNG trong thư mục `evidence/` ở Tasks 6 và 7.
4. Kiểm tra lại các câu trả lời rồi tự gửi bài theo quy định khóa học.

Bài chưa được gửi trên Mark; bộ tài liệu này đã sẵn sàng để bạn xem và nộp.

## Hai URL cần nộp

Task 1:
https://github.com/kazuonguyen/oaqjp-final-project-emb-ai/blob/main/README.md

Task 4 Activity 1:
https://github.com/kazuonguyen/oaqjp-final-project-emb-ai/blob/main/EmotionDetection/__init__.py

## Chạy lại trong Theia khi cần

API chỉ truy cập được trong Theia theo hướng dẫn khóa học. Trong terminal:

```bash
git clone https://github.com/kazuonguyen/oaqjp-final-project-emb-ai.git final_project
cd final_project
python3 -m pip install -r requirements.txt
python3 tools/collect_evidence.py --live
python3 -m flask --app server run --host=0.0.0.0 --port=5000
```

Dùng **Launch Application**, chọn cổng **5000** để mở giao diện.
Môi trường lab không lưu lâu dài; bản sao đã được giữ trong GitHub và file ZIP.

## Nguồn chính thức

- Hướng dẫn lab IBM:
  https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/Ikq0b5aphFY8ilBIqdwA5A/Final-project-emb-ai-Mark-v1.md
- Repository khởi đầu:
  https://github.com/ibm-developer-skills-network/oaqjp-final-project-emb-ai
- API/model Watson Emotion:
  https://www.ibm.com/docs/en/watson-libraries?topic=catalog-emotion
