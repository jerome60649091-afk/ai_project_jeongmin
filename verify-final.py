# -*- coding: utf-8 -*-
import sys
import io
from pathlib import Path

# Set output encoding for Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("=== 최종 검증: CSS 스타일시트 링크 확인 ===\n")

# 1. index.html 검증
index_file = Path(__file__).parent / "index.html"
with open(index_file, 'r', encoding='utf-8') as f:
    index_content = f.read()

print("[검증 1] index.html에서 CSS 링크 태그 확인")
if '<link rel="stylesheet" href="style.css">' in index_content:
    print("[PASS] CSS 링크 태그가 있습니다.")
    print("  위치: <head> 섹션 내")
    print("  태그: <link rel=\"stylesheet\" href=\"style.css\">")
else:
    print("[FAIL] CSS 링크 태그가 없습니다!")
    sys.exit(1)

# 2. style.css 검증
style_file = Path(__file__).parent / "style.css"
if style_file.exists():
    with open(style_file, 'r', encoding='utf-8') as f:
        style_content = f.read()

    print("\n[검증 2] style.css에서 필요한 CSS 클래스 확인")

    css_classes = {
        '.message-box': '메시지 박스 기본 스타일',
        '.message-success': '성공 메시지 스타일 (초록색)',
        '.message-warning': '경고 메시지 스타일 (노란색)'
    }

    all_found = True
    for css_class, description in css_classes.items():
        if css_class in style_content:
            print(f"[PASS] {description} ({css_class})")
        else:
            print(f"[FAIL] {description} ({css_class}) - 정의 안 됨")
            all_found = False

    if not all_found:
        sys.exit(1)
else:
    print("[FAIL] style.css 파일이 없습니다!")
    sys.exit(1)

# 3. script.js 검증
script_file = Path(__file__).parent / "script.js"
with open(script_file, 'r', encoding='utf-8') as f:
    script_content = f.read()

print("\n[검증 3] script.js에서 올바른 ID 참조 확인")

id_checks = {
    'getElementById("nameInput")': '이름 입력 필드 ID',
    'getElementById("startButton")': '버튼 ID',
    'getElementById("resultArea")': '결과 표시 영역 ID',
}

all_found = True
for id_check, description in id_checks.items():
    if id_check in script_content:
        print(f"[PASS] {description} ({id_check})")
    else:
        print(f"[FAIL] {description} - 찾을 수 없음")
        all_found = False

if not all_found:
    sys.exit(1)

print("\n[검증 4] script.js에서 CSS 클래스명 확인")

class_checks = {
    '"message-box "': '기본 스타일 클래스',
    '"message-success"': '성공 메시지 클래스',
    '"message-warning"': '경고 메시지 클래스',
}

all_found = True
for class_check, description in class_checks.items():
    if class_check in script_content:
        print(f"[PASS] {description} ({class_check})")
    else:
        print(f"[FAIL] {description} - 찾을 수 없음")
        all_found = False

if not all_found:
    sys.exit(1)

print("\n[검증 5] script.js에서 null 체크 확인")
if '!nameInput || !startButton || !messageArea' in script_content:
    print("[PASS] null 체크 방어 코드가 있습니다")
else:
    print("[FAIL] null 체크 방어 코드가 없습니다")
    sys.exit(1)

# 최종 결과
print("\n" + "="*50)
print("최종 결과: 모든 검증 항목 통과")
print("="*50)
print("\n예상되는 기능 (브라우저에서 확인):")
print("1. index.html 열기 → CSS 스타일시트 로드됨")
print("2. 이름 입력 없이 '실습 시작' 버튼 클릭")
print("   → 노란 배경(#fff7db) 경고 메시지 표시")
print("   → 텍스트: '이름을 먼저 입력해주세요.'")
print("3. 이름 입력 후 '실습 시작' 버튼 클릭")
print("   → 초록 배경(#e8f9ef) 성공 메시지 표시")
print("   → 텍스트: '[이름]님, 환영합니다! AI 협업 개발 실습을 시작합니다.'")
print("4. 메시지 박스는 패딩, 테두리, 반경이 적용됨")
print("\n브라우저 개발자 도구 Console: 에러 없음")
