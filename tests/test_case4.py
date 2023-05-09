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


def test_get_sentences_body_header(case4):
    sentences = get_sentences_body_header(case4)
    expected = [
        "Órgãos do Governo",
        "Acesso à Informação",
        "Legislação",
        "Acessibilidade",
        "Serviços e Informações do Brasil",
    ]
    assert sentences == expected, case4.base.get("href")


def test_get_sentences_nav_breadcrumbs(case4):
    sentences = get_sentences_nav_breadcrumbs(case4)
    expected = [
        "Serviços",
        "Denunciar violação de direitos humanos",
    ]
    assert sentences == expected, case4.base.get("href")


def test_get_sentences_div_listagem_servicos(case4):
    sentences = get_sentences_div_listagem_servicos(case4)
    expected = [
        "Assistência Social",
        "Rede de Assistência e Proteção Social",
        "Proteção Social",
    ]
    assert sentences == expected, case4.base.get("href")


def test_get_sentences_div_contentcore_header(case4):
    sentences = get_sentences_div_contentcore_header(case4)
    expected = [
        "Denunciar violação de direitos humanos (Disque 100)",
        '''" Disque Direitos Humanos – Disque 100" , " Direitos Humanos Brasil"''',
        "Iniciar",
    ]

    assert sentences == expected, set(sentences).difference(expected)


def test_get_sentences_div_contentcore_avaliacao_container(case4):
    sentences = get_sentences_div_contentcore_avaliacao_container(case4)
    expected = ["Avaliação: 4.0      (1)"]
    assert sentences == expected, sentences


def test_get_sentences_div_id_viewlet_above_content_body(case4):
    sentences = get_sentences_div_id_viewlet_above_content_body(case4)
    expected = ["Última Modificação: 05/01/2023", "Compartilhe:"]
    assert sentences == expected, case4.base.get("href")


def test_get_sentences_id_dados_basicos(case4):
    sentences = get_sentences_id_dados_basicos(case4)
    expected = [
        "O que é?",
        "O Disque Direitos Humanos - Disque 100 é um serviço disseminação de informações sobre direitos de grupos vulneráveis e de denúncias de violações de direitos humanos.",
        "O serviço pode ser considerado como “pronto socorro” dos direitos humanos e atende graves situações de violações que acabaram de ocorrer ou que ainda estão em curso, acionando os órgãos competentes e possibilitando o flagrante.",
        "Qualquer pessoa pode reportar alguma notícia de fato relacionada a violações de direitos humanos, da qual seja vítima ou tenha conhecimento.",
        "Por meio desse serviço, o Ministério da Mulher, da Família e dos Direitos Humanos recebe, analisa e encaminha aos órgãos de proteção e responsabilização as denúncias de violações de direitos de crianças e adolescentes, pessoas idosas, pessoas com deficiência, população LGBT, população em situação de rua, entre outros.",
        "O serviço funciona diariamente, 24 horas, por dia, incluindo sábados, domingos e feriados. As ligações podem ser feitas de todo o Brasil por meio de discagem direta e gratuita, de qualquer terminal telefônico fixo ou móvel, bastando discar 100.",
        "O Disque 100 recebe, analisa e encaminha denúncias de violações de direitos humanos relacionadas aos seguintes grupos e/ou temas:",
        "Crianças e adolescentes",
        "Pessoas idosas",
        "Pessoas com deficiência",
        "Pessoas em restrição de liberdade",
        "População LGBT",
        "População em situação de rua",
        "Discriminação ética ou racial",
        "Tráfico de pessoas",
        "Trabalho escravo",
        "Terra e conflitos agrários",
        "Moradia e conflitos urbanos",
        "Violência contra ciganos, quilombolas, indígenas e outras comunidades tradicionais",
        "Violência policial (inclusive das forças de segurança pública no âmbito da intervenção federal no estado do Rio de Janeiro)",
        "Violência contra comunicadores e jornalistas",
        "Violência contra migrantes e refugiados",
        "Pessoas com Doenças Raras",
        'Para mais informações, visite a seção " Perguntas Frequentes " da página do Ministério da Mulher, da Família e dos Direitos Humanos .',
    ]
    for i in range(len(expected)):
        assert sentences[i] == expected[i], sentences[i]

    assert len(sentences) == len(expected)


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


