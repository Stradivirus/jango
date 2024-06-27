import subprocess

packages = [
    "net-tools",
    "tar",
    "wget",
    "vim",
    "tree",
    "pip",
    "gcc",
    "gcc-c++",
    "kernel-devel",
    "make",
    "git",  # 추가됨
]

# 시스템 업데이트
subprocess.run(["sudo", "dnf", "-y", "update"], check=True)

# 패키지 설치
subprocess.run(["sudo", "dnf", "-y", "install"] + packages, check=True)

#되냐?
