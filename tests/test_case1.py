import pytest
from bs4 import BeautifulSoup

from src.pull_data import (
    get_sentence_by_tag,
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


def test_get_sentences_body_header(case1):
    sentences = get_sentences_body_header(case1)
    expected = [
        "Órgãos do Governo",
        "Acesso à Informação",
        "Legislação",
        "Acessibilidade",
        "Serviços e Informações do Brasil",
    ]
    assert sentences == expected, case1.base.get("href")


def test_get_sentences_nav_breadcrumbs(case1):
    sentences = get_sentences_nav_breadcrumbs(case1)
    expected = [
        "Serviços",
        "Aderir ao Projeto Salas Verdes",
    ]
    assert sentences == expected, case1.base.get("href")


def test_get_sentences_div_listagem_servicos(case1):
    sentences = get_sentences_div_listagem_servicos(case1)
    expected = [
        "Meio Ambiente e Clima",
        "Pesquisa e Aprendizado",
        "Estudos e Capacitações",
    ]
    assert sentences == expected, case1.base.get("href")


def test_get_sentences_div_contentcore_header(case1):
    sentences = get_sentences_div_contentcore_header(case1)
    expected = [
        "Aderir ao Projeto Salas Verdes",
        "Iniciar",
    ]
    assert sentences == expected, case1.base.get("href")


def test_get_sentences_div_contentcore_avaliacao_container(case1):
    sentences = get_sentences_div_contentcore_avaliacao_container(case1)
    expected = ["Avaliação: Sem Avaliação"]
    assert sentences == expected, case1.base.get("href")


def test_get_sentences_div_id_viewlet_above_content_body(case1):
    sentences = get_sentences_div_id_viewlet_above_content_body(case1)
    expected = ["Última Modificação: 25/07/2022", "Compartilhe:"]
    assert sentences == expected, case1.base.get("href")


def test_get_sentences_id_dados_basicos(case1):
    sentences = get_sentences_id_dados_basicos(case1)
    expected = [
        "O que é?",
        "O Projeto Salas Verdes tem como objetivo incentivar a implantação de espaços educadores para atuarem como centros de informação e formação ambiental em todo o país. A Sala Verde é um espaço dedicado ao desenvolvimento de atividades de caráter educacional, voltadas à temática socioambiental e cultural, que visam contribuir e estimular a discussão crítica, a organização e o fortalecimento de identidades grupais. As instituições que queiram criar uma sala verde devem concorrer à chamada pública, submetendo ao MMA um Projeto Político Pedagógico. Ao chancelar uma Sala Verde, o MMA reconhece a sua relevância e certifica que o projeto apresentado está alinhado com as diretrizes e objetivos da Política Nacional de Educação Ambiental. Estão entre as principais ações realizadas pelo MMA em prol das salas verdes: Acompanhar as atividades realizadas pelas salas verdes; Dar visibilidade às atividades desenvolvidas pela Sala Verde no portal do projeto, grupo de facebook e e-mail; Divulgar o espaço como referência em meio ambiente na área de abrangência geográfica de sua localização; Enviar kits do Circuito Tela Verde para as salas verdes, caso tenham interesse em realizar atividades de educação ambiental utilizando material audiovisual; Disponibilizar, em meio digital, publicações e materiais do MMA, de suas entidades vinculadas e de potenciais parceiros institucionais; Informar sobre a disponibilidade de cursos lançados na Plataforma de Educação à distância do MMA.",
    ]
    assert sentences == expected, case1.base.get("href")


@pytest.mark.parametrize(
    "tag, expected",
    (
        ("<p>test</p>", ["test"]),
        ("<p>test <span>test</span> test</p>", ["test test test"]),
        ("<p>test <div>test</div><br> test</p>", ["test test", "test"]),
        ("<p>test <br><br>test</p>", ["test", "test"]),
        ("<p>test <br><br>test<br><br></p>", ["test", "test"]),
        ("<span>test</span>", ["test"]),
        ("<div>test <span>test</span></div>", ["test", "test"]),
    ),
)
def test_get_sentence_by_tag(tag, expected):
    soup = BeautifulSoup(tag, "html.parser")
    tag = soup.find(True)
    result = get_sentence_by_tag(tag)
    assert result == expected, tag.name


def test_get_sentences_id_solicitantes(case1):
    sentences = get_sentences_id_solicitantes(case1)
    expected = [
        "Quem pode utilizar este serviço?",
        "Instituições com capacidade comprovada de atuação na área de Educação Ambiental.",
        "Para concorrer à chamada pública e implementar uma Sala Verde a instituição deve ter:",
        "Projeto Político Pedagógico - PPP: é o documento que traça uma proposta de ação pedagógica e social para o espaço da Sala Verde. O PPP consiste na formulação e enunciação de uma proposta educacional, suas bases conceituais e políticas até sua operacionalização.",
        "Espaço: infraestrutura mínima, devendo contar pelo menos com espaço físico com cadeiras, mesas e estantes. Há ainda exemplos de Salas Verdes que desenvolvem seus projetos de forma itinerante, utilizando a estrutura de ônibus, trens, barcos, caminhões;",
        "Equipe: a Sala Verde deve contar com uma equipe para o desenvolvimento de suas atividades. A equipe deve se responsabilizar por catalogar e manter em ordem o acervo de livros e materiais, promover atividades educativas, bem como coordenar, acompanhar e avaliar a implementação do Projeto Político Pedagógico- PPP;",
        "Equipamentos e recursos: não é necessário que a Sala Verde disponha inicialmente de recursos adicionais, além dos recursos humanos e da infraestrutura mínima já mencionada. Considera-se que recursos adicionais, tais como computadores, projetores, quadros podem ser adquiridos e incorporados ao patrimônio da instituição à medida que o projeto se fortaleça e se articule com outras iniciativas;",
    ]

    assert sentences == expected, case1.base.get("href")


def test_get_sentences_id_etapas_servico(case1):
    sentences = get_sentences_id_etapas_servico(case1)
    expected = [
        "Etapas para a realização deste serviço",
        "Submeter o Projeto Político Pedagógico (PPP) para avaliação e seleção pela equipe técnica do MMA",
        "As instituições interessadas em criar uma sala verde devem submeter o seu PPP ao MMA após o lançamento de chamada pública. O PPP deve conter, no mínimo: Identificação do projeto; histórico e justificativa; objetivos gerais e específicos; programação de ações e metas; metodologia; mapeamento e identificação dos recursos; cronograma de atividades; estratégias de monitoramento e avaliação; público e região de atuação; referências bibliográficas.",
        "Canais de prestação",
        "E-mail :",
        "sissalasverdes@mma.gov.br",
        "Documentação",
    ]

    for i in range(len(expected)):
        assert sentences[i] == expected[i], (
            sentences[i],
            case1.base.get("href"),
        )


def test_get_sentences_id_outras(case1):
    sentences = get_sentences_id_outras(case1)
    expected = [
        "Outras Informações",
        "Quanto tempo leva?",
        "Em média 90 dia(s) útil(eis) é o tempo estimado para a prestação deste serviço.",
        "Este serviço é gratuito para o cidadão.",
        "Para mais informações ou dúvidas sobre este serviço, entre em contato",
        "Endereço de correio eletrônico: salaverde@mma.gov.br",
        "Telefone: 61 2028-1207",
        "Este é um serviço do(a) Ministério do Meio Ambiente . Em caso de dúvidas, reclamações ou sugestões favor contactá-lo.",
        "Validade do Documento",
        "Sem validade.",
        "Informações adicionais ao tempo de validade",
        "Cada Sala Verde recebe um Banner, com a logomarca do MMA, representando a aprovação e chancela do MMA com relação à existência do espaço educador. Não existe um prazo de validade para o banner. Além disso, a qualquer momento, mediante justificativa, a instituição pode solicitar a inativação da sala verde.",
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
    ]

    for i in range(len(expected)):
        assert sentences[i] == expected[i], (
            sentences[i],
            case1.base.get("href"),
        )


def test_get_sentences_div_canais_atendimento(case1):
    sentences = get_sentences_div_canais_atendimento(case1)
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

    assert sentences == expected, case1.base.get("href")


def test_get_sentences_id_category(case1):
    sentences = get_sentences_id_category(case1)
    expected = [
        "Tags:",
        "Educação Ambiental",
        "Espaço Educador",
        "Sala Verde",
        "Socioambiental",
    ]

    assert sentences == expected, case1.base.get("href")


def test_get_sentences_div_avaliacao(case1):
    sentences = get_sentences_div_avaliacao(case1)
    expected = [
        "Esta página foi útil para você?",
    ]

    assert sentences == expected, case1.base.get("href")


def test_get_sentences_div_portal_footer(case1):
    sentences = get_sentences_div_portal_footer(case1)
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
        "Últimas Notícias do GOV.BR",
        "Últimas notícias",
        "Serviços para o cidadão",
        "Saúde",
        "Agricultura e Pecuária",
        "Cidadania e Assistência Social",
        "Cultura e Esporte",
        "Economia e Gestão Pública",
        "Educação e Pesquisa",
        "Energia",
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

    assert sentences == expected, case1.base.get("href")
