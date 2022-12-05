from bs4.element import NavigableString
import re

re_spaces = re.compile(r"\s{2,}")


def normalize_spaces(sentence):
    return re_spaces.sub(" ", sentence).strip()


def get_sentence_by_tag(tag):

    if tag.name == "p":
        if not tag.find_all("br"):
            return [tag.get_text(" ", strip=True)]
        text_list = []
        for descendant in tag.descendants:
            if isinstance(descendant, NavigableString):
                text = descendant.strip()
                text_list.append(text)
            elif descendant.name == "br":
                text_list.append("<#SPLIT#>")
        text_list = " ".join(text_list).split("<#SPLIT#>")
        return [text.strip() for text in text_list if text.strip()]
    else:
        text_list = tag.get_text("<#SPLIT#>", strip=True).split("<#SPLIT#>")
        return text_list


def get_sentences_body_header(soup):
    """Get sentences from soup.body.header."""
    text_list = [
        a.get_text().strip() for a in soup.body.header.ul.find_all("a")
    ]
    name = soup.body.header.find("div", attrs={"class": "site-name"}).get_text(
        strip=True
    )
    text_list.append(name)
    return text_list


def get_sentences_nav_breadcrumbs(soup):
    """Get sentences from nav#breadcrumbs"""
    breadcrumbs = soup.body.find("nav", attrs={"id": "breadcrumbs"})
    text_list = [
        span.get_text(strip=True)
        for span in breadcrumbs.find_all("span", attrs={"dir": "ltr"})
    ]
    return text_list


def get_sentences_div_listagem_servicos(soup):
    """div.listagem-servicos"""
    content_core = soup.body.find("div", attrs={"id": "content-core"})
    list_serv = content_core.find("div", attrs={"class": "listagem-servicos"})
    text_list = [a.get_text(strip=True) for a in list_serv.find_all("a")]
    return text_list


def get_sentences_div_contentcore_header(soup):
    content_core = soup.body.find("div", attrs={"id": "content-core"})
    visao_serviço = content_core.find("div", attrs={"class": "visao-servico"})
    header = visao_serviço.find("div", attrs={"class": "header"})
    text_list = [
        child.get_text(strip=True)
        for child in header.find_all(True, recursive=False)
    ]
    return text_list


def get_sentences_div_contentcore_avaliacao_container(soup):
    content_core = soup.body.find("div", attrs={"id": "content-core"})
    container = content_core.find(
        "div", attrs={"class": "avaliacao-container"}
    )
    text_list = [
        " ".join(
            span.get_text(strip=True) for span in container.find_all("span")
        )
    ]
    return text_list


def get_sentences_div_id_viewlet_above_content_body(soup):
    viewlet = soup.body.find("div", attrs={"id": "viewlet-above-content-body"})
    document_by_line = viewlet.find("div", attrs={"class": "documentByLine"})
    modified = document_by_line.get_text(strip=True)
    social_links = viewlet.find("div", attrs={"class": "social-links"})
    label = social_links.label.get_text(strip=True)
    return [modified, label]


def get_sentences_id_dados_basicos(soup):
    a_dados_basicos = soup.find("a", attrs={"id": "dados_basicos"})
    conteudo = a_dados_basicos.parent.div
    text_list = [a_dados_basicos.get_text(strip=True)]
    for tag in conteudo.find_all(True, recursive=False):
        result = get_sentence_by_tag(tag)
        text_list.extend(result)
    return [normalize_spaces(text) for text in text_list if text]


def get_sentences_id_solicitantes(soup):
    solicitantes = soup.find("a", attrs={"id": "solicitantes"})
    conteudo = solicitantes.parent.div
    text_list = [solicitantes.get_text(strip=True)]
    for tag in conteudo.find_all(True, recursive=False):
        result = get_sentence_by_tag(tag)
        text_list.extend(result)
    return [normalize_spaces(text) for text in text_list if text]


def get_sentences_id_etapas_servico(soup):
    solicitantes = soup.find("a", attrs={"id": "etapas-servico"})
    conteudo = solicitantes.parent.div
    text_list = [solicitantes.get_text(strip=True)]
    for tag in conteudo.find_all(True, recursive=False):
        result = get_sentence_by_tag(tag)
        text_list.extend(result)
    return [normalize_spaces(text) for text in text_list if text]


def get_sentences_id_outras(soup):
    outras = soup.find("a", attrs={"id": "outras"})
    conteudo = outras.parent.div
    text_list = [outras.get_text(strip=True)]
    for tag in conteudo.find_all(True, recursive=False):
        if tag.b is not None:
            text_list.append(tag.b.get_text(" ", strip=True))
        if tag.div is not None:
            text_list.append(tag.div.get_text(" ", strip=True))
        else:
            text_list.append(tag.get_text(" ", strip=True))
    return [normalize_spaces(text) for text in text_list if text]


def get_sentences_div_canais_atendimento(soup):
    content_core = soup.body.find("div", attrs={"id": "content-core"})
    visao = content_core.find("div", attrs={"class": "visao-servico"})
    canais = visao.find("div", attrs={"class": "canais-atendimento"})

    text_list = [canais.div.get_text(strip=True)]
    for tag in canais.find_all("span", attrs={"class": "back"}):
        text_list.extend(
            tag.get_text("<#SPLIT#>", strip=True).split("<#SPLIT#>")
        )
    return text_list


def get_sentences_id_category(soup):
    category = soup.body.find("div", attrs={"id": "category"})
    return category.get_text("<#SPLIT#>", strip=True).split("<#SPLIT#>")