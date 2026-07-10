from typing import List


def process_arguments(s: str) -> List[str]:
    args = []
    open = ''
    tmp = ''

    s = s.strip()

    for c in s:
        if not open and c == ' ':
            args.append(tmp.strip())
            tmp = ''
            continue

        if not open and (c == '\'' or c == '\"'):
            open = c
            continue

        if open and c == open:
            open = ''
            args.append(tmp.strip())
            tmp = ''
            continue

        tmp += c

    if tmp:
        args.append(tmp)

    res = []
    for s in args:
        if not s.strip():
            continue
        res.append(s)

    return res
