import numpy as np

#Dữ liệu điểm số của 6 sinh viên trong 3 môn (Toán, Lý, Hóa)
scores = np.array([
    [7.5, 8.0, 6.5],
    [5.0, 6.0, 5.5],
    [8.5, 7.5, 9.0],
    [6.0, 5.5, 6.5],
    [9.0, 9.5, 8.0],
    [4.0, 5.0, 4.5]
])
print('---PHÂN TÍCH ĐIỂM SỐ SINH VIÊN---\n')

#Câu 1: Tính điểm trung bình mỗi sinh viên
print('1.Điểm trung bình mỗi sinh viên:')
student_averages = np.mean(scores, axis=1)
for i, avg in enumerate(student_averages):
    print(f'Sinh viên {i+1}:{avg:.2f}')
    
#Câu 2: Tính điểm trung bình mỗi môn học
print('\n2.Điểm trung bình mỗi môn học:')
subject_names = ['Toán','Lý','Hóa']
subject_averages = np.mean(scores,axis=0)
for i, (subject, avg) in enumerate(zip(subject_names, subject_averages)):
    print(f'{subject}: {avg:.2f}')
    
#Câu 3: Tìm sinh viên có điểm trung bình cao nhất
print('\n3.Sinh viên có điểm trung bình cao nhất:')
max_avg_index = np.argmax(student_averages)
print(f'Sinh viên {max_avg_index+1} với điểm trung bình: {student_averages[max_avg_index]}')

#Câu 4: Tìm những sinh viên có điểm Hóa >= 8.0
print('\n4.Sinh viên có điểm Hóa >= 8.0')
chemistry_scores = scores[:,2] 
high_chemistry = np.where(chemistry_scores >= 8)[0]
if len(high_chemistry) > 0:
    for student_idx in high_chemistry:
        print(f'Sinh viên {student_idx+1}:{chemistry_scores[student_idx]}') 
else:
    print('Không có sinh viên nào có điểm Hóa >= 8.0')  
    
#Câu 5: Thêm một cột mới chứa điểm trung bình của từng sinh viên vào scores
print('\n5.Thêm cột điểm trung bình vào ma trận scores:')
scores_with_avg = np.column_stack((scores,student_averages))
print('Ma trận mới (Toán, Lý, Hóa, Trung bình):')
for i, row in enumerate(scores_with_avg):
    print(f'Sinh viên {i+1}:[{row[0]:.1f},{row[1]:.1f},{row[2]:.2f}]') 
    
#Câu 6: Đếm số sinh viên có điểm Toán < 6.0
print('\n6.Số sinh viên có điểm Toán < 6.0')
math_scores = scores[:,0]
low_math_count = np.sum(math_scores< 6.0)
print(f'Có {low_math_count} sinh viên có điểm Toán < 6.0')

#Hiển thị chi tiết
low_math_students = np.where(math_scores< 6.0)[0]
if len(low_math_students) > 0:
    print('Chi tiết:')
    for student_idx in low_math_students:
        print(f'Sinh viên {student_idx+1}: {math_scores[student_idx]}')
        
#Câu 7: Chuẩn hóa điểm (z-score) cho từng môn học
print('\n7.Chuẩn hóa điểm (z-score) cho từng môn học:')
scores_normalized = np.zeros_like(scores)
for subject_idx in range(scores.shape[1]):
    subject_scores = scores[:, subject_idx]
    mean_score = np.mean(subject_scores)
    std_score = np.std(subject_scores)
    scores_normalized[:, subject_idx] = (subject_scores - mean_score)/ std_score
print('Z-score (Toán, Lý, Hóa):')
for i, row in enumerate(scores_normalized):
    print(f'Sinh viên {i+1}: [{row[0]:.3f},{row[1]:.3f},{row[2]:3f}]')
    
#Hiển thị thống kê chuẩn hóa
print('\nKiểm tra chuẩn hóa (mean ≈ 0,std ≈ 1):')
for i, subject in enumerate(subject_names):
    norm_mean = np.mean(scores_normalized[:,i])
    norm_std = np.std(scores_normalized[:,i])
    print(f'{subject}: mean = {norm_mean:.6f}, std = {norm_std:.6f}')
    
#Câu 8: Sắp xếp scores theo tổng điểm giảm dần
print('\n8.Sắp xếp sinh viên theo tổng điểm giảm dần:')
total_scores = np.sum(scores,axis=1)
sorted_indices = np.argsort(total_scores)[::-1]
print('Thứ tự xếp hạng:')
for rank, student_idx in enumerate(sorted_indices):
    total = total_scores[student_idx]
    avg = student_averages[student_idx]
    print(f'{rank+1}.Sinh viên {student_idx+1}: Tổng= {total:.1f}, TB = {avg:2f}')
    
#Ma trận đã sắp xếp
scores_sorted = scores[sorted_indices]
print('\nMa trận điểm đã sắp xếp:')
for i, (original_idx, row) in enumerate(zip(sorted_indices, scores_sorted)):
    print(f'Hạng {i+1} (SV {original_idx+1}: [{row[0]:.1f}, {row[1]:.1f}, {row[2]:.1f}])')
print("\n=== KẾT THÚC PHÂN TÍCH ===")