def test_get_sentences_id_solicitantes(case4):
    sentences = get_sentences_id_solicitantes(case4)
    expected = [
        "Quem pode utilizar este serviço?",
        "Qualquer cidadão pode fazer uma denúncia sobre violações de direitos humanos da qual seja a vítima ou mesmo tenha conhecimento de que acontece com outra pessoa.",
    ]

    assert sentences == expected, set(sentences).difference(expected)


def test_get_sentences_id_etapas_servico(case4):
    sentences = get_sentences_id_etapas_servico(case4)
    expected = [
        "Etapas para a realização deste serviço",
        "Fazer uma denúncia",
        "O Disque Direitos Humanos – Disque 100 está disponível diariamente, 24 horas por dia, incluindo sábados, domingos e feriados. As denúncias são registradas e encaminhadas aos órgãos competentes. Também é possível fazer reclamações, sugestões ou elogios sobre o funcionamento dos serviços de atendimento.",
        "Canais de prestação",
        "Telefone :",
        "No Brasil: 100",
        "As ligações podem ser feitas de todo o Brasil, gratuitamente, de qualquer telefone fixo ou móvel (celular): basta discar 100.",
        "Em outros países:",
        "Passo 1: Digite o número do país em que você estiver (confira abaixo)",
        "Passo 2: Escolha o idioma. Tecle 1 para português ou 2 para inglês",
        "Passo 3: Aperte 1 novamente",
        "Passo 4: Ligue para o número 61 3535-8333",
        "País",
        "Telefone",
        "África do Sul",
        "0800 99 00 55",
        "Alemanha",
        "0800 08 000 55",
        "Argentina",
        "0800 999 55 00",
        "0800 999 55 01",
        "0800 999 55 03",
        "0800 555 55 00",
        "Austrália",
        "1800 88 15 50",
        "Áustria",
        "0800 200 255",
        "Bélgica",
        "0800 100 55",
        "Bolívia",
        "800 1000 55",
        "Canadá",
        "1800 46 366 56",
        "Chile",
        "800 360 220",
        "800 800 272",
        "China",
        "800 4900 125",
        "Chipre",
        "800 932 91",
        "Cingapura",
        "8000 55 05 50",
        "Colômbia",
        "01800 955 00 10",
        "Coreia do Sul",
        "00722055",
        "00309551",
        "Dinamarca",
        "808 855 25",
        "Eslováquia",
        "0800 00 55 00",
        "Espanha",
        "900 99 00 55",
        "Estados Unidos",
        "1800 745 55 21",
        "Formosa",
        "801550055",
        "França",
        "0800 99 00 55",
        "Grécia",
        "800 161 220 54 194",
        "Guiana Francesa",
        "0800 99 00 55",
        "Holanda",
        "08 000 220 655",
        "Hungria",
        "068 000 5511",
        "Israel",
        "1809494550",
        "Itália",
        "800 172 211",
        "Japão",
        "005 395 51",
        "006 635 055",
        "Luxemburgo",
        "0800 200 55",
        "México",
        "01800 123 02 21",
        "Noruega",
        "800 195 50",
        "Panamá",
        "008 000 175",
        "Paraguai",
        "008 55 800",
        "Peru",
        "0800 50 190",
        "Polônia",
        "008 00 491 14 88",
        "Portugal",
        "800 800 550",
        "Reino Unido",
        "0800 89 00 55",
        "República Dominicana",
        "1800 7518500",
        "Rússia",
        "810 800 20 971 049",
        "Suécia",
        "207 990 55",
        "Suíça",
        "0800 555 251",
        "Uruguai",
        "000455",
        "Venezuela",
        "0800 100 15 50",
        "Web :",
        "Disque 100",
        "E-mail :",
        "ouvidoria@mdh.gov.br",
        "Aplicativo móvel :",
        "Direitos Humanos Brasil",
        "Postal :",
        "Ouvidoria Nacional de Direitos Humanos",
        "Ministério da Mulher, da Família e dos Direitos Humanos",
        "Esplanada dos Ministérios Bloco A – 9º andar",
        "CEP: 70.049-900 – Brasília, DF",
        "Presencial :",
        "Ouvidoria Nacional de Direitos Humanos",
        "Esplanada dos Ministérios Bloco A – Térreo",
        "CEP: 70.049-900 – Brasília, DF",
        "Dias de atendimento: de segunda à sexta-feira, exceto aos feriados.",
        "Horário de atendimento: de 9h às 12h e de 14h às 18h.",
        "Tempo estimado de espera : Até 20 minuto(s)",
        "Aplicativo móvel :",
        "Desde 29 de outubro de 2020, o Disque 100 está disponível pelo WhatsApp.",
        "Para receber atendimento ou fazer denúncias, basta o cidadão enviar mensagem para o número:",
        "61 99656-5008",
        "Após resposta automática, ele será atendido por uma pessoa da equipe da central única dos serviços.",
        "Aplicativo móvel :",
        "Também é possível utilizar o Disque 100 por meio do Telegram, basta digitar “Direitoshumanosbrasil” na busca do aplicativo.",
        "Após uma mensagem automática inicial, o atendimento será realizado pela equipe do Disque Direitos Humanos – Disque 100.",
        "Tempo de duração da etapa",
        "Atendimento imediato",
        "Acompanhamento da denúncia",
        "Após o registro, a denúncia é analisada e encaminhada aos órgãos de proteção, defesa e responsabilização em direitos humanos, respeitando as competências de cada órgão.",
        "Se o cidadão quiser acompanhar a denúncia, basta ligar para o Disque 100, fornecer o número de protocolo e confirmar os dados da denúncia.",
        "Canais de prestação",
        "Telefone :",
        "No Brasil: 100.",
        "As ligações podem ser feitas de todo o Brasil, gratuitamente, de qualquer telefone fixo ou móvel (celular): basta discar 100.",
        "Em outros países:",
        "Passo 1: Digite o número do país em que você estiver (confira abaixo)",
        "Passo 2: Escolha o idioma. Tecle 1 para português ou 2 para inglês",
        "Passo 3: Aperte 1 novamente",
        "Passo 4: Ligue para o número 61 3535-8333",
        "País",
        "Telefone",
        "África do Sul",
        "0800 99 00 55",
        "Alemanha",
        "0800 08 000 55",
        "Argentina",
        "0800 999 55 00",
        "0800 999 55 01",
        "0800 999 55 03",
        "0800 555 55 00",
        "Austrália",
        "1800 88 15 50",
        "Áustria",
        "0800 200 255",
        "Bélgica",
        "0800 100 55",
        "Bolívia",
        "800 1000 55",
        "Canadá",
        "1800 46 366 56",
        "Chile",
        "800 360 220",
        "800 800 272",
        "China",
        "800 4900 125",
        "Chipre",
        "800 932 91",
        "Cingapura",
        "8000 55 05 50",
        "Colômbia",
        "01800 955 00 10",
        "Coreia do Sul",
        "00722055",
        "00309551",
        "Dinamarca",
        "808 855 25",
        "Eslováquia",
        "0800 00 55 00",
        "Espanha",
        "900 99 00 55",
        "Estados Unidos",
        "1800 745 55 21",
        "Formosa",
        "801550055",
        "França",
        "0800 99 00 55",
        "Grécia",
        "800 161 220 54 194",
        "Guiana Francesa",
        "0800 99 00 55",
        "Holanda",
        "08 000 220 655",
        "Hungria",
        "068 000 5511",
        "Israel",
        "1809494550",
        "Itália",
        "800 172 211",
        "Japão",
        "005 395 51",
        "006 635 055",
        "Luxemburgo",
        "0800 200 55",
        "México",
        "01800 123 02 21",
        "Noruega",
        "800 195 50",
        "Panamá",
        "008 000 175",
        "Paraguai",
        "008 55 800",
        "Peru",
        "0800 50 190",
        "Polônia",
        "008 00 491 14 88",
        "Portugal",
        "800 800 550",
        "Reino Unido",
        "0800 89 00 55",
        "República Dominicana",
        "1800 7518500",
        "Rússia",
        "810 800 20 971 049",
        "Suécia",
        "207 990 55",
        "Suíça",
        "0800 555 251",
        "Uruguai",
        "000455",
        "Venezuela",
        "0800 100 15 50",
        "Tempo de duração da etapa",
        "Não estimado ainda",
    ]

    for i in range(len(expected)):
        assert sentences[i] == expected[i], (
            sentences[i],
            case4.base.get("href"),
        )


