import re


def parse_git_log(raw_log):
    pattern = re.compile(r'''(AuthorName(.*\n){4}(([\d|\-]*\t[\d|\-]*\t.*\n)|\n)*)''')
    matches = pattern.findall(raw_log)
    for match in matches:
        print(match[0])
        print("-------------------")
