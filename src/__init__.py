from bs4 import BeautifulSoup

from .pull_data import (
    get_sentences_body_header,
    get_sentences_div_avaliacao,
    get_sentences_div_canais_atendimento,
    get_sentences_div_contentcore_avaliacao_container,
    get_sentences_div_contentcore_header,
    get_sentences_div_id_viewlet_above_content_body,
    get_sentences_div_listagem_servicos,
    get_sentences_div_portal_footer,
    get_sentences_id_category,
    get_sentences_id_dados_basicos,
    get_sentences_id_etapas_servico,
    get_sentences_id_outras,
    get_sentences_id_solicitantes,
    get_sentences_nav_breadcrumbs,
)


class Scrap:
    functions = (
        get_sentences_body_header,
        get_sentences_nav_breadcrumbs,
        get_sentences_div_listagem_servicos,
        get_sentences_div_contentcore_header,
        get_sentences_div_contentcore_avaliacao_container,
        get_sentences_div_id_viewlet_above_content_body,
        get_sentences_id_dados_basicos,
        get_sentences_id_solicitantes,
        get_sentences_id_etapas_servico,
        get_sentences_id_outras,
        get_sentences_div_canais_atendimento,
        get_sentences_id_category,
        get_sentences_div_avaliacao,
        get_sentences_div_portal_footer,
    )
    errors = None
    soup = None

    def __call__(self, code_string):
        self.soup = BeautifulSoup(code_string, "html.parser")
        result = self.run()
        return result

    def run(self):
        result = []
        errors = {}
        for f in self.functions:
            try:
                sentences = f(self.soup)
                result.extend(sentences)
            except Exception as e:
                errors[f.__name__] = e
        self.errors = errors
        return result


scrap = Scrap()
