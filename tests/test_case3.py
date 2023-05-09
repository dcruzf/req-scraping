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


def test_get_sentences_body_header(case3):
    sentences = get_sentences_body_header(case3)
    expected = [
        "Órgãos do Governo",
        "Acesso à Informação",
        "Legislação",
        "Acessibilidade",
        "Serviços e Informações do Brasil",
    ]
    assert sentences == expected, case3.base.get("href")


def test_get_sentences_nav_breadcrumbs(case3):
    sentences = get_sentences_nav_breadcrumbs(case3)
    expected = [
        "Serviços",
        "Certificar-se como Entidade Beneficente de Assistência Social",
    ]
    assert sentences == expected, case3.base.get("href")


def test_get_sentences_div_listagem_servicos(case3):
    sentences = get_sentences_div_listagem_servicos(case3)
    expected = [
        "Assistência Social",
        "Rede de Assistência e Proteção Social",
        "Entidades Beneficentes",
    ]
    assert sentences == expected, case3.base.get("href")


def test_get_sentences_div_contentcore_header(case3):
    sentences = get_sentences_div_contentcore_header(case3)
    expected = [
        "Certificar-se como Entidade Beneficente de Assistência Social (CEBAS)",
        '''" CEBAS Assistência Social"''',
        "Iniciar",
    ]

    assert sentences == expected, set(sentences).difference(expected)


def test_get_sentences_div_contentcore_avaliacao_container(case3):
    sentences = get_sentences_div_contentcore_avaliacao_container(case3)
    expected = ["Avaliação: 4.5      (2177)"]
    assert sentences == expected, sentences


def test_get_sentences_div_id_viewlet_above_content_body(case3):
    sentences = get_sentences_div_id_viewlet_above_content_body(case3)
    expected = ["Última Modificação: 05/01/2023", "Compartilhe:"]
    assert sentences == expected, case3.base.get("href")


def test_get_sentences_id_dados_basicos(case3):
    sentences = get_sentences_id_dados_basicos(case3)
    expected = [
        "O que é?",
        "A Certificação CEBAS é um dos documentos exigidos pela Receita Federal, para que a entidade sem fins lucrativos usufrua de isenções e contribuições sociais, tais como a parte patronal da contribuição previdenciária sobre a folha de pagamento; a Contribuição Social sobre o Lucro Líquido – CSLL; entre outras.",
        "A Certificação CEBAS também possibilita a entidade a fazer convênios e parcerias com o poder público. Para obter a Certificação, a entidade deve solicitar por este Portal de Serviços gov.br.",
        "Participe dos Conselhos de Usuários(as) de Serviços Públicos do Ministério da Cidadania. Sua opinião é muito importante para ajudar a sua comunidade e todos(as) os(as) demais usuários(as) de serviços públicos a receber serviços mais ágeis, melhores e adequados às expectativas da população.",
        "Qualquer pessoa que utilize determinado serviço pode se inscrever para participar da avaliação dos serviços públicos. Uma vez cadastrados(as), os(as) conselheiros(as) podem responder a consultas sobre os serviços e também apresentar propostas de melhorias. O funcionamento dos conselhos é totalmente virtual, basta se voluntariar por meio da Plataforma virtual do Conselho de Usuários(as) de Serviços Públicos.",
        "Clique aqui, seja um(a) conselheiro(a) e avalie este serviço!",
    ]
    for i in range(len(expected)):
        assert sentences[i] == expected[i], sentences[i]

    assert len(sentences) == len(expected)


def test_get_sentences_id_solicitantes(case3):
    sentences = get_sentences_id_solicitantes(case3)
    expected = [
        "Quem pode utilizar este serviço?",
        "Pessoas jurídicas de direito privado sem fins lucrativos que atenderem, ao mesmo tempo, os seguintes requisitos:",
        "Realizar ações de atendimento, assessoramento, defesa e garantia de direitos de forma gratuita, continuada, planejada e universal, conforme as normativas da Política Nacional de Assistência Social, Estar inscrita no Conselho Municipal de Assistência Social CMAS de todos os municípios de atuação, no ano anterior ao requerimento da Certificação CEBAS, Estar em funcionamento no mínimo há 12 meses, e Estar com o Cadastro Nacional de Entidades Beneficentes de Assistência Social – CNEAS concluído no ano anterior ao do requerimento da Certificação CEBAS.",
    ]

    assert sentences == expected, set(sentences).difference(expected)


