import lief
import sys
import os

def inject_frida(so_path, frida_lib_name="libfrida.so"):
    # 加载 libmain.so
    binary = lief.parse(so_path)

    # 检查是否已经注入过
    for library in binary.libraries:
        if library == frida_lib_name:
            print(f"[-] {frida_lib_name} 已经存在于导入表中。")
            return

    # 添加依赖项
    binary.add_library(frida_lib_name)

    # 保存新文件
    output_path = so_path + ".new"
    binary.write(output_path)
    print(f"[+] 成功！新文件已生成: {output_path}")
    print(f"[!] 请将该文件重命名回 libmain.so 并替换 APK 中的原文件。")

if __name__ == "__main__":
    # 你从 APK 提取出的 libmain.so 路径
    target_so = "libmain.so"
    if os.path.exists(target_so):
        inject_frida(target_so)
    else:
        print("[-] 错误：请将 libmain.so 放在当前目录下。")
