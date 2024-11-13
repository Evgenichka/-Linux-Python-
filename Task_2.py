import subprocess
import string


def check_output_for_text(command, search_text, word_mode=False):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout

    if word_mode:
        out = out.translate(str.maketrans('', '', string.punctuation)).split()
        for element in out:
            print(element)

    if result.returncode == 0 and (search_text in out if word_mode else search_text in result.stdout):
        return True
    else:
        return False


if __name__ == '__main__':
    cmd = "cat /etc/os-release"
    search_txt = "LTS"
    is_successful = check_output_for_text(cmd, search_txt, word_mode=True)
    if is_successful:
        print(f'Команда "{cmd}"  выполнена, и слово "{search_txt}" найдено.')
    else:
        print("Команда не выполнена или слово не найдено.")