def test_get_sentences_id_etapas_servico(case3):
    sentences = get_sentences_id_etapas_servico(case3)
    expected = [
        "Etapas para a realização deste serviço",
        "Requerer a certificação",
        "O requerimento pode ser feito de forma simples e rápida, diretamente por meio deste Portal de Serviços, bastando que o representante da entidade já tenha feito o seu cadastro para obter login e senha de acesso na Plataforma Digital da Certificação CEBAS. O representante legal da entidade deve acessar este Portal de Serviços e inserir as informações da entidade e toda a documentação necessária, conforme esclarecimentos abaixo:",
        "Canais de prestação",
        "Web :",
        "Clique Aqui",
        "Documentação",
        "Documentação em comum para todos os casos",
        "REFERENTE AO EXERCÍCIO FISCAL DO ANO CORRENTE AO DO REQUERIMENTO:",
        "Apresentar comprovante de inscrição (matriz e filiais) no Cadastro Nacional de Pessoa Jurídica - CNPJ demonstrando estar legalmente constituída no país e em efetivo funcionamento há pelo menos 12 meses antes do requerimento;",
        "Ata de eleição dos dirigentes e do instrumento comprobatório de representação legal, quando for o caso;",
        "Estatuto Social registrado e autenticado em Cartório, contendo cláusula de dissolução/extinção, com destinação do eventual patrimônio remanescente a entidade sem fins lucrativos congêneres ou a entidades públicas, conforme art. 3º da Lei nº 12.101, de 2009 , e ter natureza, objetivos e público-alvo compatíveis com a legislação.",
        "REFERENTE AO EXERCÍCIO FISCAL DO ANO ANTERIOR AO DO REQUERIMENTO:",
        "Comprovante de inscrição da entidade no Conselho Municipal de Assistência Social ou do Distrito Federal (art. 3º e 19, I da Lei nº 12.101/2009 c/c art. 3º e 39, II do Decreto nº 8.242/2014), da matriz, bem como de suas respectivas filiais que atuem na área da Assistência Social;",
        "Relatório de todas as atividades desempenhadas, incluindo atividades meio e atividades não certificáveis, se houver. A entidade deve destacar em seu relatório as atividades desenvolvidas, os seus objetivos, com a identificação clara de cada serviço, projeto, programa ou benefício socioassistencial, a metodologia utilizada, o público alvo atendido, o número de atendidos, sua capacidade de atendimento, os resultados obtidos e recursos humanos envolvidos.",
        "Demonstrativo do Resultado do Exercício - DRE contendo receitas e despesas separadas por área de atuação da entidade, se for o caso. O DRE deve ser elaborado por profissional legalmente habilitado, atendidas as normas do Conselho Federal de Contabilidade.",
        "Notas Explicativas contendo esclarecimento da origem de todas as receitas apresentadas no DRE, elaboradas por profissional legalmente habilitado, atendidas as normas do Conselho Federal de Contabilidade.",
        "Atenção: as entidades com receita superior a R$1.000.000,00 (um milhão de reais) devem apresentar, além do DRE e Notas Explicativas, também o Balanço Patrimonial do exercício fiscal anterior ao requerimento.",
        "Importante: Para enviar os documentos por este Portal, a entidade poderá utilizar os seguintes formatos de arquivo: Word (.doc), PDF, Excel, Power Point e Imagem (.bmp, .jpg ou .jpeg). Desde 01/05/2019, a entidade deverá estar com o seu cadastro no CNEAS (Cadastro Nacional de Entidades de Assistência Social) concluído no ano anterior ao do requerimento.",
    ]

    for i in range(len(expected)):
        assert sentences[i] == expected[i], (
            sentences[i],
            case3.base.get("href"),
        )


def test_get_sentences_id_outras(case3):
    sentences = get_sentences_id_outras(case3)
    expected = [
        "Outras Informações",
        "Quanto tempo leva?",
        "Até 180 dia(s) corrido(s) é o tempo estimado para a prestação deste serviço.",
        "Informações adicionais ao tempo estimado",
        "Desde 01/05/2019, a entidade deve protocolar seu requerimento de concessão ou renovação do CEBAS diretamente neste Portal de Serviços. Não haverá mais protocolo via Correios ou balcão no Ministério da Cidadania.",
        "Este serviço é gratuito para o cidadão.",
        "Para mais informações ou dúvidas sobre este serviço, entre em contato",
        "Cartilha com passo a passo do CEBAS",
        "Chat direto com o MC.",
        "Telefone Central de Relacionamento: 121",
        "E-mail: cebas@cidadania.gov.br – para dúvidas sobre a Certificação.",
        "Este é um serviço do(a) Ministério da Cidadania . Em caso de dúvidas, reclamações ou sugestões favor contactá-lo.",
        "Validade do Documento",
        "Válido por 3 ano(s)",
        "Informações adicionais ao tempo de validade",
        "Conforme a legislação aplicável, Lei 12.101/2009 e Decreto 8.242/2014, a validade da certificação CEBAS poderá ser de 3 anos, se for um pedido originário de concessão de certificação ou se a entidade apresentar requerimento de renovação com receita bruta superior a 1 milhão de reais. Caso a entidade apresente um requerimento de renovação e entidade inferior a 1 milhão, o período da certificação será de 5 anos.",
        "Legislação",
        "Resolução CNAS n° 34/2011",
        "Resolução CNAS nº 27/2011",
        "Resolução CNAS nº 33/2011",
        "Resolução CNAS nº 109/2009",
        "Lei nº 12.101/2009",
        "Tratamento a ser dispensado ao usuário no atendimento",
        "O(A) usuário(a) deverá receber, conforme os princípios expressos na Lei nº 13.460/17, um atendimento pautado nas seguintes diretrizes:"
        "",
    ]

    for i in range(len(expected)):
        assert sentences[i] == expected[i], (sentences[i], expected[i])


def test_get_sentences_div_canais_atendimento(case3):
    sentences = get_sentences_div_canais_atendimento(case3)
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

    assert sentences == expected, case3.base.get("href")


def test_get_sentences_id_category(case3):
    sentences = get_sentences_id_category(case3)
    expected = [
        "Tags:",
        "Assistência Social",
        "Credenciamento",
        "CMAS",
        "Entidade Beneficiente",
        "Direitos",
        "MDS",
        "cebas",
        "CEBAS",
    ]

    assert sentences == expected, set(sentences).difference(expected)


def test_get_sentences_div_avaliacao(case3):
    sentences = get_sentences_div_avaliacao(case3)
    expected = [
        "Esta página foi útil para você?",
    ]

    assert sentences == expected, case3.base.get("href")


def test_get_sentences_div_portal_footer(case3):
    sentences = get_sentences_div_portal_footer(case3)
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
