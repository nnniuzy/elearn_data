import hanlp
import wordninja

tokenzier = hanlp.utils.rules.tokenize_english

first = tokenzier(
    "Manymachinelearningproblemsbecomeexceedinglydifficultwhenthenumberofdimensionsinthedataishigh.Thisphenomenonisknownasthecurseofdimensionality.Ofparticularconcernisthatthenumberofpossibledistinctconfigurationsofasetofvariablesincreasesexponentiallyasthenumberofvariablesincreases")
print(first)


def punctuation_index(str, punctuations):
    """
    查找标点索引
    :param str: 字符串
    :param punctuations: 标点列表
    :return: 标点索引
    """
    index = []
    for i, content in enumerate(str):
        if content in punctuations:
            index.append(i)
    return index


def split_punctuation(str, punctuations):
    """
    根据索引将标点符号和英文分开
    :param str:
    :param punctuations:
    :return:
    """
    index = punctuation_index(str, punctuations)
    target = []
    pre = 0
    for i in index:
        target.append(str[pre:i])
        target.append(str[i:i + 1])
        pre = i + 1
    target.append(str[index[-1] + 1:])
    return target


def is_punctuation(str, punctuations):
    if str in punctuations:
        return True
    else:
        return False


def separate_words(str, punctuations):
    middle = split_punctuation(str, punctuations)
    target = []
    for i in middle:
        if is_punctuation(i, punctuations):
            target.append(i)
        else:
            cache = wordninja.split(i)
            for j in cache:
                target.append(j)
    return target


print(separate_words(first[0], [',', '.']))
