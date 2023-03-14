from bs4.element import NavigableString, Tag

# import sys

# sys.setrecursionlimit(10000)


def get_sentences_tag_util(tag: Tag):

    if isinstance(tag, NavigableString):
        return [str(tag)]

    if tag.name == "p":
        texts = []
        for descendant in tag:
            if isinstance(descendant, NavigableString):
                text = str(descendant)
                texts.append(text)
            else:
                texts.extend(get_sentences_tag_util(descendant))
        return "".join(texts).strip().split("<br>")

    if tag.name in ["span", "a"]:
        return [tag.get_text()]

    if tag.name == "br":
        return ["<br>"]

    if tag.name in ["ul", "ol", "li"]:
        texts = []
        for list_item in tag:
            texts.extend(get_sentences_tag_util(list_item))
        return texts

    if tag.name == "div":
        texts = []
        for element in tag:
            texts.extend(get_sentences_tag_util(element))
        return texts

    return tag.get_text("<br>", strip=True).split("<br>")
