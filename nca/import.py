import os
import django

# Django 설정 로드
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nca.settings")
django.setup()

from exam.models import Question

def import_questions_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        questions = content.split('\n\n')
        
        for q in questions:
            lines = q.strip().split('\n')
            if len(lines) == 6:
                question_text = lines[0]
                choices = lines[1:5]
                correct_answer = lines[5].split(':')[-1].strip()
                
                question = Question(
                    question_text=question_text,
                    choice_a=choices[0][3:].strip(),  # "1) " 제거
                    choice_b=choices[1][3:].strip(),  # "2) " 제거
                    choice_c=choices[2][3:].strip(),  # "3) " 제거
                    choice_d=choices[3][3:].strip(),  # "4) " 제거
                    correct_answer=correct_answer
                )
                question.save()
                print(f"저장된 문제: {question_text}")
            else:
                print(f"올바르지 않은 형식의 문제를 건너뜁니다: {q}")

    print("문제 가져오기가 완료되었습니다.")

if __name__ == "__main__":
    file_path = "/work/django/nca/exam.txt"  # 실제 txt 파일 경로로 변경하세요
    import_questions_from_file(file_path)