def test_get_sentences_id_outras(case4):
    sentences = get_sentences_id_outras(case4)
    expected = [
        "Outras Informações",
        "Quanto tempo leva?",
        "Atendimento imediato",
        "Este serviço é gratuito para o cidadão.",
        "Para mais informações ou dúvidas sobre este serviço, entre em contato",
        "Disque 100",
        "Este é um serviço do(a) Ministério da Mulher, da Família e dos Direitos Humanos . Em caso de dúvidas, reclamações ou sugestões favor contactá-lo.",
        "Legislação",
        "Lei nº 13.010, de 26 de Junho de 2014",
        "Lei nº 13.684 de 21/06/2018",
        "Decreto nº 9.937 de 24/07/2019",
        "Decreto nº 7.177, de 12 de Maio de 2010",
        "Tratamento a ser dispensado ao usuário no atendimento",
        "De acordo com a Lei nº 13.460, de 26 de Junho de 2017, o usuário de serviço público tem direito à adequada prestação dos serviços, devendo os agentes públicos e prestadores de serviços públicos observar as seguintes diretrizes:",
        "I - urbanidade, respeito, acessibilidade e cortesia no atendimento aos usuários;",
        "II - presunção de boa-fé do usuário;",
        "III - atendimento por ordem de chegada, ressalvados casos de urgência e aqueles em que houver possibilidade de agendamento, asseguradas as prioridades legais às pessoas com deficiência, aos idosos, às gestantes, às lactantes e às pessoas acompanhadas por crianças de colo;",
        "IV - adequação entre meios e fins, vedada a imposição de exigências, obrigações, restrições e sanções não previstas na legislação;",
        "V - igualdade no tratamento aos usuários, vedado qualquer tipo de discriminação;",
        "VI - cumprimento de prazos e normas procedimentais;",
        "VII - definição, publicidade e observância de horários e normas compatíveis com o bom atendimento ao usuário;",
        "VIII - adoção de medidas visando a proteção à saúde e a segurança dos usuários;",
        "IX - autenticação de documentos pelo próprio agente público, à vista dos originais apresentados pelo usuário, vedada a exigência de reconhecimento de firma, salvo em caso de dúvida de autenticidade;",
        "X - manutenção de instalações salubres, seguras, sinalizadas, acessíveis e adequadas ao serviço e ao atendimento;",
        "XI - eliminação de formalidades e de exigências cujo custo econômico ou social seja superior ao risco envolvido;",
        "XII - observância dos códigos de ética ou de conduta aplicáveis às várias categorias de agentes públicos;",
        "XIII - aplicação de soluções tecnológicas que visem a simplificar processos e procedimentos de atendimento ao usuário e a propiciar melhores condições para o compartilhamento das informações;",
        "XIV - utilização de linguagem simples e compreensível, evitando o uso de siglas, jargões e estrangeirismos; e",
        "XV - vedação da exigência de nova prova sobre fato já comprovado em documentação válida apresentada.",
        "Informações sobre as condições de acessibilidade, sinalização, limpeza e conforto dos locais de atendimento",
        "O usuário do serviço público, conforme estabelecido pela Lei nº 13.460, de 26 de Junho de 2017, tem direito a atendimento presencial, quando necessário, em instalações salubres, seguras, sinalizadas, acessíveis e adequadas ao serviço e ao atendimento.",
        "Informação sobre quem tem direito a tratamento prioritário",
        "Têm atendimento prioritário as pessoas com deficiência, os idosos com idade igual ou superior a 60 (sessenta) anos, as gestantes, as lactantes, as pessoas com crianças de colo e os obesos, de acordo com a Lei nº 10.048, de 8 de novembro de 2000.",
    ]

    for i in range(len(expected)):
        assert sentences[i] == expected[i], (sentences[i], expected[i])


def test_get_sentences_div_canais_atendimento(case4):
    sentences = get_sentences_div_canais_atendimento(case4)
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

    assert sentences == expected, case4.base.get("href")


def test_get_sentences_id_category(case4):
    sentences = get_sentences_id_category(case4)
    expected = [
        "Tags:",
        "direitos e garantias fundamentais",
        "direitos da criança e do adolescente",
        "igualdade racial",
        "liberdade de expressão e manifestação de pensamento",
        "respeito às diferenças",
        "diversidade de manifestações culturais, políticas e religiosas",
    ]

    assert sentences == expected, set(sentences).difference(expected)


def test_get_sentences_div_avaliacao(case4):
    sentences = get_sentences_div_avaliacao(case4)
    expected = [
        "Esta página foi útil para você?",
    ]

    assert sentences == expected, case4.base.get("href")


def test_get_sentences_div_portal_footer(case4):
    sentences = get_sentences_div_portal_footer(case4)
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
