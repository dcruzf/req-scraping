from bs4.element import NavigableString, Tag


def get_text_general(tag: Tag):
    texts = []
    for descendant in tag.descendants:
        if isinstance(descendant, NavigableString):
            texts.append(str(descendant))
        elif descendant.name in ["a", "b", "span", "strong", "abbr"]:
            continue
        elif descendant.name in ["p", "li", "div", "td", "br"]:
            texts.append("<#SPLIT#>")

    # breakpoint()
    texts = "".join(texts).strip().split("<#SPLIT#>")
    return [text.strip() for text in texts if text.strip()]
