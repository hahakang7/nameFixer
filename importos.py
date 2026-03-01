import os
import unicodedata

def fix_hangeul_filenames(directory_path): 
    # 폴더 존재 여부 확인
    if not os.path.isdir(directory_path):
        print(f"오류: '{directory_path}' 경로를 찾을 수 없습니다.")
        return

    count = 0
    # os.walk를 이용해 하위 폴더까지 탐색
    for root, dirs, files in os.walk(directory_path):
        for name in files + dirs:
            original_path = os.path.join(root, name)
            
            # NFD(분리된 한글)를 NFC(합쳐진 한글)로 변환
            normalized_name = unicodedata.normalize('NFC', name)
            
            # 이름이 변경된 경우에만 rename 실행
            if name != normalized_name:
                new_path = os.path.join(root, normalized_name)
                
                try:
                    os.rename(original_path, new_path)
                    print(f"변경됨: {name} -> {normalized_name}")
                    count += 1
                except Exception as e:
                    print(f"오류 발생 ({name}): {e}")

    print(f"\n총 {count}개의 파일명/폴더명이 복구되었습니다.")

# 사용 방법: 변환하고 싶은 폴더 경로를 입력하세요.
if __name__ == "__main__":
    target_folder = input("복구할 폴더 경로를 입력하세요: ").strip()
    fix_hangeul_filenames(target_folder)