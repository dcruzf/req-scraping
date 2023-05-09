import pytest
from bs4 import BeautifulSoup

from src.pull_data import (
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


def test_get_sentences_body_header(case5):
    sentences = get_sentences_body_header(case5)
    expected = [
        "Órgãos do Governo",
        "Acesso à Informação",
        "Legislação",
        "Acessibilidade",
        "Serviços e Informações do Brasil",
    ]
    assert sentences == expected, case5.base.get("href")


def test_get_sentences_nav_breadcrumbs(case5):
    sentences = get_sentences_nav_breadcrumbs(case5)
    expected = [
        "Serviços",
        "Requerer reconhecimento de instituição certificadora ou de certificação",
    ]

    assert sentences == expected, case5.base.get("href")


def test_get_sentences_div_listagem_servicos(case5):
    sentences = get_sentences_div_listagem_servicos(case5)
    expected = [
        "Trabalho, Emprego e Previdência",
        "Previdência",
        "Comunicações e Requerimentos",
    ]
    assert sentences == expected, case5.base.get("href")


def test_get_sentences_div_contentcore_header(case5):
    sentences = get_sentences_div_contentcore_header(case5)
    expected = [
        "Requerer reconhecimento de instituição certificadora ou de certificação",
        "Iniciar",
    ]

    assert sentences == expected, set(sentences).difference(expected)


def test_get_sentences_div_contentcore_avaliacao_container(case5):
    sentences = get_sentences_div_contentcore_avaliacao_container(case5)
    expected = ["Avaliação: Sem Avaliação"]
    assert sentences == expected, sentences


def test_get_sentences_div_id_viewlet_above_content_body(case5):
    sentences = get_sentences_div_id_viewlet_above_content_body(case5)
    expected = ["Última Modificação: 05/01/2023", "Compartilhe:"]
    assert sentences == expected, case5.base.get("href")


def test_get_sentences_id_dados_basicos(case5):
    sentences = get_sentences_id_dados_basicos(case5)
    expected = [
        "O que é?",
        "Obter reconhecimento de instituição certificadora e respectivos certificados.",
        "As instituições certificadoras são responsáveis pela certificação dos dirigentes das entidades fechadas de previdência complementar.",
        "Saiba mais sobre previdência privada e entidades fechadas de previdência complementar:",
    ]
    for i in range(len(expected)):
        assert sentences[i] == expected[i], sentences[i]

    assert len(sentences) == len(expected)


def test_get_sentences_id_solicitantes(case5):
    sentences = get_sentences_id_solicitantes(case5)
    expected = [
        "Quem pode utilizar este serviço?",
        "Instituição autônoma, responsável pela emissão, manutenção e controle dos certificados e com capacidade técnica reconhecida pela Previc.",
        "experiência de, no mínimo, três anos na emissão de certificados ou em atividades de treinamento vinculadas aos conteúdos previstos na legislação específica;",
        "experiência na guarda, controle e renovação de certificados;",
        "emitir certificado que exija conhecimento, formação e experiência compatíveis com os requisitos técnicos necessários para o exercício de cargo ou função em EFPC; e",
        "compartilhar, semestralmente, informações acerca dos certificados emitidos.",
    ]

    assert sentences == expected, set(sentences).difference(expected)


def test_get_sentences_id_etapas_servico(case5):
    sentences = get_sentences_id_etapas_servico(case5)
    expected = [
        "Etapas para a realização deste serviço",
        "Protocolar Requerimento",
        "Enviar documentação para análise da Previc.",
        "Você deverá enviar todos os documentos listados abaixo pelo sistema.",
        "Canais de prestação",
        "Web :",
        "Sistema Eletrônico de Informações - SEi!",
        "Documentação",
        "Documentação em comum para todos os casos",
        "Para reconhecimento da instituição certificadora",
        "Estatuto ou contrato social;",
        "Comprovação do cumprimento dos requisitos mínimos;",
        "Declaração de independência e de inexistência de conflito de interesses em relação às EFPC para fins de certificação;",
        "Outros documentos que facilitem a análise de reconhecimento.",
        "Para reconhecimento da certificação",
        "Identificação do certificado a ser reconhecido;",
        "Edital ou regulamento do exame de certificação;",
        "Conteúdo programático exigido para a prova de conhecimentos;",
        "Comprovação do prazo de validade máximo de quatro anos;",
        "Outros documentos que facilitem a análise de reconhecimento.",
        "Tempo de duração da etapa",
        "Não estimado ainda",
        "Receber Análise",
        "Receber resultado da análise da documentação.",
        "Análise do requerimento pela Previc.",
        "Canais de prestação",
        "Web :",
        "Sistema Eletrônico de Informações - SEi!",
        "Tempo de duração da etapa",
        "Até 30 dia(s) útil(eis)",
    ]

    for i in range(len(expected)):
        assert sentences[i] == expected[i], (
            sentences[i],
            case5.base.get("href"),
        )


def test_get_sentences_id_outras(case5):
    sentences = get_sentences_id_outras(case5)
    expected = [
        "Outras Informações",
        "Quanto tempo leva?",
        "Até 30 dia(s) útil(eis) é o tempo estimado para a prestação deste serviço.",
        "Informações adicionais ao tempo estimado",
        "Por ocasião da análise, caso seja identificada a necessidade de ajustes na documentação ou de envio de informações adicionais, a Previc pode emitir exigências, as quais deverão ser atendidas no prazo de 60 dias úteis a contar da sua intimação.",
        "Este serviço é gratuito para o cidadão.",
        "Para mais informações ou dúvidas sobre este serviço, entre em contato",
        "Coordenação-Geral de Autorização para Funcionamento e Gestão de Cadastro",
        "(61) 2021-2000",
        "Este é um serviço do(a) Superintendência Nacional de Previdência Complementar . Em caso de dúvidas, reclamações ou sugestões favor contactá-lo.",
        "Validade do Documento",
        "Sem validade.",
        "Legislação",
        "Resolução CNPC nº 19, de 30 de março de 2015",
        "Instrução Normativa nº 29, de 21 de julho de 2020",
        "Tratamento a ser dispensado ao usuário no atendimento",
        "O usuário deverá receber, conforme os princípios expressos na lei nº 13.460/17, um atendimento pautado nas seguintes diretrizes:",
        "Urbanidade;",
        "Respeito;",
        "Acessibilidade;",
        "Cortesia;",
        "Presunção da boa-fé do usuário;",
        "Igualdade;",
        "Eficiência;",
        "Segurança; e",
        "Ética",
        "Informações sobre as condições de acessibilidade, sinalização, limpeza e conforto dos locais de atendimento",
        "O usuário do serviço público, conforme estabelecido pela lei nº13.460/17, tem direito a atendimento presencial, quando necessário, em instalações salubres, seguras, sinalizadas, acessíveis e adequadas ao serviço e ao atendimento.",
        "Informação sobre quem tem direito a tratamento prioritário",
        "Tem direito a atendimento prioritário as pessoas com deficiência, os idosos com idade igual ou superior a 60 anos, as gestantes, as lactantes, as pessoas com crianças de colo e os obesos, conforme estabelecido pela lei 10.048, de 8 de novembro de 2000.",
    ]

    for i in range(len(expected)):
        assert sentences[i] == expected[i], (sentences[i], expected[i])


def test_get_sentences_div_canais_atendimento(case5):
    sentences = get_sentences_div_canais_atendimento(case5)
    expected = [
        "Ouvidoria",
        "Denúncia",
        "Para comunicar a ocorrência de alguma irregularidade relacionada ao serviço",
        "Reclamação",
        "Se você foi mal atendido e está insatisfeito com o atendimento e/ou serviço prestado",
        "Elogio",
        "Se você ficou satisfeito com o serviço prestado",
        "Sugestão",
        "Se você tiver uma idéia ou proposta de melhoria para este serviço",
    ]

    assert sentences == expected, case5.base.get("href")


def test_get_sentences_id_category(case5):
    sentences = get_sentences_id_category(case5)
    expected = [
        "Tags:",
        "Certificação",
        "Certificado",
        "Qualificação",
        "Dirigente",
    ]

    assert sentences == expected, set(sentences).difference(expected)


def test_get_sentences_div_avaliacao(case5):
    sentences = get_sentences_div_avaliacao(case5)
    expected = [
        "Esta página foi útil para você?",
    ]

    assert sentences == expected, case5.base.get("href")


def test_get_sentences_div_portal_footer(case5):
    sentences = get_sentences_div_portal_footer(case5)
    expected = [
        "Serviços",
        "Buscar serviços por",
        "Categorias",
        "Órgãos",
        "Estados",
        "Serviços por público alvo",
        "Cidadãos",
        "Empresas",
        "Órgãos e Entidades Públicas",
        "Demais segmentos (ONGs, organizações sociais, etc)",
        "Servidor Público",
        "Galeria de Aplicativos",
        "Notícias",
        "Serviços para o cidadão",
        "Saúde",
        "Agricultura e Pecuária",
        "Cidadania e Assistência Social",
        "Cultura e Esporte",
        "Economia e Gestão Pública",
        "Educação e Pesquisa",
        "Energia",
        "Forças Armadas e Defesa Civil",
        "Infraestrutura",
        "Justiça e Segurança",
        "Meio Ambiente",
        "Trabalho e Previdência",
        "Turismo",
        "Acompanhe o Planalto",
        "Navegação",
        "Acessibilidade",
        "Mapa do Site",
        "Termos de Uso",
        "Sobre o gov.br",
        "Acesse sua conta gov.br",
        "Órgãos do Governo",
        "Temas em Destaque",
        "Por dentro do Gov.br",
        "Dúvidas Frequentes em relação ao Portal gov.br",
        "Dúvidas Frequentes da conta gov.br",
        "Ajuda para Navegar o Portal",
        "Conheça os elementos do Portal",
        "Política de e-participação",
        "Termos de Uso",
        "Governo Digital",
        "Guia de Edição de Serviços do Portal Gov.br",
        "Dados do Governo Federal",
        "Dados Abertos",
        "Painel Estatístico de Pessoal",
        "Painel de Compras do Governo Federal",
        "Acesso à Informação",
        "Redefinir Cookies",
        "Redes sociais",
        "Todo o conteúdo deste site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada.",
    ]

    assert set(sentences) == set(expected), set(expected).difference(sentences)
