# Hướng dẫn nộp Final project — Emotion Detector

## Tình trạng hiện tại

- Đã clone mã khởi đầu chính thức của IBM.
- Đã viết package `EmotionDetection`, Flask `server.py`, xử lý lỗi 400/input trống.
- Đã viết đủ 5 bài kiểm thử dùng các câu yêu cầu của khóa học.
- 11 kiểm thử offline đã chạy thành công. Các kiểm thử này dùng phản hồi giả lập
  và kiểm tra logic/HTTP/Flask; không chứng minh Watson phân loại đúng.
- `pylint server.py` đạt **10.00/10**, không tắt kiểm tra hay sửa cách tính điểm.
- Đã tạo fork công khai: https://github.com/kazuonguyen/oaqjp-final-project-emb-ai
- Chưa chạy được suy luận Watson thật từ máy cá nhân. Hướng dẫn IBM xác nhận API
  chỉ truy cập được trong Skills Network Theia Lab. Một yêu cầu trực tiếp từ
  máy hiện tại đã hết thời gian chờ (HTTP 000).
- Chưa có ảnh `6b_deployment_test.png` với kết quả Watson thật.
- Ảnh `7c_error_handling_interface.png` được chụp từ ứng dụng Flask thật tại máy,
  sau khi bấm phân tích với input trống. Không cần API cho trường hợp này.

## Hoàn tất trong Skills Network Theia Lab

1. Fork công khai đã chuẩn bị:
   https://github.com/kazuonguyen/oaqjp-final-project-emb-ai
2. Trong Theia Lab, clone fork thành thư mục `final_project`:

```bash
git clone https://github.com/kazuonguyen/oaqjp-final-project-emb-ai.git final_project
```

3. Chạy:

```bash
cd final_project
python3 -m pip install -r requirements.txt
python3 tools/collect_evidence.py --live
```

Script lưu kết quả thực tế vào `evidence/`, kèm lệnh, thời gian và exit status.
Chỉ dùng log thành công để nộp; nếu có lỗi, xử lý rồi chạy lại. Không sử dụng log
`offline_tests.txt` thay cho kết quả 5 bài kiểm thử Watson thật ở Task 5.

4. Chạy giao diện:

```bash
python3 server.py
```

Dùng công cụ **Launch Application** của Skills Network, cổng **5000**.
Nhập đúng câu `I think I am having fun`, bấm **Run Sentiment Analysis**, đợi
kết quả có 5 điểm cảm xúc và cảm xúc trội. Chụp ảnh tên `6b_deployment_test.png`.
Xóa input, bấm lại và chụp ảnh `7c_error_handling_interface.png` nếu muốn
chụp lại toàn bộ bằng chứng trong lab.

5. Commit/push source và bằng chứng vào fork.
6. Hai URL cần nộp:

```text
https://github.com/kazuonguyen/oaqjp-final-project-emb-ai/blob/main/README.md
https://github.com/kazuonguyen/oaqjp-final-project-emb-ai/blob/main/EmotionDetection/__init__.py
```

Hai URL này trỏ tới fork công khai của project.

## Ánh xạ từng câu trong rubric

| Mục | Nội dung cần nộp |
| --- | --- |
| Task 1 | [README.md](https://github.com/kazuonguyen/oaqjp-final-project-emb-ai/blob/main/README.md) |
| Task 2 Activity 1 | Dán toàn bộ `evidence/2a_emotion_detection.txt` |
| Task 2 Activity 2 | Dán `evidence/2b_application_creation.txt` sau khi chạy `--live` thành công |
| Task 3 Activity 1 | Dán `evidence/3a_output_formatting.txt` |
| Task 3 Activity 2 | Dán `evidence/3b_formatted_output_test.txt` sau khi chạy `--live` thành công |
| Task 4 Activity 1 | [EmotionDetection/__init__.py](https://github.com/kazuonguyen/oaqjp-final-project-emb-ai/blob/main/EmotionDetection/__init__.py) |
| Task 4 Activity 2 | Dán `evidence/4b_packaging_test.txt` sau khi chạy `--live` thành công |
| Task 5 Activity 1 | Dán `evidence/5a_unit_testing.txt` |
| Task 5 Activity 2 | Dán `evidence/5b_unit_testing_result.txt` sau khi 5 test Watson thật đều pass |
| Task 6 Activity 1 | Dán `evidence/6a_server.txt` |
| Task 6 Activity 2 | Upload ảnh `6b_deployment_test.png` sau khi kiểm tra Watson thật |
| Task 7 Activity 1 | Dán `evidence/7a_error_handling_function.txt` |
| Task 7 Activity 2 | Dán `evidence/7b_error_handling_server.txt` |
| Task 7 Activity 3 | Upload ảnh `7c_error_handling_interface.png` |
| Task 8 Activity 1 | Dán `evidence/8a_server_modified.txt` |
| Task 8 Activity 2 | Dán `evidence/8b_static_code_analysis.txt` (đã có kết quả 10.00/10) |

## Nguồn chính thức

- Hướng dẫn lab IBM, gồm yêu cầu chạy API trong Theia:
  https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/Ikq0b5aphFY8ilBIqdwA5A/Final-project-emb-ai-Mark-v1.md
- Repository khởi đầu:
  https://github.com/ibm-developer-skills-network/oaqjp-final-project-emb-ai
- Tài liệu API/model Watson Emotion:
  https://www.ibm.com/docs/en/watson-libraries?topic=catalog-emotion
