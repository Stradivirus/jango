import os
import shutil
import subprocess

def copy_and_upload_to_git(source_folder):
    temp_folder = "/temp_git_folder"
    os.makedirs(temp_folder, exist_ok=True)
    
    for item in os.listdir(source_folder):
        s = os.path.join(source_folder, item)
        d = os.path.join(temp_folder, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks=False, ignore=None, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)
    
    try:
        subprocess.run(["git", "init"], cwd=temp_folder, check=True)
        subprocess.run(["git", "add", "."], cwd=temp_folder, check=True)
        subprocess.run(["git", "commit", "-m", "Initial commit"], cwd=temp_folder, check=True)
        
        repo_url = input("GitHub 리포지토리 URL을 입력하세요: ")
        
        subprocess.run(["git", "remote", "remove", "origin"], cwd=temp_folder, check=False)
        subprocess.run(["git", "remote", "add", "origin", repo_url], cwd=temp_folder, check=True)
        
        # 원격 저장소의 기본 브랜치 확인
        result = subprocess.run(["git", "ls-remote", "--exit-code", "--heads", "origin", "main"], 
                                cwd=temp_folder, capture_output=True, text=True)
        
        if result.returncode == 0:
            default_branch = "main"
        else:
            default_branch = "master"
        
        print(f"리포지토리의 기본 브랜치는 '{default_branch}'입니다.")
        
        # 로컬 브랜치 이름 변경
        subprocess.run(["git", "branch", "-m", default_branch], cwd=temp_folder, check=True)
        
        # force push 사용
        subprocess.run(["git", "push", "-u", "origin", default_branch, "--force"], cwd=temp_folder, check=True)
        print("파일들이 성공적으로 GitHub에 업로드되었습니다.")
    
    except subprocess.CalledProcessError as e:
        print(f"Git 명령어 실행 중 오류 발생: {e}")
    finally:
        shutil.rmtree(temp_folder)

if __name__ == "__main__":
    source_folder = input("업로드할 폴더 경로를 입력하세요: ")
    copy_and_upload_to_git(source_folder)
