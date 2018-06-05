import os
import logParser

def main():
    print("current directory : {}".format(os.getcwd()))
    repo_location = 'D:/test/GitLogNinja/repositorySamples'
    git_cmd_str = 'git -C {repo_location} log  ' \
                  '--remotes=origin --numstat --pretty=oneline --date=short ' \
                  '--format="AuthorName:%aN%n' \
                  'AuthorEmail:%aE%nAuthorDate:%ad%nSubject:%s"'

    # git_log = os.system(git_cmd_str.format(repo_location=repo_location))
    git_log = os.popen(git_cmd_str.format(repo_location=repo_location))
    log_text = ''.join(git_log)
    # commits = log_text.split(u"NUL")
    logParser.parse_git_log(log_text)
    # print(log_text)
    # for line in git_log:
    #     print("{}".format(line), end='')

    # print(type(log_text))
    # print(type(git_log))


if __name__ == "__main__":
    print("begin journey")
    main()
    print("end journey")
