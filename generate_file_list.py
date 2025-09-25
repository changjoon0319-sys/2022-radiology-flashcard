
import os
import json

# --- 설정 ---
# 이미지가 들어있는 폴더 이름을 여기에 적어주세요.
# 이 파이썬 파일과 같은 위치에 'img' 폴더가 있다고 가정합니다.
IMAGE_FOLDER = 'img'

# --- 스크립트 시작 ---
def generate_file_list():
    """지정된 폴더에서 이미지 파일 목록을 찾아 JavaScript 배열 형식으로 출력합니다."""
    if not os.path.isdir(IMAGE_FOLDER):
        print(f"오류: '{IMAGE_FOLDER}' 폴더를 찾을 수 없습니다.")
        print("이 스크립트 파일과 같은 위치에 이미지 폴더가 있는지 확인해주세요.")
        return

    try:
        # 폴더 내의 모든 파일 목록을 가져옵니다.
        files = os.listdir(IMAGE_FOLDER)
        
        # 이미지 파일만 필터링합니다 (jpg, jpeg, png 등). 대소문자 구분 없이.
        image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
        image_files = [f for f in files if os.path.splitext(f)[1].lower() in image_extensions]
        
        # 파일 이름을 올바르게 정렬합니다 (예: no1, no2, no10 순으로).
        image_files.sort(key=lambda x: int(''.join(filter(str.isdigit, os.path.splitext(x)[0]))))

        # JSON 형식으로 파일 목록을 만듭니다 (따옴표 등을 자동으로 처리해줘서 안전합니다).
        js_array_string = json.dumps(image_files)
        
        # 최종 JavaScript 코드 형식으로 출력합니다.
        print("\n--- 아래 라인을 복사해서 HTML 파일에 붙여넣으세요 ---")
        print(f"const allImageFiles = {js_array_string};")
        print(f"\n성공적으로 {len(image_files)}개의 이미지 파일을 찾았습니다.")

    except Exception as e:
        print(f"파일 목록을 생성하는 중 오류가 발생했습니다: {e}")

if __name__ == '__main__':
    generate_file_list()
