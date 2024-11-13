import subprocess


def check_output_for_text(command, search_text):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout
    if result.returncode == 0 and search_text in out:
        return True
    else:
        return False


if __name__ == '__main__':
    cmd = "cat /etc/os-release"
    search_txt = 'PRETTY_NAME="Ubuntu 22.04.4 LTS"'
    is_successful = check_output_for_text(cmd, search_txt)
    if is_successful:
        print(f'Команда "{cmd}" успешно выполнена, и текст "{search_txt}" найден.')
    else:
        print("Команда не выполнена успешно или текст не найден.")
