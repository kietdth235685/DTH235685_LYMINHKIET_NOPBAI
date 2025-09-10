'''
các loại lỗi khi lập trình và cách bắt lỗi trong Python là:
các loại lỗi:
Syntax Error:   Lỗi cú pháp, phải sửa mới chạy được
Runtime Error:  Lỗi khi chạy chương trình, có thể bắt được
Logical Error:  Chương trình chạy được nhưng kết quả sai
cách bắt lỗi:
Cách bắt lỗi trong Python (Xử lý ngoại lệ - Exception Handling)

Python dùng cấu trúc try...except để bắt và xử lý lỗi khi chạy:

try:
    # Code có thể gây lỗi
    x = int(input("Nhập số: "))
    y = 10 / x
except ZeroDivisionError:
    print("Lỗi: Chia cho 0 không hợp lệ!")
except ValueError:
    print("Lỗi: Giá trị nhập vào không phải số nguyên!")
except Exception as e:
    print("Lỗi khác:", e)
else:
    print("Kết quả:", y)
finally:
    print("Hoàn thành khối try-except")


try: Chạy đoạn code có thể gây lỗi

except: Bắt lỗi cụ thể hoặc chung

else: Thực thi khi không có lỗi xảy ra

finally: Luôn thực thi, dùng để dọn dẹp (tùy chọn)
'''